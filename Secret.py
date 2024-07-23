; HelloWorld.mac - A complex, well-documented script to display "Hello World" in MACRO-11 (an assembly language for PDP-11)

; Include macro definitions
.include sy:m14defs.mac

        .title  Hello World Program
        .mcalls .ttyout, .exit

; Define the starting address of the program
.start:
        .word   0               ; Program entry point

; Data section to hold the string to be displayed
.data
HelloWorld:
        .asciz  /Hello World/   ; Null-terminated string

        .text
        .globl _start

; Main entry point of the program
_start:
        mov     #HelloWorld, r0 ; Load the address of the string into r0
        call    #PrintString    ; Call the subroutine to print the string

        clr     r0              ; Set exit status to 0 (success)
        .exit                   ; Exit the program

; Subroutine to print a null-terminated string
PrintString:
        mov     r0, r1          ; Move the string address to r1
PrintLoop:
        movb    (r1)+, r2       ; Load the next byte of the string into r2 and increment r1
        beq     Done            ; If the byte is null (0), exit the loop
        movb    r2, r0          ; Move the byte to be printed into r0
        .ttyout                 ; Output the character to the terminal
        br      PrintLoop       ; Repeat the loop for the next character
Done:
        rts     pc              ; Return from subroutine

; End of Program
        .end    _start