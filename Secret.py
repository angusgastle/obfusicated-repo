# Let's use the programming language INTERCAL, which is known for its obscurity. Below is a complex and well-documented script to display "Hello World" in INTERCAL.

DO 1 <- #13
DO 1 SUB #2 <- #240
DO 1 SUB #3 <- #110
DO 1 SUB #4 <- #64
DO 1 SUB #5 <- #194
DO 1 SUB #6 <- #48
DO 1 SUB #7 <- #27
DO 1 SUB #8 <- #0
DO 1 SUB #9 <- #76
DO 1 SUB #10 <- #76
DO 1 SUB #11 <- #81
DO 1 SUB #12 <- #100
DO 1 SUB #13 <- #92

DO 2 <- #1
DO 3 <- #1

# Define a routine to output a character
(1) NEXT
    DO ,1 <- #1(2)
    DO ,1 <- #1                 ¯1(7),1
    DO ,1 <- #3                 ¯(5),1
    DO ,1 <- #5                 ¯(6),1
    DO ,1 <- #7                 ¯2
    DO ,1 <- #11                ¯7

# Loop through each letter in "Hello World" and print it

(2) IDENTIFY NEXT IN .1 OF PTON(2)
    DO READ OUT ,1
    DO COME FROM (4)            ¯1
    DO RESUME NEXT

(3) IDENTIFY NEXT IN .1 OF PTON(2)
    DO READ IN ,1
    DO COME FROM (6)            ¯1
    DO RESUME NEXT
    
(4)
    DO 2 <- 2 + #1 NOT(3)
    DO (1) NEXT NOT(2)
    DO 3 <- 3 + #1 NOT(1)
    DO ,1 <- #1 NOT(2)

(5)                         ¯(2),3
    DO 2 <- 2                                       
    DO 1 <- 1 NOT(3)
    DO 5 <- 0
    DO 5 <- 5 ~1(4) OF 2

(6)
    DO 6 <- 5 + 1~2
    DO 6 +<- 1

    # Print character
    DO WRITE IN ,1

(7) COME FROM (1)
    DO RESUME NEXT

(8) DO ,(5) <- .(6)

(9) DO (7) <- .#1
    
(10) DO ,(3) <- .#1(7)
    DO 1 <- #0
    DO 2 <- (1) OF 1(7)
    DO 3 <- #5
    DO 1 +<- 1(2) NOT(3)

(11)
    DO RESUME .1999 #1(5)
    DO RESUME ,1999

# Start execution
DO (1) NEXT
DO 2 <- 2
DO 1 <- 1(2)
DO 1 <- 2
DO 1 <- 3
DO 1 <- 4
DO 1 <- 5
DO 1 <- 6
DO 1 <- 7
DO 1 <- 8
DO 1 <- 9
DO 1 <- 10
DO 1 <- 11
DO 1 <- 12
DO 1 <- 13