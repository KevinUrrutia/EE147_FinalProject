# EE147_FinalProject


## NVIDIA Performance Primitives Installation, a Sub Library of NVIDIA NCCL
Check the software requirements of your system:
* your environment needs glibc 2.17 or higher, CUDA version 10.0 or higher. To check this run the following commands

```
nvcc --version
ldd --version
```

Installing NCCL:
* Installing NCCL on ubuntu requires that you first make an account with nvidia to download the deb package https://developer.nvidia.com/nccl

* Go to the directory where the deb file was installed

```
sudo apt-key add /var/nccl-local-repo-ubuntu2004-2.12.10-cuda11.6/7fa2af80.pub
sudo dpkg -i nccl-local-repo-ubuntu2004-2.12.10-cuda11.6_1.0-1_amd64.deb
sudo apt update
sudo apt install libnccl2 libnccl-dev
```
## Install cuBlas
Install CuBlas by going to the Nvidia developer site for the sdk download
https://developer.nvidia.com/cublas

```
echo 'deb [trusted=yes] https://developer.download.nvidia.com/hpc-sdk/ubuntu/amd64 /' | sudo tee /etc/apt/sources.list.d/nvhpc.list
sudo apt-get update -y
sudo apt-get install -y nvhpc-22-3
```
