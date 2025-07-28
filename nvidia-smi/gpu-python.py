# pip install nvidia-ml-py3
import pynvml

pynvml.nvmlInit()

device_count= pynvml.nvmlDeviceGetCount()

print(f"Number of devices: {device_count}")

for i in range(device_count):
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    print(f"Device {i}: {pynvml.nvmlDeviceGetName(handle)}")
    memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    temp_info = pynvml.nvmlDeviceGetTemperature(handle, 0)
    utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)


    print(f"    Temperature: {temp_info} C")
    print(f"    Total memory: {memory_info.total // (1024**2)} MB")
    print(f"    Used memory: {memory_info.used // (1024**2)} MB")
    print(f"    GPU Utilization: {utilization.gpu} %")
    print(f"    Memory Utilization: {utilization.memory} %")
  
pynvml.nvmlShutdown()