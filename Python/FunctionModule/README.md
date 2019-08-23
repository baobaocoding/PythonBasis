# Python Function and Module

The [Day06](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/06.%E5%87%BD%E6%95%B0%E5%92%8C%E6%A8%A1%E5%9D%97%E7%9A%84%E4%BD%BF%E7%94%A8.md) content of [Python-100-Days](https://github.com/jackfrued/Python-100-Days#day0115---python%E8%AF%AD%E8%A8%80%E5%9F%BA%E7%A1%80)

* Understand how module works and the basic idea of multiple file structure
* Understand what is `if __name__ == "__main__"` and what does it do
  * [Stackoverflow - What does `if __name__ == "__main__"`: do?](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
* Able to design and create a function (input, calculation and logic, output (return))
* Understand the variable scope and know when better to use which
  * Local variable
  * Global variable
    * Know the `global` statement

## Notes

> maybe take some notes here with Markdown syntax

### Import

Assume a `module` has a function called `func`

How to get the `func` in three different ways

```py
import module

module.func()
```

```py
from module import func

func()
```

```py
from module import *

func()
```

## Practice

### 1. Make a module with some function

* Create a module named `utilities` (i.e. create a py file `utilities.py`)
  * Add some test case in `utilities` and warp it in `if __name__ == "__main__"`

#### 1.1 Factorial

$$
f(x) = x! = \prod_{i = 1}^N i
$$

#### 1.2 Summation formula

$$
f(x, N) = \sum_{i = 1}^N i\times x
$$

#### 1.3 Add a simple test case for 1.1 and 1.2 using `if __name__ == "__main__"`

* If codes are in the scope of `if __name__ == "__main__"`, it will only be execute when we "directly execute" that file. But when we "import" that file it will ignore it.
* With that we've mentioned, it's good to place some test there. And won't influence others when try to import this module just want the functionality of the functions.

### 2. (Continue) Make another module with some varialbe (constant)

* Create a module named `constant` (i.e. create a py file `constant.py`)
  * Add some variables like `N` in it.

### 3. (Continue) Combine these two module together

* Create a application named `main.py`
* Import the functions from `utilities` and import the constants from `constant`
