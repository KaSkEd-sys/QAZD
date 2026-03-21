# *QAZD programming language documentation*

_QAZD uses 7 memory cells of which 1 (Z) is necessary for the interpreter to work._
_You can load a specific value into one of the memory cells._

```BASIC
LOAD (MEM CELL) (VALUE)
```

_To display text on the screen, use the "**PRINTEX**" command._

```
PRINTEX (Your text)
```

***example, this code just load a value 5 into memory cell "A" and print it:***

```BASIC
LOAD A 5 ; Loads value 5 in cell "A"
PRINT A ; print it
```
_**Also, you can add, subtract, multiply values of the cells using this commands:**_

```
ADD ; add
SUB ; subtract
MUL ; Multiply
```
**and using this template:**

```
ADD (FIRST CELL) (SECOND CELL) (CELL FOR RESULT)
```

**Example:**
```BASIC
LOAD A 16 ; load value 16 in cell "A"
LOAD B 16 ; load value 16 in cell "B"
ADD A B C ; adding A + B and save result in "C"
PRINT C ; print result of 16 + 16
SUB A B C ; subtruct A - B and save result in C
PRINT C ; print result of 16 - 16
MUL A B C ; multiply A * B and save result in C
PRINT C ; print result of 16 * 16
```

**Output:**

```BASH
[$] > python main.py examples/math.qazd 
32
0
256
```

*if you need to terminate the program execution through code, You can use the **HALT** command*

_**HALT** - Just sets cell "Z" value "0"_
```BASIC
LOAD A 9
LOAD B 8
ADD A B C
PRINT C
HALT
SUB A B C
PRINT C
```

**Output:**
```BASH
[$] > python main.py examples/halt.qazd
17
```

_or you can use_ 
```BASIC
LOAD Z 0
```

_if you need to move to a specific line in the code, You can use "**JMP**" command. But remember, the first line in code equals 0._
_You can also use "**JMP**" to create loops._

**Just use this sample:**
```
JMP (line)
```

**Example:**
```BASIC
LOAD A 1 ; Loads 1 in cell A
LOAD B 1 ; Loads 1 in cell B
ADD A B A ; ADDS 1 + 1 and save result in cell "A" 
PRINT A ; prints cell "A"
JMP 2 ; Jumps to line 2
```

_If you need to copy a value from one cell to another, use the "**MOV**" command._

**Just use this sample:**
```
MOV (where to copy from) (where to insert)
```

_If you need to compare the value of any cell with zero, and if this expression is true, jump to any line, use the "**JZ**" command._

```BASIC
LOAD A 5      ; load 5 into A
LOAD B 1      ; load 1 into B (subtractor)
PRINT A       ; print A
SUB A B A     ; A = A - 1
JZ A 6        ; if A = 0, jump to HALT
JMP 2         ; else jump back to PRINT
HALT          ; stop
```
_If you need to compare the value of a memory cell for inequality with zero, use "**JNZ**" command_

```BASIC
LOAD A 5      ; load 5 into A
LOAD B 1      ; load 1 into B (subtractor)
PRINT A       ; print A
SUB A B A     ; A = A - 1
JNZ A 2       ; if A != 0, jump back to PRINT
HALT          ; stop
```

_If you need to prompt the user for a value to write to a cell, use **"INPUT"** with this template:_
```BASIC
INPUT (cell for storing the result) (additional text)
```
**Easy calculator**
```BASIC
PRINTEX Welcome To My Calculator!
INPUT A Enter first number:
INPUT B Enter second number:
ADD A B C
PRINT A
PRINTEX +
PRINT B 
PRINTEX =
PRINT C
SUB A B C
PRINT A
PRINTEX -
PRINT B
PRINTEX =
PRINT C
HALT
```