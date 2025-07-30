docker network create demo-network

docker run -d \
  --gpus all \
  --rm \
  --name dcgm-exporter --network demo-network \
  -p 9400:9400 nvcr.io/nvidia/k8s/dcgm-exporter:3.1.6-3.1.3-ubuntu20.04


  docker run -d   -p 9090:9090   -v /home/ubuntu/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml   --name prometheus  --network demo-network prom/prometheus