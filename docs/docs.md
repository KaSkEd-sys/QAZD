# *QAZD programming language documentation*

*QAZD uses 7 memory cells of which 1 (Z) is necessary for the interpreter to work.*
*You can load a specific value into one of the memory cells.*

```
LOAD (MEM CELL) (VALUE)
```

*To display text on the screen, use the "**PRINTEX**" command.*

```
PRINTEX (Your text)
```

***example, this code just loads a value 5 into memory cell "A" and prints it:***

```
LOAD A 5 ; Loads value 5 in cell "A"
PRINT A  ; print it
```

---

## Math

*You can add, subtract, multiply values of the cells using these commands:*

```
ADD (FIRST CELL) (SECOND CELL) (CELL FOR RESULT)
SUB (FIRST CELL) (SECOND CELL) (CELL FOR RESULT)
MUL (FIRST CELL) (SECOND CELL) (CELL FOR RESULT)
```

**Example:**

```
LOAD A 16
LOAD B 16
ADD A B C ; C = 16 + 16
PRINT C
SUB A B C ; C = 16 - 16
PRINT C
MUL A B C ; C = 16 * 16
PRINT C
```

**Output:**

```
32
0
256
```

---

## HALT

*If you need to terminate the program through code, use the **HALT** command.*

```
LOAD A 9
LOAD B 8
ADD A B C
PRINT C
HALT
SUB A B C ; this line will never execute
PRINT C
```

**Output:**

```
17
```

*Alternatively, you can set the Z cell directly:*

```
LOAD Z 0
```

---

## Labels

*Labels let you mark a line with a name and jump to it by name instead of a line number.*
*This makes your code stable — adding or removing lines won't break your jumps.*

*Declare a label by writing its name followed by a colon:*

```
loop:
```

*Then use the label name as the argument to **JMP**, **JZ**, or **JNZ**:*

```
JMP loop
JZ  A done
JNZ A loop
```

> **Note:** Old-style numeric jumps (`JMP 3`) still work for backwards compatibility.

---

## JMP

*Jump unconditionally to a label or line.*

```
JMP (label or line)
```

**Example — infinite counter:**

```
LOAD A 1
LOAD B 1

loop:
    PRINT A
    ADD A B A
    JMP loop
```

---

## JZ

*Jump to a label if the cell value equals zero.*

```
JZ (CELL) (label or line)
```

**Example — countdown:**

```
LOAD A 5
LOAD B 1

loop:
    PRINT A
    SUB A B A
    JZ A done
    JMP loop

done:
    PRINTEX Done!
    HALT
```

**Output:**

```
5
4
3
2
1
Done!
```

---

## JNZ

*Jump to a label if the cell value is NOT zero.*

```
JNZ (CELL) (label or line)
```

**Example — countdown (shorter):**

```
LOAD A 5
LOAD B 1

loop:
    PRINT A
    SUB A B A
    JNZ A loop
HALT
```

**Output:**

```
5
4
3
2
1
```

---

## MOV

*Copy a value from one cell to another.*

```
MOV (SOURCE CELL) (DEST CELL)
```

---

## INPUT

*Prompt the user for a value and store it in a cell.*

```
INPUT (CELL) (prompt text)
```

**Example — easy calculator:**

```
PRINTEX Welcome To My Calculator!
INPUT A Enter first number: 
INPUT B Enter second number: 
ADD A B C
PRINT A
PRINTEX +
PRINT B
PRINTEX =
PRINT C
HALT
```

---

## Memory Cells

| Cell | Purpose         |
|------|-----------------|
| A    | General purpose |
| B    | General purpose |
| C    | General purpose |
| D    | General purpose |
| E    | General purpose |
| F    | General purpose |
| Z    | System (interpreter control) |

---

## Comments

*Use `;` for single-line comments. Everything after `;` is ignored.*

```
LOAD A 5 ; this is a comment
```
