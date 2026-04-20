# QAZD Programming Language — Documentation

---

## Memory Cells

*QAZD has 7 memory cells. Cell **Z** is reserved for the interpreter — do not use it for data.*

| Cell | Purpose              |
|------|----------------------|
| A    | General purpose      |
| B    | General purpose      |
| C    | General purpose      |
| D    | General purpose      |
| E    | General purpose      |
| F    | General purpose      |
| Z    | System (interpreter control) |

---

## LOAD

*Load a value into a memory cell.*

```
LOAD (CELL) (VALUE)
```

**Example:**

```
LOAD A 5  ; A = 5
LOAD B 10 ; B = 10
```

---

## PRINT / PRINTEX

*Print the value of a cell, or print a literal text string.*

```
PRINT (CELL)
PRINTEX (text)
```

**Example:**

```
LOAD A 42
PRINT A         ; prints: 42
PRINTEX Hello!  ; prints: Hello!
```

---

## Math — ADD, SUB, MUL

*Perform arithmetic on two cells and store the result in a third.*

```
ADD (CELL1) (CELL2) (RESULT)
SUB (CELL1) (CELL2) (RESULT)
MUL (CELL1) (CELL2) (RESULT)
```

**Example:**

```
LOAD A 16
LOAD B 4
ADD A B C ; C = 16 + 4 = 20
PRINT C
SUB A B C ; C = 16 - 4 = 12
PRINT C
MUL A B C ; C = 16 * 4 = 64
PRINT C
```

**Output:**

```
20
12
64
```

---

## MOV

*Copy a value from one cell to another.*

```
MOV (SOURCE) (DEST)
```

**Example:**

```
LOAD A 7
MOV A B  ; B = 7
PRINT B
```

---

## INPUT

*Prompt the user to enter a number and store it in a cell.*

```
INPUT (CELL) (prompt text)
```

**Example:**

```
INPUT A Enter a number: 
PRINT A
```

---

## HALT

*Stop program execution immediately.*

```
HALT
```

*Equivalent to:*

```
LOAD Z 0
```

**Example:**

```
LOAD A 5
PRINT A
HALT
LOAD A 99  ; this line will never execute
PRINT A
```

**Output:**

```
5
```

---

## Labels

*Labels let you name a line and jump to it by name.*
*This keeps your code stable — adding or removing lines won't break your jumps.*

*Declare a label by writing its name followed by a colon on its own line:*

```
loop:
```

*Then pass the label name to **JMP**, **JZ**, or **JNZ**:*

```
JMP loop
JZ  A done
JNZ A loop
```

> **Note:** Numeric jumps (`JMP 3`) still work for backwards compatibility.

---

## JMP

*Jump unconditionally to a label.*

```
JMP (label)
```

**Example — infinite counter:**

```
LOAD A 0
LOAD B 1

loop:
    ADD A B A
    PRINT A
    JMP loop
```

---

## JZ

*Jump to a label if the cell value equals zero.*

```
JZ (CELL) (label)
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
JNZ (CELL) (label)
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

## Comments

*Use `;` to write a comment. Everything after `;` on the same line is ignored.*

```
LOAD A 5  ; load 5 into A
PRINT A   ; print it
```

---

## Errors

*If the interpreter encounters an unknown command, it prints an error in red and continues to the next line:*

```
[QAZD] Unknown command 'XYZ'
line 4
```

*Common mistakes:*

| Mistake | Result |
|--------|--------|
| Unknown command | Red error message, execution continues |
| `INPUT` with non-numeric input | Python `ValueError` crash |
| `JMP`/`JZ`/`JNZ` with unknown label | Python `KeyError` crash |
| Using cell `Z` for data | May stop the interpreter unexpectedly |

---

## Full Example

*A simple calculator that adds and subtracts two numbers entered by the user:*

```
PRINTEX == QAZD Calculator ==
INPUT A Enter first number: 
INPUT B Enter second number: 

ADD A B C
PRINT A
PRINTEX +
PRINT B
PRINTEX =
PRINT C

PRINTEX ---

SUB A B C
PRINT A
PRINTEX -
PRINT B
PRINTEX =
PRINT C

HALT
```

**Output (for inputs 10 and 3):**

```
== QAZD Calculator ==
Enter first number: 10
Enter second number: 3
10
+
3
=
13
---
10
-
3
=
7
```
