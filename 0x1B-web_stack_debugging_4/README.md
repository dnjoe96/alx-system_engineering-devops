## Webstack debugging 4

Idenifying and fixing apache server performance issue.

[ab](https://httpd.apache.org/docs/2.4/programs/ab.html]) is a tool for benchmarking your Apache Hypertext Transfer Protocol (HTTP) server. It is designed to give you an impression of how your current Apache installation performs. This especially shows you how many requests per second your Apache installation is capable of serving.

```bash
ab -c 100 -n 2000 localhost/
```

### Task 0
In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0

#### error from log -> /var/log/nginx/error.log
```
2022/05/03 11:32:19 [crit] 651#0: *1 open() "/usr/share/nginx/html/index.html" failed (24: Too many open files),
client: ::1, server: localhost, request: "GET / HTTP/1.0", host: "localhost"
```
#### solution
Setting the value of ULIMIT in /etc/default/nginx resolved the issue.
ULIMIT="n -2000"
