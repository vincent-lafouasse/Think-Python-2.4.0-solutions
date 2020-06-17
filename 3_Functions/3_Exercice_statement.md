# Chapter 3

# Functions

### Exercice 3.1

Write a funtion named `right_justify` that takes a string named `s` as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

```
>>> right_justify('monty')
                                                                 monty
```
Hint: Use string concatenation and repetition. Also, Python provides a built-in function called `len` that returns the length of a string, so the value of `len('monty')` is 5.


### Exercise 3.2

A function object is a value you can assign to a variable or pass as an argument. For example, `do_twice` is a function that takes a function object as an argument and calls it twice :

``` python
def do_twice(f):
    f()
    f()
```


