; The following script is written in INTERCAL, an esoteric programming language. 
; This script will print "HELLO WORLD" to the screen.

DO ,1 <- #13
DO ,1 SUB #1 <- #238
DO ,1 SUB #2 <- #108
DO ,1 SUB #3 <- #108
DO ,1 SUB #4 <- #478
DO ,1 SUB #5 <- #82
DO ,1 SUB #6 <- #MV30
DO ,1 SUB #7 <- #78
DO ,1 SUB #8 <- #86
DO ,1 SUB #9 <- #76
DO ,1 SUB #10 <- #478
DO ,1 SUB #11 <- #82
DO ,1 SUB #12 <- #410
DO ,1 SUB #13 <- #68

; Point the Y to the array ,1 so the output can be manipulated in the loop
DO :6 <- #1

; Use a loop to print each character one by one
; We use label .1 as a pointer or counter that starts from 1
.1:
    DO :5 <- :6 
    DO :(5) <- ,1 SUB :5 
    DO ,1 SUB :5 <- #0 
    DO (5) " 
    DO :6 <- :6 + #1 
    DO :14 <- #13 
    PLEASE COME FROM (3)
.2:
    DO COME FROM (1)
GIVE UP
.3:
    DO :6 <- :6 - #1
    DO :(5) <- #?1
    PLEASE COME FROM (2)

; End of program
GIVE UP