# Bao Bao's Python Practice Plan

Goals:

1. Recall the Python Basis that Bao has learned. (And also some basic console, git manipulation)
2. Get famalier with the Markdown (and some LaTeX syntax for formula) and be able to take note with it.
3. Practice keyboard typing and English when taking notes or coding.

> Also understand some basic knowledge like what is relative path and so on.

## Getting Started

First few steps to get started.

1. Open the terminal (`⌘ + space` and search for iTerm)
2. Go to the directory (folder) you want to place this project by using `cd` or maybe `ls` to see the content
3. Clone (download) this repository using `git clone https://github.com/baobaocoding/PythonBasis.git`
4. Go to this project directory `cd PythonBasis`
5. Open this directory as workspace using VSCode by typing `code .` (The `.` means current directory)

How to submit my changes?

1. Add the changes by either inside the VSCode's Source Control View or using `git add -A` to add all the changes you've made
2. Commit the changes by either inside the VSCode's Source Control View or using `git commit -m "the description of current changes"`
3. Submit/Upload/Synchronize the changes to GitHub by the left-bottom button in VSCode or using `git push`

How to get the latest update from Github?

1. Use the left-bottom button in VSCode or using `git fetch` and then `git pull` (make sure the current repository (directory) is clean (no unstage modification))

### Jupyter Notebook

> Get the jupyter notebook by `pip3 install jupyterlab`

```sh
# Open jupyter notebook in current directory
jupyter notebook
# Open the specific notebook file
jupyter notebook filename.ipynb
```

* Terminate the jupyter notebook server by `ctrl + c` or clicking Quit button on the webpage
* Create code block for Python code
* Create markdown block for notes

## Schedule

### Recall the Python Basis

| Subject                                          | Start Date | Finished (Y/N) |
| ------------------------------------------------ | ---------- | -------------- |
| [Variable and Basic Calculation](Python/VarCalc) | 2019/6/25  | Y (2019/6/27)  |
| [If Condition](Python/IfCondition)               | 2019/6/27  | Y (2019/8/22)  |
| [Loops](Python/Loop)                             | 2019/8/22  | Y (2019/8/23)  |
| [Function and Module](FunctionModule)            | 2019/8/23  | Y (2019/8/23)  |

### Kaggle Python

| Lesson                          | Start Date | Finished (Y/N) |
| ------------------------------- | ---------- | -------------- |
| Hello, Python                   | 2019/9/7   | N              |
| Functions and Getting Help      | -          | N              |
| Booleans and Conditionals       | -          | N              |
| Lists                           | -          | N              |
| Loops and List Comprehensions   | -          | N              |
| Strings and Dictionaries        | -          | N              |
| Working with External Libraries | -          | N              |

1. Goto the [Kaggle Learn Python page](https://www.kaggle.com/learn/python)
2. View the Tutorial of the Lesson
3. Click the link under Your Turn or the Exercise
   * The code is an jupyter notebook. In Kaggle it is called Kaggle Kernal
4. Edit the Code
   1. If encounter difficulties, uncommit the `qnum.hint()` and run it for the hint
   2. Uncommit the `qnum.solution()` to see the detail explination
   3. The `qnum.check()` will automatically check your solution
5. Execute the Code in order
   * Make sure the code block start with `from learntools.core import ...` has been executed first
   * For the shortcut, you can use `shift + enter` to run the current code block
6. Commit the changes online or download the notebook by clicking `File > Download notebook` and then commit locally

### To Be Put In Schedule

* String, List, Dict, (Tuple, Set)
* OOP (Class)
* Real word cases (Playing with external libraries)

## Note

> You can oragnize your notes here. First create a link to a file by Markdown link syntax `[link name](link to file or website)` to your file. And press `⌘` click left mouse button it will ask if to create the file. (If the file exist then it will jump to the file immediately.)

* [Python](Notes/Python.md)

## Resources

Bash/Shell (Console/Terminal/Command Line)

* [**Resources to learn Git**](https://try.github.io/)
  * [**Git-It**](https://github.com/jlord/git-it-electron#what-to-install)
    * [download for mac](https://github.com/jlord/git-it-electron/releases/download/4.4.0/Git-it-Mac-x64.zip)
* Codecademy
  * [**Learn the Command Line**](https://www.codecademy.com/learn/learn-the-command-line)
  * [Learn Git](https://www.codecademy.com/learn/learn-git)

Python

* [**Kaggle Python**](https://www.kaggle.com/learn/python)
* [**Python-100-Days**](https://github.com/jackfrued/Python-100-Days)
* Codecademy
  * [**Learn Python**](https://www.codecademy.com/learn/learn-python)
  * [**Learn Statistics With Python**](https://www.codecademy.com/learn/learn-statistics-with-python)
* [Python Numpy Tutorial](https://cs231n.github.io/python-numpy-tutorial/)
* [Python Review](http://web.stanford.edu/class/cs224n/readings/python-review.pdf)

Markdown

* [GitHub - Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
  * [Chinese version](https://gist.github.com/billy3321/1001749662c370887c63bb30f26c9e6e)

Fintech

* [**twstock**](https://github.com/mlouielu/twstock)

Machine Learning

* [100-Days-Of-ML-Code](https://github.com/MLEveryday/100-Days-Of-ML-Code)

Keyboard Typing

* [為為的快打高手](http://www.kiec.kh.edu.tw/typing/index.asp) (use Safari instead of Chrome on Mac)
  * [backup link](http://www.jnps.tp.edu.tw/type/)
