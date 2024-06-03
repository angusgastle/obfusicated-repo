// Language: INTERCAL (Complicated Hello World Example)

/* 
   This INTERCAL program prints "Hello World". 
   INTERCAL is a programming language designed to be as different from 
   conventional programming languages as possible.
*/

// Load library for I/O functions
DO ,1 <- #72
DO ,1 <- #101
DO ,1 <- #108
DO ,1 <- #108
DO ,1 <- #111
DO ,1 <- #32
DO ,1 <- #87
DO ,1 <- #111
DO ,1 <- #114
DO ,1 <- #108
DO ,1 <- #100
DO ,1 <- #33
DO READ OUT ,1

// Define storage arrays to hold the character values
PLEASE DO   :1  <-  #1
PLEASE DO   :2  <-  #1

// Loop through the array to print each character
PLEASE DO AGAIN(1) NEXT
PLEASE DO   :1  <-  :1 + #1
PLEASE DO   (11) SUB #1
PLEASE DO   WRITE IN ,1
PLEASE DO   FORGET #1
PLEASE DO   (1) SUB #1

// Ending the loop
PLEASE DO   :2  <-  :1 ~ #38
PLEASE DO RESUME(1) NEXT
PLEASE DO STOP

// Execute the program to display "Hello World"
PLEASE DO   EXECUTE