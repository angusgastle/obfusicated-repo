5WS2 ;; Sokoban programming language.

; Load the Sokoban environment
(BOARD
 "######"
 "#@ $. "
 "######")

; Define a variable for the message
(DEFINE message "Hello World")

; Create a custom object to display the message
(DEFINEOBJ letter (BLOCK 0))

; Create a function to plot each character on the board
(DEFINEFUN plotLetter
 (PARAM x: INT y: INT char: INT)
 (SET (BOARD-AT x y) char))

; Main program to display the message
(DEFINEFUN main
 (LET len (LENGTH message)
 (LET i 0
 (WHILE (< i len)
 (LET x (+ i 1)
 (LET y 1
 (LET char (CHAR-AT message i)
 (plotLetter x y char)))))
 (SET i (+ i 1)))))

; Run the main program
main