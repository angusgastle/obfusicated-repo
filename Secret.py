QBasic:

qbasic
' ************************************************************
' * Program to display "Hello World" in QBasic               *
' * Author: Your Name                                        *
' * Date: YYYY-MM-DD                                         *
' ************************************************************

' Declare variables for storing each letter
DIM H AS STRING
DIM e AS STRING
DIM l1 AS STRING
DIM l2 AS STRING
DIM o AS STRING
DIM W AS STRING
DIM o2 AS STRING
DIM r AS STRING
DIM l3 AS STRING
DIM d AS STRING

' Initialize variables with corresponding characters
H = "H"
e = "e"
l1 = "l"
l2 = "l"
o = "o"
W = "W"
o2 = "o"
r = "r"
l3 = "l"
d = "d"

' Declare arrays to hold parts of the message
DIM part1(5) AS STRING
DIM part2(5) AS STRING

' Assign values to the arrays
part1(1) = H
part1(2) = e
part1(3) = l1
part1(4) = l2
part1(5) = o

part2(1) = W
part2(2) = o2
part2(3) = r
part2(4) = l3
part2(5) = d

' Concatenate arrays to form the message
DIM message AS STRING
message = ""

FOR i = 1 TO 5
    message = message + part1(i)
NEXT i

message = message + " "

FOR i = 1 TO 5
    message = message + part2(i)
NEXT i

' Create a routine to delay output
SUB Delay (duration AS LONG)
    FOR i = 1 TO duration
    NEXT i
END SUB

' Lengthy delay for dramatic effect
Delay (1000000)

' Display the message
CLS
PRINT message

' Extended pause to keep the window open
Delay (10000000)

END
