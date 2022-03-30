## web debugging

### docker commands I used for this task
docker run --help
docker run -p 8080:80 -d -it holbertonschool/265-0
docker ps
docker ps -a
docker exec -it c8094a8e19d0 echo 'cat'
docker exec -it c8094a8e19d0 hostname
docker exec -it c8094a8e19d0 apt-get update
docker exec -it c8094a8e19d0 apt install apache2
docker exec -it c8094a8e19d0 apache2ctl start
curl localhost:8080
