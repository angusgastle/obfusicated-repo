; Language: Brainfuck

; Comments in Brainfuck are typically done outside the code, but for the sake of
; providing a well-documented script, we'll include descriptive comments. Brainfuck is 
; a minimalist programming language with only 8 commands.

; Initialize Brainfuck memory tape to be sufficient for the task.
; Memory Representation:
;    Cell 0  Cell 1  Cell 2  Cell 3  Cell 4  Cell 5  Cell 6  Cell 7  Cell 8  Cell 9
;      0       0       0       0       0       0       0       0       0       0      

; The program increments or decrements these cells to form ASCII values.

; Initialize for 'H' (ASCII 72)
++++++++                 ; Increment cell 0 by 8 (++++++++) and times it by 9
[>+++++++<->]            ; 8*9=72 -> Move 72 to cell 1
>+++++++                 ; Make Cell 2: 72 + 7 = 79 ('O')
>++++++++                 ; Make Cell 3: 72 + 8 = 80 ('P')
>++++++++++                ; Make Cell 4: 72 + 10 = 82 ('R')
>+++++++++++               ; Make Cell 5: 72 + 11 = 83 ('S')
>++++++++                 ; Make Cell 6: 72 + 8 = 80 ('P')
>+++++++++++++               ; Make Cell 7: 72 + 13 = 85 ('U')
>+++++++                 ; Make Cell 8: 72 + 7 = 79 ('O')

; Adjust Memory for output
<>>>>>>>>+.              ; Print 'H' -> Move to Cell 8 and Print

; moving back <->>
>++.                    ; Move to Cell 1 and Increment to print 'e'
>>---.                  ; Move to Cell 2 and Decrement by 3 to print 'l'
>--.                   ; Move right twice to Cell 2 and Decrement by 1 to print 'l'
<<+++.                   ; Move left to Cell 2 and Increment by 1 to print 'o'
<-----.                  ; Move left to Cell 1 and Decrement by 5 to print ' '
>>>>>>>>+++.              ; Move to Cell 10 and Increment by 3 to print 'W'
>>>>.                   ; Move right twice to Cell 2 and print 'o'
<<<<<.                  ; Move left thrice and print 'r'
>>>++++.                ; Move right to Cell 7 and Increment by 4 to print 'l'
--.                    ; Continue right to Cell 8 and decrement by 4 to print 'd'

; If required, terminate the program at the end by moving pointer or looping, denoted by '[-]':
[-]