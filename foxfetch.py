#import
import platform
import csv
import shutil
import subprocess
import winreg
from concurrent.futures import ThreadPoolExecutor
#colors
ORANGE = "\033[38;2;255;128;0m"
RESET   = "\033[0m"
#logo
LOGO = r"""
    |\__/|
   /     \
  /_.~ ~,_\
     \@/
"""
#get os,kernel,cpu,gpu
def get_os():
    return platform.system()
def get_kernel():
    return platform.version()
def get_cpu():
    return platform.processor()
def get_gpu_nvidia():
    if not shutil.which("nvidia-smi"):
        return []

    fields = [
        "index",
        "name",
        "driver_version",
        "memory.total",
        "memory.used",
        "memory.free",
        "utilization.gpu",
        "temperature.gpu",
    ]
    command = [
        "nvidia-smi",
        f"--query-gpu={','.join(fields)}",
        "--format=csv,noheader,nounits",
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, timeout=5)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return []

    gpus = []
    for row in csv.reader(result.stdout.strip().splitlines()):
        gpus.append({field: value.strip() for field, value in zip(fields, row)})
    return gpus
#get gpu
def get_gpu():
    gpus = []
    try:
        base = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}")
    except OSError:
        return gpus
    i = 0
    while True:
        try:
            sub = winreg.EnumKey(base, i)
        except OSError:
            break
        i += 1
        try:
            k = winreg.OpenKey(base, sub)
            gpus.append({"Name": winreg.QueryValueEx(k, "DriverDesc")[0]})
            winreg.CloseKey(k)
        except OSError:
            pass
    winreg.CloseKey(base)
    return gpus
#print os,kernel,cpu,gpu
with ThreadPoolExecutor(max_workers=6) as pool:
    f_nvidia = pool.submit(get_gpu_nvidia)
    f_gpu = pool.submit(get_gpu)
    nvidia_gpus = f_nvidia.result()
    gpus = f_gpu.result()

info = [
    f"{ORANGE}os:{RESET} {get_os()}",
    f"{ORANGE}kernel:{RESET} {get_kernel()}",
    f"{ORANGE}cpu:{RESET} {get_cpu()}",
]
if gpus:
    info.append(f"{ORANGE}gpu:{RESET} {gpus[0]['Name']}")

logo_lines = LOGO.strip("\n").splitlines()
width = max(len(line) for line in logo_lines) + 3
rows = max(len(logo_lines), len(info))

for i in range(rows):
    left = logo_lines[i] if i < len(logo_lines) else ""
    right = info[i] if i < len(info) else ""
    print(f"{ORANGE}{left.ljust(width)}{RESET}{right}")