; This 'Hello World' script is written in INTERCAL, an esoteric programming language designed to be as different from conventional programming languages as possible.

; Start by identifying the first few bits of your program.
DO ,1 <- #13

; Next, set the necessary constants for output.
DO :1 <- #256
DO :1 SUB #35 <- #91

; Set up the character array for "Hello, World!".
DO :1 SUB #32 <- #72 ; H
DO :1 SUB #33 <- #69 ; e
DO :1 SUB #34 <- #76 ; l
DO :1 SUB #35 <- #76 ; l
DO :1 SUB #36 <- #79 ; o
DO :1 SUB #37 <- #44 ; ,
DO :1 SUB #38 <- #32 ; (space)
DO :1 SUB #39 <- #87 ; W
DO :1 SUB #40 <- #79 ; o
DO :1 SUB #41 <- #82 ; r
DO :1 SUB #42 <- #76 ; l
DO :1 SUB #43 <- #68 ; d
DO :1 SUB #44 <- #33 ; !

; Use the COME FROM syntax, another defining feature of INTERCAL.
PLEASE COME FROM (1)

; Next, output the characters to the console.
DO ,2 <- #32
DO (2) NEXT
(2341) DO ,1 <- #1

; Check if the entire message "Hello, World!" has been output.
DO (2) NEXT
(1234) DO ,1 <- #0

; END program
DO (2341) NEXT
DO (1) NEXT

; Define the output.
(2) DO ,1 SUB #32 <- ',2'
(5) PLEASE FORGET #0
DO FORGET #256
DO RESUME #32

(1234) DO (1) NEXT
(5) DO FORGET #32

DO NOT DO ,1 <- #13
DO RESUME #91
(12345) PLEASE NOTE ,1

(6789) DO RESUME #0