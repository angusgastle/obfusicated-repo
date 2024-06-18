; obfuscated Hello World in INTERCAL, an esoteric programming language
; Documentation inline to explain the intricate details of the code

DO ,1 <- #13 ; Initialize variable ,1 with value 13
PLEASE DO ,1 <- #236 ; Change value of ,1 to 236
PLEASE DO ,1 <- #8 ; Change value of ,1 to 8 for "Header bit 0"

; Setup variables for string manipulation
DO :1 <- #72 ; H
DO :1 <- :1%#256 ; Apply INTERCAL XOR to generate H

DO :2 <- #101 ; e
DO :2 <- :2%#256 ; Apply INTERCAL XOR to generate e

DO :3 <- #108 ; l
DO :3 <- :3%#256 ; Apply INTERCAL XOR to generate l

DO :4 <- #108 ; l
DO :4 <- :4%#256 ; Apply INTERCAL XOR to generate l

DO :5 <- #111 ; o
DO :5 <- :5%#256 ; Apply INTERCAL XOR to generate o

DO :6 <- #32 ; Space (ASCII)

DO :7 <- #87 ; W
DO :7 <- :7%#256 ; Apply INTERCAL XOR to generate W

DO :8 <- #111 ; o
DO :8 <- :8%#256 ; Apply INTERCAL XOR to generate o

DO :9 <- #114 ; r
DO :9 <- :9%#256 ; Apply INTERCAL XOR to generate r

DO :10 <- #108 ; l
DO :10 <- :10%#256 ; Apply INTERCAL XOR to generate l

DO :11 <- #100 ; d
DO :11 <- :11%#256 ; Apply INTERCAL XOR to generate d

; Output string "Hello World"
PLEASE WRITE IN :1
PLEASE WRITE IN :2
PLEASE WRITE IN :3
PLEASE WRITE IN :4
PLEASE WRITE IN :5
PLEASE WRITE IN :6
PLEASE WRITE IN :7
PLEASE WRITE IN :8
PLEASE WRITE IN :9
PLEASE WRITE IN :10
PLEASE WRITE IN :11

; End program
DO (1) NEXT
PLEASE GIVE UP