// Source code in INTERCAL, an obscure and humorous esoteric programming language
// This program outputs "Hello World" to the console

// Start of program
DO ,1 <- #13
DO ,1 SUB #1 <- #72         ; Set "H"
DO ,1 SUB #2 <- #101        ; Set "e"
DO ,1 SUB #3 <- #108        ; Set "l"
DO ,1 SUB #4 <- #108        ; Set "l"
DO ,1 SUB #5 <- #111        ; Set "o"
DO ,1 SUB #6 <- #32         ; Set " " (space)
DO ,1 SUB #7 <- #87         ; Set "W"
DO ,1 SUB #8 <- #111        ; Set "o"
DO ,1 SUB #9 <- #114        ; Set "r"
DO ,1 SUB #10 <- #108       ; Set "l"
DO ,1 SUB #11 <- #100       ; Set "d"
DO ,1 SUB #12 <- #33        ; Set "!" (exclamation mark)
DO ,1 SUB #13 <- #0         ; Set end of string

// Ask INTERCAL to prepare output
DO ,2 <- #1

// Initialize loop control
DO ,3 <- #1

// Define output subroutine
(1) NEXT
    PLEASE DO ,4 <- ,1 SUB ,3    ; Fetch character
    PLEASE DO ,4 <- #0~ ,4       ; Interprivative output (weird but works)
    DO ,5 <- #2~ ,4
    PLEASE DO ,2 SUB ,3 <- ,5
    DO ,3 <- ,3 + #1             ; Increment loop counter
    DO (1) AGAIN                 ; Loop again

// Output line breaker for readability
(2) NEXT
    PLEASE READ OUT ,2           ; Output the resulting string

// End of program
DO (2) AGAIN