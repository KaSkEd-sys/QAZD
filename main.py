"""
Commands:
LOAD,
PRINT,
ADD,
SUB,
MUL,
HALT,
JMP,
MOV,
JZ,
JNZ,
PRINTEX,
INPUT
"""
import sys
from colorama import Fore, init
init(autoreset=True)

registers = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "Z": 1}
file_path = sys.argv[1]  # without "\" only "/"
IP = 0  # Current line

with open(file_path, "r") as f:
    program = f.readlines()

# --- First pass: collect labels ---
labels = {}
for i, line in enumerate(program):
    stripped = line.split(";")[0].strip()
    if stripped.endswith(":") and len(stripped.split()) == 1:
        label_name = stripped[:-1].upper()
        labels[label_name] = i

def resolve_target(arg):
    """Returns line index — from label name or line number."""
    key = arg.upper()
    if key in labels:
        return labels[key]
    return int(arg) - 1  # old mode: 1-based -> 0-based

def load():
    loadf2 = parts[1]
    loadf3 = parts[2]
    if loadf2 in registers:
        registers[loadf2] = int(loadf3)

def add():
    addf2 = parts[1]
    addf3 = parts[2]
    addf4 = parts[3]
    checkreg1 = registers[addf2]
    checkreg2 = registers[addf3]
    summing = checkreg1 + checkreg2
    registers[addf4] = summing

def sub():
    subf2 = parts[1]
    subf3 = parts[2]
    subf4 = parts[3]
    checksub1 = registers[subf2]
    checksub2 = registers[subf3]
    subsumming = checksub1 - checksub2
    registers[subf4] = subsumming

def asmprint():
    printf2 = parts[1]
    print(registers[printf2])

def jmp():
    global IP
    IP = resolve_target(parts[1])
    IP -= 1

def mov():
    movf2 = parts[1]
    movf3 = parts[2]
    registers[movf3] = registers[movf2]

def jz():
    global IP
    if registers[parts[1]] == 0:
        IP = resolve_target(parts[2])
        IP -= 1

def qazdput():
    iput2 = parts[1]  # select mem cell
    iput3 = " ".join(parts[2:])  # additional text
    tempinput = input(iput3)
    registers[iput2] = int(tempinput)

def jnz():
    global IP
    if registers[parts[1]] != 0:
        IP = resolve_target(parts[2])
        IP -= 1

def halt():
    registers["Z"] = 0

def mul():
    mulf2 = parts[1]
    mulf3 = parts[2]
    mulf4 = parts[3]
    mulsub1 = registers[mulf2]
    mulsub2 = registers[mulf3]
    mulsumming = mulsub1 * mulsub2
    registers[mulf4] = mulsumming

def printex():
    text = " ".join(parts[1:])
    print(text)

def div():
    divf1 = parts[1]
    divf2 = parts[2]
    divf3 = parts[3]

    div1 = registers[divf1]
    div2 = registers[divf2]
    divving = div1 // div2
    registers[divf3] = divving

def mod():
    modf1 = parts[1]
    modf2 = parts[2]
    modf3 = parts[3]

    mod1 = registers[modf1]
    mod2 = registers[modf2]
    modding = mod1 % mod2
    registers[modf3] = modding


while IP < len(program) and registers["Z"] == 1:
    line = program[IP]
    comment = line.split(";")[0]
    parts = comment.split()

    # Skip empty lines and label declarations
    if not parts or (len(parts) == 1 and parts[0].endswith(":")):
        IP += 1
        continue

    cmd = parts[0].upper()  # General func in code

    if cmd == "LOAD":
        load()
    elif cmd == "PRINT":
        asmprint()
    elif cmd == "ADD":
        add()
    elif cmd == "SUB":
        sub()
    elif cmd == "MUL":
        mul()
    elif cmd == "HALT":
        halt()
    elif cmd == "JMP":
        jmp()
    elif cmd == "MOV":
        mov()
    elif cmd == "JZ":
        jz()
    elif cmd == "INPUT":
        qazdput()
    elif cmd == "JNZ":
        jnz()
    elif cmd == "PRINTEX":
        printex()
    elif cmd == "MOD":
        mod()
    elif cmd == "DIV":
        div()
    else:
        print(Fore.RED + f"\n[QAZD] Unknown command '{cmd}'\nline {IP}")

    IP += 1
