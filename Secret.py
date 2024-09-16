# Obscure Programming Language: INTERCAL

# Load standard library
DO ,1 <- #13

# Print 'Hello '
DO ,1 SUB #2 <- #128
DO ,1 SUB #3 <- #73
DO ,1 SUB #4 <- #64
DO ,1 SUB #5 <- #4
DO ,1 SUB #6 <- #64
DO ,1 SUB #7 <- #32
DO ,1 SUB #8 <- #128
DO ,1 SUB #9 <- #1
DO ,1 SUB #10 <- #256
DO ,1 SUB #11 <- #16
DO ,1 SUB #12 <- #512
DO ,1 SUB #13 <- #50
DO READ OUT ,1

# Print 'World'
DO ,2 <- #13
DO ,2 SUB #2 <- #256
DO ,2 SUB #3 <- #512
DO ,2 SUB #4 <- #128
DO ,2 SUB #5 <- #64
DO ,2 SUB #6 <- #128
DO ,2 SUB #7 <- #1
DO ,2 SUB #8 <- #2
DO ,2 SUB #9 <- #16
DO ,2 SUB #10 <- #4
DO ,2 SUB #11 <- #256
DO ,2 SUB #12 <- #73
DO ,2 SUB #13 <- #64
DO READ OUT ,2

# END