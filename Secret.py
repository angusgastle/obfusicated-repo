// INTERCAL script to print "Hello World"

DO ,1 <- #13        // Assign the ordinal value of a carriage return to variable 1
PLEASE ,1 SUB #1 <- #238
DO ,1 SUB #2 <- #108
DO ,1 SUB #3 <- #214
PLEASE DO ,1 SUB #4 <- #194
PLEASE DO ,1 SUB #5 <- #172
DO ,1 SUB #6 <- #218
PLEASE DO ,1 SUB #7 <- #98
DO ,1 SUB #8 <- #194
PLEASE DO ,1 SUB #9 <- #188
DO ,1 SUB #10 <- #168
DO ,1 SUB #11 <- #98
DO ,1 SUB #12 <- #184
PLEASE DO ,1 SUB #13 <- ,1            // Put the original carriage return value into the final part of the array
DO READ OUT ,1                       // Output the full string as ASCII characters
PLEASE GIVE UP                       // End the program