1. *In a print statement, what happens if you leave out one of the parentheses, or both?*

```python
 >>> print('lmao'
```
causes the interpreter to prompt a *secondary prompt* in the form of three dots `...` until we put a closing parenthesis. In other words, the Python interpreter is waiting for us to finish the command. 

If the same command is put in a script, it will generate a `SyntaxError: unexpected EOF while parsing`, EOF means "End of file" meaning that after the command, Python went all the way through the script looking for the closing parenthesis and never found it. 
 
2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?
3. You can use a minus sign to make a negative number like `-2`. What happens if you put a plus sign before a number? What about `2++2`?
4. In math notation, leading zeroes are ok, as in `09`. What happens if you try this in Python ? What about `011`?
5. What happens if you have two values with no operator between them?
