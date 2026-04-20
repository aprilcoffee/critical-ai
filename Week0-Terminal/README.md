# Command Line & Python Environment

Welcome back. ✧*｡٩(ˊᗜˋ*)و✧*｡

Before we can do anything with Python — before we can install Ollama, run a model, or write a single line of creative code — we need to become friends with the **command line**. For many of you this will be the first time opening it. Don't worry. It looks scary because it is just text, but that is also why it is powerful: everything you do here is explicit, nothing is hidden behind a button.

Today we will:

1. Open the terminal on your machine
2. Learn ~8 commands that will carry you through the rest of the course
3. Check whether Python is installed (and install it if not)
4. Create a **virtual environment** — a little sealed room where we can install libraries without breaking your system

The goal by the end of class: you can open a terminal, navigate to a folder, and activate a Python virtual environment without looking at this sheet.

---

## 0. Why the command line?

You already use graphical interfaces every day — Finder, Explorer, Photoshop, VSCode. The command line (**CLI**, *Command Line Interface*) is just another way of talking to the computer, but:

- it is **the same on every machine** (almost), so tutorials and documentation are written for it
- it lets you **automate** — anything you type can be saved into a script
- it is **honest** — the computer only does exactly what you wrote, nothing more

When people talk about "the terminal", "the shell", "bash", "zsh", "PowerShell" — they mean variations of the same thing: a text window where you type commands, one per line, and the computer replies.

---

## 1. Open your terminal

### 🍎 macOS — Terminal

- `Cmd + Space` → type `Terminal` → `Enter`
- Or: Applications → Utilities → Terminal

You will see something like:

```
ting@MacBook-Pro ~ %
```

That `%` (or sometimes `$`) is the **prompt**. It is waiting for you. The shell you are using is called **zsh** on modern macOS.

### 🪟 Windows — PowerShell

- `Win` key → type `PowerShell` → `Enter`
- Or right-click the Start button → *Terminal* / *Windows PowerShell*

You will see something like:

```
PS C:\Users\ting>
```

The `PS` stands for PowerShell, and the `>` is the prompt.

> ⚠️ On Windows, please **do not** use the old "Command Prompt" (`cmd.exe`). Always use **PowerShell** (or Windows Terminal). The commands below assume PowerShell.

---

## 2. The eight commands you actually need

The good news: most basic commands work **the same on Mac and PowerShell**, because Microsoft made aliases. Where they differ, I show both.

### 2.1 Where am I? → `pwd`

`pwd` means *print working directory*. It tells you where in the filesystem your terminal currently is.

```bash
pwd
```

Mac output:
```
/Users/ting
```

Windows output:
```
C:\Users\ting
```

### 2.2 What's here? → `ls`

`ls` means *list*. It shows the files and folders in the current directory.

```bash
ls
```

On both Mac and PowerShell this works. On old Windows `cmd.exe` you would need `dir` — but we are not using `cmd.exe`.

To see **hidden files** (files starting with `.`):

| macOS | Windows PowerShell |
|---|---|
| `ls -a` | `ls -Force` |

### 2.3 Go somewhere → `cd`

`cd` means *change directory*. It is how you move around.

```bash
cd Desktop
cd my-project
cd ..          # go up one level
cd ~           # go to your home folder
cd /           # go to the root (Mac)
```

On Windows, `cd ~` also works in PowerShell. `cd ..` works on both.

💡 **Tip:** type the first few letters of a folder name, then press `Tab`. The shell will autocomplete. This will save your life.

### 2.4 Make a folder → `mkdir`

```bash
mkdir creative-coding
```

Works the same on both.

### 2.5 Make an empty file

| macOS | Windows PowerShell |
|---|---|
| `touch hello.txt` | `New-Item hello.txt` |

### 2.6 Look inside a file → `cat`

```bash
cat hello.txt
```

Works on both. (PowerShell has `Get-Content`, but `cat` is an alias.)

### 2.7 Clear the screen

| macOS | Windows PowerShell |
|---|---|
| `clear` (or `Cmd + K`) | `cls` (or `clear`) |

### 2.8 Stop a running command

Press `Ctrl + C`. This works everywhere. If something runs forever, or you get stuck — `Ctrl + C`.

---

### Quick reference table

| What you want | macOS / Linux | Windows PowerShell |
|---|---|---|
| Where am I | `pwd` | `pwd` |
| List files | `ls` | `ls` |
| List hidden files | `ls -a` | `ls -Force` |
| Change directory | `cd folder` | `cd folder` |
| Go up one level | `cd ..` | `cd ..` |
| Home folder | `cd ~` | `cd ~` |
| Make folder | `mkdir name` | `mkdir name` |
| New empty file | `touch name.txt` | `New-Item name.txt` |
| Read file | `cat file.txt` | `cat file.txt` |
| Clear screen | `clear` | `cls` |
| Stop a process | `Ctrl + C` | `Ctrl + C` |

---

## 3. Practice — 5 minutes

Do this before we continue. Open your terminal and type each line:

```bash
cd ~
mkdir creative-coding
cd creative-coding
pwd
mkdir week1
cd week1
touch notes.txt
ls
cd ..
ls
```

If you got lost, type `cd ~` to go home and start again. Raise your hand and I will come. 🙌

---

## 4. Check if Python is installed

Both Mac and Windows now usually ship with some Python, but the version can be wrong or hidden. Let's check.

### macOS

```bash
python3 --version
```

If you see something like `Python 3.11.7` — good, you have it.
If you see `command not found` — we'll install it in the next step.

> ⚠️ On Mac, always use `python3` (not `python`). The bare `python` on old macOS pointed to Python 2, which is dead.

### Windows

```bash
python --version
```

or

```bash
py --version
```

If you see `Python 3.11.x` or higher — good.
If the Microsoft Store window opens instead — that means Python is not really installed, it's just a placeholder. Close it and install Python properly below.

**We need Python 3.10 or newer for this course.**

---

## 5. Install Python (if you need to)

### 🍎 macOS

Easiest route — use the installer:

1. Go to https://www.python.org/downloads/macos/
2. Download the latest **macOS 64-bit universal2 installer**
3. Run it. Next, next, done.
4. Close your terminal, open a new one, and check again:
   ```bash
   python3 --version
   ```

*Advanced alternative:* if you like package managers, install [Homebrew](https://brew.sh/) first, then:
```bash
brew install python
```
We will not go this route in class, but it is cleaner long-term.

### 🪟 Windows

1. Go to https://www.python.org/downloads/windows/
2. Download the **Windows installer (64-bit)**
3. Run it. **IMPORTANT:** on the first screen, tick the box
   ☑️ **Add Python to PATH**
   If you forget this, the `python` command will not work in PowerShell and you will have to reinstall.
4. Click *Install Now*.
5. Close PowerShell, open a new PowerShell window, check:
   ```bash
   python --version
   ```

---

## 6. Virtual environments — *why*

Here is the problem. When you `pip install` a library, it is installed **globally** on your machine. If project A needs `numpy 1.24` and project B needs `numpy 2.0`, they will fight. Over a year your Python becomes a swamp.

A **virtual environment** (venv) is a folder containing its own isolated copy of Python and its own libraries. When you "activate" it, any `pip install` happens only inside that folder. When you are done, you deactivate it and your system is untouched.

Think of it as a sketchbook per project. We will make a new venv for almost every week of this course.

---

## 7. Create a venv

Navigate into a project folder first:

```bash
cd ~/creative-coding/week1
```

Then create the environment:

### macOS

```bash
python3 -m venv venv
```

### Windows

```bash
python -m venv venv
```

This creates a folder called `venv` inside your project. (You can name it something else, but `venv` is the convention, and most `.gitignore` files already ignore it.)

### Activate it

This is the part with the biggest Mac/Windows difference.

**macOS:**
```bash
source venv/bin/activate
```

**Windows PowerShell:**
```bash
venv\Scripts\Activate.ps1
```

If it worked, your prompt now starts with `(venv)`:

```
(venv) ting@MacBook-Pro week1 %
```

You are now inside the bubble. Anything you `pip install` stays in this folder.

> 🪟 **Windows note** — if you get an error like
> *"running scripts is disabled on this system"*
> run this **once**, then try again:
> ```bash
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> This tells Windows it is OK to run trusted local scripts like your venv activator.

### Install something

Let's install one small package to test:

```bash
pip install requests
```

Then:

```bash
python -c "import requests; print(requests.__version__)"
```

You should see a version number. 🎉

### Leave the venv

```bash
deactivate
```

Your prompt returns to normal.

---

## 8. Conda — the alternative

**Conda** (specifically **Miniconda**) is an alternative to `venv`. It does the same job — isolated environments — but it can also manage non-Python dependencies (like CUDA, ffmpeg, system libraries), which matters for AI/ML work.

**Use `venv` if:** you want something small, built-in, minimal.
**Use `conda` if:** you plan to do heavy ML work (PyTorch, transformers), or you have previously broken your Python and want a fresh start in a separate sandbox.

### Install Miniconda

Download from https://www.anaconda.com/docs/getting-started/miniconda/install
→ pick your OS → run the installer.

On Mac, when installation finishes, **close and reopen your terminal**.
On Windows, a new program appears called **Anaconda Prompt** — use that instead of PowerShell for conda commands (at least at the beginning).

### Create a conda environment

```bash
conda create -n creative-ai python=3.11
```

`-n creative-ai` is the name of the environment. `python=3.11` is the Python version.

### Activate it

```bash
conda activate creative-ai
```

Your prompt now starts with `(creative-ai)`.

### Install a package

```bash
conda install numpy
```

or still use pip inside a conda env:

```bash
pip install requests
```

### Leave

```bash
conda deactivate
```

---

## 9. What to choose for this course

For **Einblick in Creative Coding**, I recommend:

- If you just want something working quickly → **`venv`** is enough.
- If your laptop already has conda, or you plan to keep working with local AI after this course → **Miniconda**.

Either is fine. What matters is that by next session you can:

- [ ] Open a terminal
- [ ] Navigate into a project folder
- [ ] Create an environment
- [ ] Activate it
- [ ] `pip install` something

---

## 10. Troubleshooting — the usual suspects

**`command not found: python3`** (Mac)
→ Python is not installed, or the installer didn't update PATH. Close terminal, open again.

**`python is not recognized as an internal or external command`** (Windows)
→ You forgot to tick *Add Python to PATH* during install. Reinstall Python with the box ticked, or repair the installation.

**`running scripts is disabled on this system`** (Windows)
→ Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`, answer `Y`.

**I activated my venv but `pip install` says "Permission denied"**
→ You are probably not actually inside the venv. Check your prompt — does it say `(venv)` at the start? If not, activate again.

**I installed a package but Python says it's not there**
→ You probably ran `pip install` **outside** the venv and then entered the venv. Activate first, then install.

**I deleted the `venv` folder, now what?**
→ That is fine. Virtual environments are disposable — just make a new one. **Never put anything important inside the `venv` folder**, only your own code outside it.

---

## 11. Homework / before next class

1. Make a folder on your machine called `creative-coding/` (you probably already did).
2. Inside, make a folder for next week: `week2-ollama/`.
3. In that folder, create a venv called `venv` and activate it.
4. Install one package of your choice (`pip install rich` is a fun one — try `python -c "from rich import print; print('[red]hello[/red]')"` after).
5. Deactivate it.

If any of this broke — take a screenshot of the error and send it in our channel. We will fix it together next session.

---

## Further reading — if you are curious

- **The Missing Semester of Your CS Education** (MIT) — a beautiful free course on the tools they never teach you: https://missing.csail.mit.edu/
- **Python venv docs** — the official reference, short and clear: https://docs.python.org/3/library/venv.html
- **Conda cheat sheet** — one page, very useful: https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html

See you next session — we will start with Ollama. 👾
