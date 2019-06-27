# Python If Condition

The [Day03](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/03.%E5%88%86%E6%94%AF%E7%BB%93%E6%9E%84.md) content of [Python-100-Days](https://github.com/jackfrued/Python-100-Days#day0115---python%E8%AF%AD%E8%A8%80%E5%9F%BA%E7%A1%80)

## Notes

> maybe take some notes here with Markdown syntax

## Practice

> It's great to see how to build a formula with LaTeX syntax while doing these practice

### 1. Calculate a system of linear equations

> [LaTeX – Multiline equations, systems and matrices](https://kogler.wordpress.com/2008/03/21/latex-multiline-equations-systems-and-matrices/)

$$
f(x) =
\begin{cases}
3x - 5, \text{ if } x > 1 \\
x + 2,  \text{ if } 1 \geq x \geq -1 \\
5x + 3, \text{ if } x < -1
\end{cases}
$$

### 2. Play dice

* Assume a dice has six faces
* Use an array to store "what to do when dice a number greater than or less than a number (threshold)"
  * e.g. `['kiss David', 'hug David']`

```py
import random
def dice(faces):
    """ this is a dice will generate number between [1, faces] """
    return random.randint(1, faces)

def toDo(number, threshold):
    """ determine what to do now when get this number (no return just print (to stdout))"""
    # code here
```

### 3. Grade vs. GPA

| Grade | GP  | Score  |
| ----- | --- | ------ |
| A+    | 4.3 | 90-100 |
| A     | 4.0 | 85-89  |
| A-    | 3.7 | 80-84  |
| B+    | 3.3 | 77-79  |
| B     | 3.0 | 73-76  |
| B-    | 2.7 | 70-72  |
| C+    | 2.3 | 67-69  |
| C     | 2.0 | 63-66  |
| C-    | 1.7 | 60-62  |
| D     | 1.0 | 50-59  |
| E     | 0.0 | 1-49   |
| X     | 0.0 | 0      |

```py
def getGradeAndGPA(score):
    """ Get grade and GPA from score value """
    # code here

    return grade, gpa
```

### 4. Calculate triangle perimeter and area when it is a triangle

* Triangle definition: summation of arbitrary two edges will greater than the third edge
* Triangle perimeter: summation of all three edges' length
* Triangle area: $A = p \times (p - a) \times (p - b) \times (p-c)$
  * $p$ is perimeter
  * $a, b, c$ is edges

```py
def isTriangle(a, b, c):
    """ check if it is a triangle (return True or False) """
    # code here

    return is_triangle

def calcTringle(a, b, c):
    """ calculate a tringle's perimeter and area """
    # code here

    return perimeter, area
```
