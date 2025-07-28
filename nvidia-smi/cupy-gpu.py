import cupy as cp
import json

# Get device properties for GPU 0
props = cp.cuda.runtime.getDeviceProperties(0)

# Convert byte string keys to readable string and print nicely
gpu_info = {
    'name': props['name'].decode('utf-8'),
    'totalGlobalMem (bytes)': props['totalGlobalMem'],
    'sharedMemPerBlock (bytes)': props['sharedMemPerBlock'],
    'regsPerBlock': props['regsPerBlock'],
    'warpSize': props['warpSize'],
    'memPitch': props['memPitch'],
    'maxThreadsPerBlock': props['maxThreadsPerBlock'],
    'maxThreadsDim': props['maxThreadsDim'],
    'maxGridSize': props['maxGridSize'],
    'clockRate (kHz)': props['clockRate'],
    'totalConstMem (bytes)': props['totalConstMem'],
    'major': props['major'],
    'minor': props['minor'],
    'multiProcessorCount (SMs)': props['multiProcessorCount'],
    'l2CacheSize': props['l2CacheSize'],
    'maxThreadsPerMultiProcessor': props['maxThreadsPerMultiProcessor'],
    'computeMode': props['computeMode'],
    'memoryClockRate (kHz)': props['memoryClockRate'],
    'memoryBusWidth (bits)': props['memoryBusWidth'],
    'concurrentKernels': props['concurrentKernels'],
    'pciBusID': props['pciBusID'],
    'pciDeviceID': props['pciDeviceID']
}

# Pretty print the results
print(json.dumps(gpu_info, indent=2))