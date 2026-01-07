# How to open Python Shell on your OS?

The Python Shell (also known as the REPL — Read-Eval-Print Loop) is an interactive environment where you can type Python code and see the results immediately. It is perfect for testing short snippets of code or performing quick calculations.

Here is how you access and use it across different operating systems.

## 1. Opening the Shell

| Operating System | Method | Command |
|---|---|---|
| Windows | Command Prompt or PowerShell | python (or py) |
| macOS | Terminal | python3 |
| Linux | Terminal | python3 |

---

## 2. How to use it (All Systems)?

Once you run the command, you will see the Python version info followed by the prompt: >>>. This indicates that Python is ready for your input.

 * **Run a Command**: Type
   ```python
   print("Hello")
   ```
   and hit *Enter* .
 * **Do Math**: Type
   ```python
   10 + 5
   ```
   and hit *Enter* .
 * **Create Variables**: Type
   ```python
   x = 10
   x * 2
   ```
   to see the result.

> Note: The Shell doesn't "save" your work. Once you close the window, your variables and code disappear. For permanent code, you'll need to write a .py file.
>

---
 
## 3. Exiting the Shell

Getting out of the shell is one of the most common "stuck" moments for beginners.

 * The Command Method (Universal):
   Type `exit()` or `quit()` and hit *Enter* .
 * The Keyboard Shortcut:
   * Windows: Press *Ctrl + Z* and then hit *Enter* .
   * macOS / Linux: Press *Ctrl + D* .

---
   
## 4. Special OS-Specific Features

- **Windows**: The Python Launcher (py)
               Windows users often have the Python Launcher installed. Instead of typing `python`, you can type `py`. If you have multiple versions of Python installed (e.g., 3.11 and 3.12), you can specify which shell to open by typing py -3.11.
- **macOS & Linux**: The python vs python3 Trap
                     On many Mac and Linux systems, typing `python` might refer to an old, unsupported version (Python 2). To ensure you are using the modern shell you just installed, always use the command `python3`.

---

### IDLE (Integrated Development and Learning Environment)

Regardless of the OS, Python usually installs a graphical shell called IDLE.

 * On Windows, search for "IDLE" in the Start Menu.
 * On macOS, it’s in your Applications folder under the Python folder.
 * It provides a windowed version of the shell with helpful syntax highlighting (colors).
