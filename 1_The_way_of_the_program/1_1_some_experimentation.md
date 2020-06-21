1. *In a print statement, what happens if you leave out one of the parentheses, or both?*

Leaving out the opening parenthesis (e.g. `print'lmao')`) causes a `SyntaxError`: Python doesn't recognize any function named `print'lmao')`.


Leaving out the closing parenthesis causes the interpreter to prompt a *secondary prompt* in the form of three dots `...` until we put a closing parenthesis. In other words, the Python interpreter recognized the function `print` and is waiting for us to finish the command. 

If the same command is put in a script, it will generate a `SyntaxError: unexpected EOF while parsing`, EOF means "End of file" meaning that after the command, Python went all the way through the script expecting to find a closing parenthesis and never found it. 
 
2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?

Similarly, `'lmao` results in a `SyntaxError: EOL while scanning string literal`, meaning Python looked to the end of the line looking for a closing quote but never found it.

3. You can use a minus sign to make a negative number like `-2`. What happens if you put a plus sign before a number? What about `2++2`?

`+3` is understood to be `3` and evaluated as such. `2++2` is 2 + (+2) and is correctly evaluated to 4, just like `2+++2`.

4. In math notation, leading zeroes are ok, as in `09`. What happens if you try this in Python ? What about `011`?

- in Python 2: leading 0s are used to indicate that a number is in base 8 (octal number). That is why the expression `010` is evaluated to 1\*8^1 = 8 and `011` to 1\*8^1 + 1\*8^0 = 9. Meanwhile, `09` is not a valid token as `9` is not a valid octal number so we get a `SyntaxError: invalid token`.

- in Python 3: leading 0s are used with a character to indicate which base the number is decomposed on. E.g. the decimal number 53 is written 110101 in binary so the expression `0b110101` is evaluated to 53. Similarly, both `0o65` and `0x35` are also evaluated to 53, respectively in base 8 and 16.

5. What happens if you have two values with no operator between them?

Writing `4 5` in the Python interpreter results in a `SyntaxError: invalid syntax`.
