import psycopg2
import psycopg2.pool
import random

pool = None

def get_pool():
    global pool
    if pool is None:
        pool = psycopg2.pool.SimpleConnectionPool(
            1, 4, database="test_perf", user="test_perf_user", password="test_pass", port=5432,
        )
    return pool


max_n = 1000_000 - 1


def get_by_index(index):
    conn = get_pool().getconn()
    cursor = conn.cursor()

    cursor.execute("select id, value from test where id = %s;", (index,))
    ((index, value),) = cursor.fetchall()
    cursor.close()
    get_pool().putconn(conn)
    return index, value

def get_random_row():
    index = random.randint(1, max_n)

    index, value = get_by_index(index)

    return index, value


def insert_row(index, value):
    conn = get_pool().getconn()

    cursor = conn.cursor()
    cursor.execute("INSERT INTO test (id, value) VALUES(%s, %s)", (index, value))

    conn.commit()

    cursor.close()
    get_pool().putconn(conn)