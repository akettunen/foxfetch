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

## Rust (recommended)
I have also made a identical program using Rust.
- https://github.com/akettunen/foxfetch-rs

## Pictures
<img width="1093" height="93" alt="image" src="https://github.com/user-attachments/assets/748ace95-96d0-4425-8775-84884528e15e" />

## COPYRIGHT (C) akettunen 2026
