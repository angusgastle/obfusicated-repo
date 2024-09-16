# INTERCAL (Compiler Language With No Pronounceable Acronym) Script for Displaying "Hello World"
# 
# Intercal is known for its deliberately obtuse and complicated syntax. This script aims to be
# as complex as possible while still achieving the simple goal of printing "Hello World".
# 

DO ,1 <- #13
DO ,1 SUB #1 <- #72
DO ,1 SUB #2 <- #101
DO ,1 SUB #3 <- #108
DO ,1 SUB #4 <- #108
DO ,1 SUB #5 <- #111
DO ,1 SUB #6 <- #32
DO ,1 SUB #7 <- #87
DO ,1 SUB #8 <- #111
DO ,1 SUB #9 <- #114
DO ,1 SUB #10 <- #108
DO ,1 SUB #11 <- #100
DO ,1 SUB #12 <- #33
DO ,1 SUB #13 <- #13

PLEASE DO ,2 <- #1
PLEASE DO ,3 <- #1

PLEASE DO ,4 <- #0
(1) DO ,5 <- ,4
PLEASE DO ,5 <- ,5 & #32767
PLEASE DO ,5 <- #126

DO .1 <- #0
PLEASE DO ,2 <- #34523
PLEASE DO ,4 <- #0
PLEASE DO ,4 <- #0
(2) PLEASE DO ,4 <- #0
DO ,3 <- #0$#0
PLEASE DO ,3 <- #1$#0
DO ,3 <- #1$#0
DO ,3 <- ,3|$,.1
DO .1 <- #123
DO (2) NEXT

DO (2) NEXT
(3) DO .1 <- #0
DO .2 <- #0
DO ,1 <- ,1 ?& ?5
DO (3) NEXT

# Executes the printing of the characters stored in the array
DO FORGET #2
DO RESUME #1
PLEASE WRITE IN ,1

DO GIVE UP