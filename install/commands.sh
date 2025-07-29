docker pull ubuntu

docker run -it --name ubuntu1 ubuntu bash


apt update && \
    apt install -y curl wget vim htop net-tools iputils-ping dnsutils \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

