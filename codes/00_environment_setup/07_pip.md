# Python's Package Installer

Managing packages with **pip** (Python's Package Installer) is one of the most important skills for a Python developer. 

Here is a guide to the most common `pip` commands.

---

### 1. Searching and Installing

Before you install something, you usually want to make sure you have the right package name.

* **Install a package:**
```bash
pip install requests

```


* **Install a specific version:** (Useful if your code doesn't work with the newest version)
```bash
pip install requests==2.28.1

```


* **Upgrade a package:**
```bash
pip install --upgrade requests

```



---

### 2. Inspecting Your Environment

Once you have several packages installed, you need to know what's in your "sandbox."

* **List all installed packages:**
```bash
pip list

```


*This gives you a nice table of names and versions.*
* **Show details of a specific package:**
```bash
pip show pandas

```


*This tells you the author, the website, and most importantly, what other libraries it depends on.*

---

### 3. Uninstalling Packages

If you no longer need a library or installed the wrong one:

```bash
pip uninstall flask

```

*Note: It will ask you to confirm with `y/n` before deleting.*

---

### 4. Bulk Management

You shouldn't install things one by one when moving projects. Use your **requirements.txt** file.

* **Export your list:** `pip freeze > requirements.txt`
* **Install everything from a list:** `pip install -r requirements.txt`

---

### 5. Dealing with "Permission Denied" Errors

On Ubuntu, if you try to install a package **outside** of a virtual environment, you might get an error.

> **Warning:** Avoid using `sudo pip install`. This can mess up your Ubuntu system's internal Python files.

**If you must install globally, use the `--user` flag:**

```bash
pip install --user package_name

```

*But remember: 99% of the time, you should just activate your **venv** first.*

---

### Summary Table of `pip` Commands

| Goal | Command |
| :---: | :---: |
| **Install** | `pip install <name>` |
| **Remove** | `pip uninstall <name>` |
| **Update** | `pip install -U <name>` |
| **See everything** | `pip list` |
| **Check for security/bugs** | `pip check` |
| **Create a manifest** | `pip freeze > requirements.txt` |

