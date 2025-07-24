 1002  clear
 1003  docker ps
 1004  docker inspect n1
 1005  docker inspect n2
 1006  clear
 1007  docker ps
 1008  curl 172.17.0.2:80
 1009  docker rm -f n1 n2
 1010  docker run -d --name -p 9081:80  n1 nginx
 1011  docker run -d --name n1 -p 9081:80 nginx
 1012  docker run -d --name n2 -p 9082:80 nginx
 1013  docker ps
 1014  curl localhost:9082
 1015  curl localhost:9081
 1016  clear
 1017  docker ps