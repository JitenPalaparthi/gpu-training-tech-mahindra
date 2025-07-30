#!/bin/bash

docker run -d \
  --rm \
  --runtime=nvidia \
  --network=gpu-net \
  --name=dcgm-exporter \
  -e NVIDIA_VISIBLE_DEVICES=all \
  -p 9400:9400 \
  nvcr.io/nvidia/k8s/dcgm-exporter:3.1.8-3.1.5-ubuntu20.04
