# foxfetch

## Features

- Shows OS, kernel version, CPU and GPU
- GPU name is read from the Windows registry (works with AMD, NVIDIA and Intel)
- Optional NVIDIA details through `nvidia-smi`
- GPU queries run in parallel with `ThreadPoolExecutor`
- Orange colored labels using ANSI escape codes
- Can be compiled with Cython

## Requirements

- Windows (uses `winreg`)
- Python 3.x
- Terminal with ANSI color support (Windows Terminal, PowerShell)

### COPYRIGHT (C) akettunen 2026
