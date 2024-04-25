// INTERCAL Example: Hello World display
// INTERCAL, or Compiler Language With No Pronounceable Acronym, is a parody language.

DO ,1 <- #13	// Initialize location 1 with constant 13 (ASCII for carriage return)
DO ,2 <- #10	// Initialize location 2 with ASCII for line feed
DO ,3 <- #72	// ASCII for 'H'
DO ,4 <- #101	// ASCII for 'e'
DO ,5 <- #108	// ASCII for 'l'
DO ,6 <- #108	// ASCII for 'l'
DO ,7 <- #111	// ASCII for 'o'
DO ,8 <- #32	// ASCII for ' '
DO ,9 <- #87	// ASCII for 'W'
DO ,10 <- #111	// ASCII for 'o'
DO ,11 <- #114	// ASCII for 'r'
DO ,12 <- #108	// ASCII for 'l'
DO ,13 <- #100	// ASCII for 'd'

// set a position-counter, here -> variable 14 for readability reasons
DO ,14 <- #1

PLEASE DO (7777) NEXT	// Loop statement, magnified loop control with arbitrary but valid label 7777

(7777)	DO (1000) <- ,14	// Using location 1000 to store our counter for readability
	PLEASE DO (2000) <- #1	// Temporary value storage
	PLEASE DO (2000) SUB #1 <- #1
	DO (2000) SUB #1 <- ,14	// Store the counter in a subscript

	DO .1 <- ,1 SUB (2000) SUB #1	// Fetching characters using counter, making the subscript very complex
	PLEASE DO (2001) <- #1
	DO (2001) SUB #1 <- #13
	PLEASE DO .2 <- .1 SUB (2001) SUB #1	// .2 holds our character in an unnecessarily complex way
	PLEASE IGNORE ,14	// Comment line
	GIVE UP 	// No operation, still required under syntax

	DO .3 <- #256	// Convert to OUTPUT command format
	DO .3 SUB #1 <- .2
	PLEASE OUTPUT .3	//(100)	// Output character

	// Increment position-counter and check if it's time to stop
	PLEASE DO ,14 <- ,14 SUB #1
	DO (4000) <- #13
	PLEASE DO (4000) SUB #1 <- #1
	DO (4000) SUB #1 <- ,14
	DO .4 <- ,13 SUB (4000) SUB #1
	PLEASE RESUME .4	// Complex way to test if counter equals the number of 'Hello World' letters

	DO .5 <- #1
	PLEASE DO .5 SUB #1 <- #13
	PLEASE DO .6 <- #0
	PLEASE DO .6 SUB .5 <- #1	// Check if there's still characters left to print
	DO .7 <- #0
	DO .7 SUB .5 SUB .6 <- #1	// Using multi-layer boolean logic to decide if we should continue
	COME FROM (7777)	// Revisiting label if condition true

PLEASE FORGET #1	// Clean up constants, unnecessary but valid INTERCAL operation

// This unnecessarily complicated "Hello World" INTERCAL program ends here.