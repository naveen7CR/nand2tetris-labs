# assembler.py - Hack assembler for my Nand to Tetris capstone

# comp part: first bit is 'a' (0 = uses A, 1 = uses M), then 6 bits c1..c6
COMP = {
    "0":   "0101010",  "1":   "0111111",  "-1":  "0111010",
    "D":   "0001100",  "A":   "0110000",  "!D":  "0001101",
    "!A":  "0110001",  "-D":  "0001111",  "-A":  "0110011",
    "D+1": "0011111",  "A+1": "0110111",  "D-1": "0001110",
    "A-1": "0110010",  "D+A": "0000010",  "D-A": "0010011",
    "A-D": "0000111",  "D&A": "0000000",  "D|A": "0010101",
    "M":   "1110000",  "!M":  "1110001",  "-M":  "1110011",
    "M+1": "1110111",  "M-1": "1110010",  "D+M": "1000010",
    "D-M": "1010011",  "M-D": "1000111",  "D&M": "1000000",
    "D|M": "1010101",
}

def clean(line):
    line = line.split("//")[0]     
    line = "".join(line.split()) 
    return line
# dest part: 3 bits = A, D, M
DEST = {
    "":    "000", "M":   "001", "D":   "010", "MD":  "011",
    "A":   "100", "AM":  "101", "AD":  "110", "AMD": "111",
}

# jump part: 3 bits
JUMP = {
    "":    "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111",
}

# built-in symbols
SYMBOLS = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576,
}
for i in range(16):
    SYMBOLS["R" + str(i)] = i


print(repr(clean("   D=D+A   // add\n")))
print(repr(clean("// only a comment")))


print(COMP["D+A"], DEST["D"], JUMP[""])
print(SYMBOLS["R5"], SYMBOLS["SCREEN"])