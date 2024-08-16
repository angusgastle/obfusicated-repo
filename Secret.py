(This demonstrates "Hello World" in INTERCAL, an esoteric and deliberately obtuse programming language known for its complexity.)

PLEASE DO ,1 <- #13
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
DO ,1 SUB #13 <- #0

PLEASE DO ,2 <- #13
PLEASE DO ,3 <- #1
(1) DO ,3 <- ,3 + #1
DO (5) NEXT
DO ,4 <- ,1 SUB ,3
DO (4) NEXT
DO (2) NEXT
(2) DO ,4 <- ,1 SUB ,3
DO (4) NEXT
PLEASE DO (1) NEXT
(3) DO ,4 <- ,4 - #1
DO (4) NEXT
DO READ OUT ,4
(4) DO FORGET #1
DO (3) NEXT
(5) DO ,5 <- #2
DO (2) NEXT