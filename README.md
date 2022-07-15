# stress-testing
Stress Test Practice

1. Create simple web page that accept requests and stores data from request to database
2. Prepare siege urls file
3. Run siege with different concurrency ( 10, 25, 50, 100 )
4. Find resource availability, avg response time, throughput
5. Implement probabilistic cache flushing

Load testing results

Concurrency 10

| Caching            | Availability     | Avg. response time | Throughput  | Transaction rate |
|--------------------|------------------|--------------------|-------------|------------------|
| No cache           | 100%             | 0.97 secs          | 0.00 MB/sec | 10.25 trans/sec  |
| Simple cache       | 100%             | 0.04 secs          | 0.01 MB/sec | 258.72 trans/sec |
| Probalistic cache  | 100%             | 0.04 secs          | 0.01 MB/sec | 229.34 trans/sec |

Concurrency 25

| Caching            | Availability     | Avg. response time | Throughput  | Transaction rate |
|--------------------|------------------|--------------------|-------------|------------------|
| No cache           | 100%             | 2.49 secs          | 0.00 MB/sec | 9.81 trans/sec   |
| Simple cache       | 100%             | 0.10 secs          | 0.01 MB/sec | 250.44 trans/sec |
| Probalistic cache  | 100%             | 0.10 secs          | 0.01 MB/sec | 245.97 trans/sec |

Concurrency 50

| Caching            | Availability     | Avg. response time | Throughput  | Transaction rate |
|--------------------|------------------|--------------------|-------------|------------------|
| No cache           | 100%             | 4.76 secs          | 0.00 MB/sec | 10.06 trans/sec  |
| Simple cache       | 100%             | 0.21 secs          | 0.01 MB/sec | 240.89 trans/sec |
| Probalistic cache  | 100%             | 0.19 secs          | 0.01 MB/sec | 258.53 trans/sec |

Concurrency 100

| Caching            | Availability     | Avg. response time | Throughput  | Transaction rate |
|--------------------|------------------|--------------------|-------------|------------------|
| No cache           | 100%             | 9.01 secs          | 0.00 MB/sec | 10.10 trans/sec  |
| Simple cache       | 100%             | 0.37 secs          | 0.01 MB/sec | 267.08 trans/sec |
| Probalistic cache  | 100%             | 0.46 secs          | 0.01 MB/sec | 214.19 trans/sec |