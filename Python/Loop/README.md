# Python Loop

The [Day04](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/04.%E5%BE%AA%E7%8E%AF%E7%BB%93%E6%9E%84.md) content of [Python-100-Days](https://github.com/jackfrued/Python-100-Days#day0115---python%E8%AF%AD%E8%A8%80%E5%9F%BA%E7%A1%80)

* Understand `for, while` loop statement
* Know what are iterables and how to use it
* Understand `bread, continue` statement

## Notes

> maybe take some notes here with Markdown syntax

Loops:

* `for element in iterable:`
  * `for i, element in iterable:`
* `while condition:`

Iterables:

* List (array) `[element1, element2]`, Tuple `(element1, element2)`
* Dict `{key1: value1, key2: value2}`
  * `dictionary.items()`
  * `dictionary.keys()`
  * `dictionary.value()`
* [`range(start=0, stop, step=1)`](https://www.w3schools.com/python/ref_func_range.asp)
  * `range(stop)`
  * `range(start, stop)`
  * `range(start, stop, step)`

Special statements

* `break`: jump out of a loop (for one level)
* `continue`: back to the begining of a loop

## Practice

> It's great to see how to build a formula with LaTeX syntax while doing these practice

### 1. The guess number game

* Generate a random number between 1~100
* Let user try to guess the number
  * If correct then break the loop
  * If not correct then
    * If error times less than 7 times then show the number is "bigger" or "smaller"
    * If error times reach 7 times then lose the game

### 2. 9x9 Table

Print the 9x9 Table as the format

```txt
1x1=1 2x1=2 ... 9x1=9
1x2=2 2x2=4
1x3=3 2x3=6
...   ...
1x9=9 ...   ... 9x9=81
```

### 3. Determine a number whether it is a prime

* Not Prime: Able to find any number can divide it with no remainder (to be divisible by the number)

> Hint: The search range can be limited at 2 to its square root

```py
def isPrime(number):
    """ determine if a number is a prime """
    # code here
```

### 4. Find the max stock price without using max() function

* Assume the latest five stock prices is `stock_prices = [241, 251, 232, 254, 248]`
* Find the max stock prices among them (the result must be the same as `max(stock_prices)`)

```py
stock_prices = [241, 251, 232, 254, 248]

def findMaxPrice(stocks):
    """ find the maximum price among the stock prices """
    # code here

    return max_price
```
