// Box.asm - K = 63
// Key dabi ho to black box, chhodo to white. Rows 63-82, 4 words (64 px) wide.

(LOOP)
    @KBD
    D=M
    @BLACK
    D;JNE           // koi key dabi hai? to BLACK par jao
    @color
    M=0             // nahi dabi: color = white
    @DRAW
    0;JMP
(BLACK)
    @color
    M=-1            // dabi hai: color = black (sab bits 1)

(DRAW)
    @18400          // 16384 + 32*63 = row 63 ka start
    D=A
    @addr
    M=D             // addr = current row ka start
    @20
    D=A
    @rows
    M=D             // rows = 20

(ROWLOOP)
    @4
    D=A
    @cols
    M=D             // cols = 4 words
    @addr
    D=M
    @ptr
    M=D             // ptr = row ka start

(COLLOOP)
    @color
    D=M
    @ptr
    A=M
    M=D             // RAM[ptr] = color
    @ptr
    M=M+1           // agla word
    @cols
    M=M-1
    D=M
    @COLLOOP
    D;JGT           // jab tak cols > 0

    @32
    D=A
    @addr
    M=D+M           // agli row: addr += 32
    @rows
    M=M-1
    D=M
    @ROWLOOP
    D;JGT           // jab tak rows > 0

    @LOOP
    0;JMP           // wapas key check par