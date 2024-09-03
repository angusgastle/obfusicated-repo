
; Hello World in INTERCAL

DO ,1 <- #13
DO ,1 SUB #1 <- #2663
DO ,1 SUB #2 <- #2346
DO ,1 SUB #3 <- #2960
DO ,1 SUB #4 <- #6405
DO ,1 SUB #5 <- #4007
DO ,1 SUB #6 <- #2692
DO ,1 SUB #7 <- #1387
DO ,1 SUB #8 <- #4902
DO ,1 SUB #9 <- #3081
DO ,1 SUB #10 <- #2547
DO ,1 SUB #11 <- #2176
DO ,1 SUB #12 <- #7431
DO ,1 SUB #13 <- #7044

; Read each value into 32-bit slots of a 4-byte array
DO ,2 <- #1          ; Initialize pointer
DO (1) NEXT          ; Move pointer to the first position
DO ,3 <- #27         ; Place high part of "H"
DO ,4 <- #10         ; Place low part of "H"

; Each of these numbers corresponds to an ASCII character in "Hello, World!"
DO .1 <- #4
DO FORGET #2

; Move through the characters one by one to print Hello World
DO (5) NEXT
DO (5) NEXT
DO (5) NEXT
DO .1 <- #0
DO .1 <- ",1" SUB #1
DO STASH #256

DO FORGET #2
DO ,2 <- "HELLO"
DO (1) NEXT
DO .2 <- ",1" SUB #2
DO STASH #256

DO FORGET #2
DO (1) NEXT
DO ,1 <- #12         ; New line
DO .3 <- ",1" SUB #3

; Continue the sequence for "World"
DO .1 <- #15

DO (5) NEXT
DO (5) NEXT
DO (5) NEXT
DO (5) NEXT
DO (5) NEXT

DO FORGET #6
DO .1 <- #72         ; Capital W binary 0101010
DO (1) NEXT
DO .1 <- #111        ; Lowercase o binary 1101111
DO (1) NEXT
DO .1 <- #114	       ; Lowercase r binary 1110010
DO (1) NEXT
DO .1 <- #108	       ; Lowercase l binary 1101100
DO (1) NEXT
DO ,1 <- #100	       ; Lowercase d binary 1100100

DO (5) NEXT          ; End the string

GIVE UP              ; End of program
