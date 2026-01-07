# Can you write and run Python code without using code editors or IDEs?

Yes, you absolutely can! In fact, this is how most developers worked before modern IDEs became popular. Every .py file is just a plain text file containing instructions for the Python interpreter.

## How to run a .py file?

Once you have saved your code (e.g., script.py) using a text editor like Notepad (Windows), TextEdit (Mac), or Gedit (Linux), follow these steps:
 1. Open your Terminal or Command Prompt.
 2. Navigate to the folder where you saved the file. Use the cd (change directory) command.
    Example:
    ```bash
    cd Documents/PythonProject
    ```

 3. Run the file by typing the Python command followed by your filename:
    * Windows:
     ```python
     python script.py
     ```
   
    * Mac/Linux:

     ```python
     python3 script.py
     ```

---

## Advantages of using a Simple Text Editor:

| Advantage | Explanation |
|---|---|
| Low Overhead | It uses almost no RAM or CPU. Your computer stays fast. |
| No Distractions | There are no complex menus, pop-ups, or buttons—just you and the code. |
| Deep Learning | Since there is no "Auto-complete," you are forced to memorize the syntax and keywords. |
| Portability | You can write code on any computer in the world without installing specialized software. |


---

### Disadvantages of using a Simple Text Editor:

| Disadvantage | Explanation |
|---|---|
| No Syntax Highlighting | In Notepad, everything is black text. It's much harder to spot a typo or a missing quote. |
| Difficult Debugging | If your code crashes, a text editor won't tell you why. You have to go back and forth between the editor and the terminal. |
| No Auto-indentation | Python relies on indentation (spaces). Simple editors won't automatically align your code, leading to "IndentationErrors." |
| No IntelliSense | You won't get "hints" for function names or variable names, which slows down your typing significantly. |
