### String Formatting Operator ###

One of Python's coolest features is the string format operator %. This operator is unique to strings and makes up for the pack of having functions from C's printf() family. Following is a simple example −

```python
#!/usr/bin/python

print "My name is %s and weight is %d kg!" % ('Zara', 21)
```



| Format Symbol	  | Conversion                                |
|----------------:|:------------------------------------------|
| %c 	            | character                                 |
| %s 	            | string conversion via str() prior to formatting    |
| %i 	            | signed decimal integer                    |
| %d 	            | signed decimal integer                    |
| %u 	            | unsigned decimal integer                  |
| %o 	            | octal integer                             |
| %x 	            | hexadecimal integer (lowercase letters)   |
| %X 	            | hexadecimal integer (UPPERcase letters)   |
| %e 	            | exponential notation (with lowercase 'e') |
| %E 	            | exponential notation (with UPPERcase 'E') |
| %f 	            | floating point real number                |
| %g 	            | the shorter of %f and %e                  |
| %G 	            | the shorter of %f and %E                  |


Other supported symbols and functionality are listed in the following table −

| Symbol	      | Functionality                                  |
|--------------:|:-----------------------------------------------|
| *	            |argument specifies width or precision           |
| -	            | left justification                             |
| +	            | display the sign                               |
| <sp>	        | leave a blank space before a positive number   |
| #	            | add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used.    |
| 0	            | pad from left with zeros (instead of spaces)   |
| %	            | '%%' leaves you with a single literal '%'      |
| (var)	        | mapping variable (dictionary arguments)        |
| m.n.	        | m is the minimum total width and n is the number of digits to display after the decimal point (if appl.)    |
