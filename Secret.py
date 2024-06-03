
/*
 * Slightly esoteric "Hello World!" program in INTERCAL.
 * It was designed to be different from all other programming languages.
 */
DO ,1 <- #13
DO ,1 SUB #1 <- #'H'
DO ,1 SUB #2 <- #'e'
DO ,1 SUB #3 <- #'l'
DO ,1 SUB #4 <- #'l'
DO ,1 SUB #5 <- #'o'
DO ,1 SUB #6 <- #32    ; ASCII space
DO ,1 SUB #7 <- #'W'
DO ,1 SUB #8 <- #'o'
DO ,1 SUB #9 <- #'r'
DO ,1 SUB #10 <- #'l'
DO ,1 SUB #11 <- #'d'
DO ,1 SUB #12 <- #'!'
DO ,1 SUB #13 <- #0    ; Null terminator for output

PLEASE DO ,1 <- #1     ; Just a formality in INTERCAL, moving content into main

; Loop over and display characters until null terminator is reached
(1) NEXT:
    DO FORGET #2       ; Prepare for next character
    DO READ OUT ,1 SUB #1
    DO .1 <- "ON"~#1  ; Modify control variable to point to next character in string
    DO (NEXT) NEXT!0(#1)     ; Loop condition check

DO .1 <- "FF"
DO RESUME NEXT
DO GIVE UP
