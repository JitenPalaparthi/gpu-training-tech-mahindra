1- brev login -t 

2. brev ssh workspace

3. docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi 

4.  brev org

5. brev org set org01

6. brev shell mmluser01


## nvidia docker containrs

```bash
apt list | grep nvidia-container-toolkit
```

```bash
apt intall nvidia-container-toolkit
```

## Build docker file

```bash
docker build . -t jpalaparthi/cuda-python-demo:v0.1
```

## Run docker file 

```bash
docker run -it --name nvidia1 --gpus all jpalaparthi/cuda-python-demo:v0.1
```

## Push Docker image 

```bash
docker push jpalaparthi/cuda-python-demo:v0.1
```