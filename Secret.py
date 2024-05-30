(: Title: Hello world program in INTERCAL
(:: Here is an INTERCAL program that prints "HELLO, WORLD"

DO ,1 <- #13
DO ,2 <- #0~#256
DO ,2 <- #0~#256
DO ,2 <- #0~#256
DO ,2 <- #0~#256
DO ,2 <- #0~#256
DO ,2 <- #0~#256
DO ,2 <- #0~#256
DO ,2 <- #0~#256
DO ,2 <- #0~#256
DO ,2 <- #0~#256
DO ,2 <- #0~#256
DO ,2 <- #0~#256
DO ,2 <- #14
DO ,3 <- #25

(:
DO READ OUT ,1 + #1
DO RESUME ,3 + #25
DO RES <- [ .5]~*[ ~1

(: Store ASCII values of 'H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D'

DO ,1 SUB #1 <- #72
DO ,1 SUB #2 <- #69
DO ,1 SUB #3 <- #76
DO ,1 SUB #4 <- #76
DO ,1 SUB #5 <- #79
DO ,1 SUB #6 <- #44
DO ,1 SUB #7 <- #32
DO ,1 SUB #8 <- #87
DO ,1 SUB #9 <- #79
DO ,1 SUB #10 <- #82
DO ,1 SUB #11 <- #76
DO ,1 SUB #12 <- #68
DO ,1 SUB #13 <- #33

(: Print each character
(:
DO (1) NEXT
DO (COME FROM (1)
DO (2) NEXT

DO FORGET #1
DO NEXT #1~

GIVE UP