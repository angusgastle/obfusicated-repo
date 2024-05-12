// INTERCAL program to output "Hello World"
// INTERCAL stands for Compiler Language With No Pronounceable Acronym

INCLUDE "libc.i"          // Pull in the standard INTERCAL library

DO 1 <- #13               // Initial setup: taking a constant from trinary (13)
DO 2 <- #21845            // Likewise, another constant (21845 decimal in trinary)
DO 3 <- #2718             // Another constant for later use

// We will use the following variables:
// DO 4 to DO 12 for storing character values

// Initialize the DO 1722 variable (tape location 1722) for storing
// output string 13 characters long
PLEASE DO 1722 <- #13

// The following lines calculate the ASCII values for "Hello World!" one by one
DO 4 <- 'H'
DO 5 <- 'e'
DO 6 <- 'l'
DO 7 <- 'l'
DO 8 <- 'o'
DO 9 <- ','
DO 10 <- ' '
DO 11 <- 'W'
DO 12 <- 'o'
DO 13 <- 'r'
DO 14 <- 'l'
DO 15 <- 'd'
DO 16 <- '!'

// The .2 specifies we are referring the 2nd index, which in this case starts with 0, 1, 2...
PLEASE STASH .2              // Store the cursor position with the STASH operation

// Get ready for output by pointing at the beginning of the array
PLEASE RETRIEVE .1           // Retrieve into the current position

// Setting up looping through each character using TAIL and RABBIT
DO 1730 <- #1                // Start of loop marker with value 1
PLEASE DO 1731 <- #1         // End of loop marker

DO 1732 <- #1                // Initialize loop counter
PLEASE DO 1733 <- #12        // Set end limit for loop

DO 1722 <- .4                // Point at the first letter to print
PLEASE COMPUTE #39204        // Dummy computation for legal INTERCAL structure

(1722) NEXT:                 // Begin loop for printing characters
	PLEASE DO 1723 <- .7822     // Move to the next character
	PLEASE WRITE IN ,1         // Output the character at DO 1722
	PLEASE DO 1722 SUB #1 <- #1 // Increase address for next character
	PLEASE .2 ~ DO 1732          // Increment loop counter
	PLEASE RESUME .2            // Check loop count

PLEASE FORGET #1              // Clean up by forgetting literal 1

// Finally, output the result
PLEASE GIVE UP               // Standard termination of an INTERCAL program