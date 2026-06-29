# Diffusers Setup on Windows

## Requirements

- Windows 10 or 11
- Python 3.10–3.12 from **python.org** (not the Microsoft Store version)
- NVIDIA GPU with CUDA (recommended) — CPU fallback works but is very slow

---

## Step 1 — Install Python

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download **Python 3.11** (recommended)
3. Run the installer
4. ✅ Check **"Add python.exe to PATH"** at the bottom before clicking Install

Verify in a new terminal:

```
python --version
```

---

## Step 2 — Create the virtual environment

Open **PowerShell** or **Command Prompt** in the folder where you want to work, then run:

```
python -m venv image
```

This creates a folder called `image/` with an isolated Python environment.

---

## Step 3 — Activate the environment

**Command Prompt (recommended, no extra steps):**
```
image\Scripts\activate.bat
```

**PowerShell:**
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
image\Scripts\Activate.ps1
```

> The `Set-ExecutionPolicy` line is required in PowerShell before activating.
> It only affects the current session and must be run each time you open a new PowerShell window.

Your prompt will change to show `(image)` — the environment is now active.

---

## Step 4 — Check your CUDA version

Before installing PyTorch, check which CUDA version your GPU driver supports:

```
nvidia-smi
```

Look for **CUDA Version** in the top-right corner of the output, e.g.:

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 546.33    Driver Version: 546.33    CUDA Version: 12.1                      |
```

> If `nvidia-smi` is not found, you either have no NVIDIA GPU or the driver is not installed.
> Download drivers at [https://www.nvidia.com/drivers](https://www.nvidia.com/drivers)

---

## Step 5 — Install PyTorch (match your CUDA version)

Pick the command that matches your CUDA version from `nvidia-smi`:

| CUDA Version | Install command |
|---|---|
| 13.1 | ⚠️ No wheel yet — use `cu130` below (see note) |
| 13.0 | `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130` |
| 12.8 | `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128` |
| 12.6 | `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126` |
| 12.4 | `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124` |
| 12.1 | `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121` |
| 11.8 | `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118` |
| No GPU / CPU only | `pip install torch torchvision` |

> **CUDA 13.1 (RTX 50-series)** — PyTorch does not yet publish a `cu131` wheel.
> Use `cu130` instead; it is forward-compatible and works on 13.x drivers.
>
> **Not sure?** The CUDA version in `nvidia-smi` is the **maximum** your driver supports.
> Installing a torch build for a lower CUDA version is always fine.

After installing torch, verify CUDA is detected:

```
python -c "import torch; print(torch.cuda.is_available())"
```

Should print `True`. If it prints `False`, re-check your CUDA version and reinstall torch with the correct `--index-url`.

---

## Step 6 — Install diffusers packages

```
pip install diffusers transformers accelerate pillow imageio[ffmpeg]
```

---

## Step 7 — Run the scripts

```
python image_simple.py
python video_simple.py
```

Output files will appear in the same folder: `image.png`, `video.mp4`

---

## Quick reference

| Task | Command |
|---|---|
| Allow scripts (PowerShell) | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` |
| Activate (PowerShell) | `image\Scripts\Activate.ps1` |
| Activate (cmd) | `image\Scripts\activate.bat` |
| Deactivate | `deactivate` |
| Check active Python | `python --version` |
| Check installed packages | `pip list` |

---

## Troubleshooting

**`python` not found** — Reinstall Python and check "Add to PATH"

**`cannot be loaded because running scripts is disabled`** — Run the `Set-ExecutionPolicy` command in Step 3 first

**CUDA out of memory** — The models are large. Close other GPU apps. If it still fails, add this line before `pipe(...)` in the script:
```python
pipe.enable_model_cpu_offload()
```

**First run is slow** — Models download automatically on first use (~7–10 GB). They cache locally so subsequent runs are fast.
