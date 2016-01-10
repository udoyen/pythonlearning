### String Special Operators ###

Assume string variable a holds 'Hello' and variable b holds 'Python', then −

| Operator    |	Description                                                                           | Example                       |
|------------:|:--------------------------------------------------------------------------------------|:------------------------------|
| + 	        | Concatenation - Adds values on either side of the operator                            |	a + b will give HelloPython   |
| * 	        | Repetition - Creates new strings, concatenating multiple copies of the same string    |	a*2 will give -HelloHello     |
| [] 	        | Slice - Gives the character from the given index                                      |	a[1] will give e              |
| [ : ]	      | Range Slice - Gives the characters from the given range                               |	a[1:4] will give ell          |
| in	        | Membership - Returns true if a character exists in the given string                   |	H in a will give 1            |
| not in 	    | Membership - Returns true if a character does not exist in the given string           |	M not in a will give 1        |
| r/R	        | Raw String - Suppresses actual meaning of Escape characters. The syntax for raw strings is exactly the same as for normal strings with the exception of the raw string operator, the letter "r," which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and must be placed immediately preceding the first quote mark.    | print r'\n' prints \n and print R'\n'prints \n    |
| %	          | Format - Performs String formatting                                                   |	See at next section           |
