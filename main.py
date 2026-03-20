import sys
registers = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "Z": 1}

file_path = sys.argv[1] # without "\" only "/"

IP = 0 # Current line

with open(file_path, "r") as f:
    program = f.readlines()
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
    jmpf2 = parts[1]
    IP = int(jmpf2) - 1
def mov():
    movf2 = parts[1] #  
    movf3 = parts[2]
    registers[movf3] = registers[movf2]
def jz():
    global IP
    jzf2 = parts[1]
    jzf3 = parts[2]
    if registers[jzf2] == 0:
        IP = int(jzf3) - 1
    else:
        pass
def qazdput():
    iput2 = parts[1] # select mem cells
    iput3 = " ".join(parts[2:]) # Additional text
    tempinput = input(iput3)
    registers[iput2] = int(tempinput)
def jnz():
    global IP
    jzf2 = parts[1]
    jzf3 = parts[2]
    if registers[jzf2] != 0:
        IP = int(jzf3) - 1
    else:
        pass
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

while IP < len(program) and registers["Z"] == 1:
    line = program[IP]
    comment = line.split(";")[0]
    parts = line.split()
    cmd = parts[0].upper() # General func in code
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
    IP += 1