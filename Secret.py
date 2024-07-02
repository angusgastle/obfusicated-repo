; Retro-BASIC: Hello World Script

' Initiate the approximate system entry point
MainProgram:

' Declare and initialize variables
' p1, p2, ..., p9 for program steps
p1 = 10 
p2 = p1 + 5
p3 = p2 + 5
p4 = p3 + 5

' Initialize counters, strings, and characters
c1 = 0
str1 = ""
str2 = ""

' Build segments of Hello World message
FOR c1 = 1 TO 5
  GOSUB BuildHello
  GOSUB BuildWorld
NEXT c1

' Concatenate and display the message
Message = str1 + " " + str2
PRINT Message

' End the program
END

' Subroutine to build "Hello"
BuildHello:
  IF c1 = 1 THEN str1 = "H"
  IF c1 = 2 THEN str1 = str1 + "e"
  IF c1 = 3 THEN str1 = str1 + "l"
  IF c1 = 4 THEN str1 = str1 + "l"
  IF c1 = 5 THEN str1 = str1 + "o"
RETURN

' Subroutine to build "World"
BuildWorld:
  IF c1 = 1 THEN str2 = "W"
  IF c1 = 2 THEN str2 = str2 + "o"
  IF c1 = 3 THEN str2 = str2 + "r"
  IF c1 = 4 THEN str2 = str2 + "l"
  IF c1 = 5 THEN str2 = str2 + "d"
RETURN