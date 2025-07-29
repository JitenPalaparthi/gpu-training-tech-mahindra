FROM nvidia/cuda:12.4.1-base-ubuntu22.04

WORKDIR /app

RUN apt update && \
    apt install -y python3.11 python3.11-venv python3.11-dev python3-pip && \
    apt install -y pciutils && \
    apt install -y nvidia-container-toolkit && \
    ln -sf /usr/bin/python3.11 /usr/bin/python3

RUN pip3 install tensorflow

COPY app.py .

ENTRYPOINT ["sh", "-c"]

CMD ["python3 app.py && nvidia-smi"]                            