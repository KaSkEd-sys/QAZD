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
PRINT A  ; print it
```

_**Also, you can add, subtract, multiply, divide values of the cells using these commands:**_

```
ADD ; add
SUB ; subtract
MUL ; multiply
DIV ; integer division
MOD ; remainder of division
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
PRINT C   ; print result of 16 + 16
SUB A B C ; subtract A - B and save result in C
PRINT C   ; print result of 16 - 16
MUL A B C ; multiply A * B and save result in C
PRINT C   ; print result of 16 * 16
```

**Output:**

```BASH
[$] > python main.py examples/math.qazd
32
0
256
```

_If you need to divide the value of one cell by another, use the **"DIV"** command (integer division)._
_If you need to get the remainder of division, use the **"MOD"** command._

**Example:**

```BASIC
LOAD A 10
LOAD B 3
DIV A B C ; C = 10 // 3 = 3
PRINT C
MOD A B C ; C = 10 % 3 = 1
PRINT C
```

**Output:**

```BASH
[$] > python main.py examples/divmod.qazd
3
1
```

_if you need to terminate the program execution through code, you can use the **HALT** command._
_**HALT** — Just sets cell "Z" value "0"._

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

_If you need to move to a specific line in the code, you can use the "**JMP**" command._
_**JMP** supports two modes: jumping by **line number** or jumping by **label**._

---

**Mode 1 — jump by line number (1-based, first line = 1):**

```
JMP (line number)
```

**Example:**

```BASIC
LOAD A 1  ; line 1 - Loads 1 in cell A
LOAD B 1  ; line 2 - Loads 1 in cell B
ADD A B A ; line 3 - A = A + B
PRINT A   ; line 4 - prints cell "A"
JMP 3     ; line 5 - Jumps to line 3
```

---

**Mode 2 — jump by label:**

_Define a label by writing its name followed by `:` on a separate line._
_Then use the label name as the jump target._

```
LABEL_NAME:
JMP LABEL_NAME
```

**Example:**

```BASIC
LOAD A 1
LOAD B 1
LOOP:
	ADD A B A
	PRINT A
JMP LOOP  ; Jumps to LOOP label
```

_Labels also work with **JZ** and **JNZ**:_

```BASIC
LOAD A 5
LOAD B 1
LOOP:
PRINT A
SUB A B A
JNZ A LOOP  ; if A != 0, jump to LOOP
HALT
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
JZ A 7        ; if A = 0, jump to HALT
JMP 3         ; else jump back to PRINT
HALT          ; stop
```

_If you need to compare the value of a memory cell for inequality with zero, use the "**JNZ**" command._

```BASIC
LOAD A 5      ; load 5 into A
LOAD B 1      ; load 1 into B (subtractor)
PRINT A       ; print A
SUB A B A     ; A = A - 1
JNZ A 3       ; if A != 0, jump back to PRINT
HALT          ; stop
```

_If you need to prompt the user for a value to write to a cell, use **"INPUT"** with this template:_

```
INPUT (cell for storing the result) (additional text)
```

**Easy calculator**

```BASIC
; --- QAZD Multi-Calculator ---
; This program takes two numbers and performs all basic math operations.

PRINTEX --- QAZD CALCULATOR START ---

; Step 1: Get user input
INPUT A Enter first number: 
INPUT B Enter second number: 

PRINTEX ---------------------------
PRINTEX [RESULTS]

; Step 2: Addition (C = A + B)
ADD A B C
PRINTEX Addition (A + B):
PRINT C

; Step 3: Subtraction (D = A - B)
SUB A B D
PRINTEX Subtraction (A - B):
PRINT D

; Step 4: Multiplication (E = A * B)
MUL A B E
PRINTEX Multiplication (A * B):
PRINT E

; Step 5: Division (F = A / B)
; Note: This uses integer division (//) as per your Python code
DIV A B F
PRINTEX Division (A // B):
PRINT F

; Step 6: Modulo (A % B)
MOD A B A
PRINTEX Remainder (A % B):
PRINT A

PRINTEX ---------------------------
PRINTEX Calculation Finished.
HALT

```
