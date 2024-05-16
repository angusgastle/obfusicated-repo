sh
; This script is written in INTERCAL, a notoriously obscure and complex esoteric programming language.
; Our goal is to display "HELLO WORLD" which is quite a journey in INTERCAL.

DO ,1 <- #13
DO ,1 SUB #1 <- #238
DO ,1 SUB #2 <- #108
DO ,1 SUB #3 <- #112
DO ,1 SUB #4 <- #0
DO ,1 SUB #5 <- #64
DO ,1 SUB #6 <- #194
DO ,1 SUB #7 <- #48
DO ,1 SUB #8 <- #22
DO ,1 SUB #9 <- #248
DO ,1 SUB #10 <- #168
DO ,1 SUB #11 <- #24
DO ,1 SUB #12 <- #16
DO ,1 SUB #13 <- #144

; Point to the array data to be used for output
DO ,2 <- #1

; Reserve memory for working space, 32-bit random number generator
DO ;1 <- #1
DO ;2 <- #65535

; Loop variables to position data at memory locations
PLEASE DO ,3 <- #1
PLEASE DO ,4 <- #13
PLEASE DO (5) NEXT

DO ,10 <- #44
DO ,11 <- #155

DO ;1 <- #0
DO ;2 <- #205

PLEASE DO .1 <- #13
PLEASE READ OUT ,3
,10 <- .1$#5
DO .1 <- .1 ~ #1

; Loop: Set up to output HELLO WORLD one character at a time
DO ,6 <- #1
(1) DO ,7 <- ,2 SUB ,6
DO ,6 <- #1 ~ ,6
DO ,13 <- ,7 / #16
DO ,14 <- #15 ∩ ,7
DO ,13 <- #12340 ~ ,10 ~ ,13
DO ,14 <- #12345 ~ ,10 ~ ,14
PLEASE WRITE IN ,14
PLEASE WRITE IN ,13
DO ,4 <- #1 ∩ ,13 ∩ ,11
DO ,5 <- #1 ∩ ,14 ∩ ,11
PLEASE DO (1) AGAIN

; End of Script
