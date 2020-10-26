import platform
import GPUtil
import os

# python screenfetch
print("-"*20, "Screenfetch", "-"*20)

uname = platform.uname()
GPUs = GPUtil.getGPUs()

listGPUs = []

for GPU in GPUs:
    GPU_Name = GPU.name
    GPU_VRAM = f"{GPU.memoryTotal} MB"
    listGPUs.append((GPU_Name))


GPUTemp = []

for temp in GPUs:
    GPU_Temp = f"{GPU.temperature} °C"
    GPUTemp.append((GPU_Temp))


print(f"User: {uname.node}")
print(f"OS: {uname.system}")
print(f"Release: {uname.release}")
print(f"Build version: {uname.version}")
print(f"CPU: {uname.processor}")
print(f"GPU: {listGPUs}")
print(f"GPU Temperature: {GPUTemp}")
print(f"System Architecture: {uname.machine}")
print("-"*54)
