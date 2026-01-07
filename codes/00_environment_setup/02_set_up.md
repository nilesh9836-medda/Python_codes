# How to set up Python on your os?

Installing Python is slightly different depending on your operating system. Here is the breakdown for the three major platforms.

## 1. Windows

Windows does not come with Python pre-installed. You have two main options:

### * Official Installer ( **Recommended** ):

   * Download the Windows Installer (64-bit) from python.org.
   * Run the .exe file.
   * Critical Step: Check the box *Add Python to PATH*  before clicking *Install Now*.
   * Once finished, open Command Prompt and type `python --version` to verify.
   
### * Microsoft Store:

   * Open the Microsoft Store and search for *Python*.
   * Select the latest version (e.g., Python 3.12) and click *Get*. This version is easier to manage and update, but has some limitations with system-level tasks.
   
---

## 2. macOS

macOS comes with a system version of Python, but it’s often outdated. You should install a modern version separately.

###  * Official Installer:

   * Download the macOS 64-bit universal2 installer from python.org.
   * Open the .pkg file and follow the wizard.
   * Run the `Install Certificates` command found in the Python folder in your Applications directory to ensure internet features work.
   
### * Homebrew (For Power Users):

   * If you have Homebrew installed, simply open your Terminal and type:
    `brew install python`
     
---

## 3. Linux

Most Linux distributions (like Ubuntu, Fedora, or Debian) come with Python 3 already installed.

 * Check First: Open your terminal and type `python3 --version`
 * Ubuntu/Debian: `sudo apt update && sudo apt install python3`
 * Fedora: `sudo dnf install python3`
 * Arch Linux: `sudo pacman -S python`

---

## Summary Table

| Feature | Windows | macOS | Linux |
|---|---|---|---|
| Pre-installed? | No | Yes (Old version) | Yes |
| Primary Method | .exe Installer | .pkg Installer | Package Manager (apt, dnf) |
| Terminal Command | python | python3 | python3 |
| Key Tip | Add to PATH | Install Certificates | Update via Sudo |

