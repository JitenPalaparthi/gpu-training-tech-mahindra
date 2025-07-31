## Prometheus and Node Exporter 

```bash
docker network create demo-network
docker inspect demo-network 
 
docker network ls
docker run --name node-exporter --network demo-network prom/node-exporter

docker run -d --name prometheus1  --network demo-network -p 9090:9090 -v $PWD/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus

docker run -d --name prometheus2 --network demo-network -p 9091:9090 -v $PWD/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus

```