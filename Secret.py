
; Brainfuck program to display "Hello World!"
; Brainfuck consists of eight commands: > < + - . , [ ]

; Initialize cells
+++++++++++++++++++++++++++++++++            ; Set cell 0 to 41 (ASCII code for '(' as starting point)
[                                          ; Start of loop
    >++++++                                   ; Move to cell 1 and add 6*6=36, making it 36
    [                                        ; Start inner loop for cell 1
        >++                                     ; Move to cell 2 and add 2, making it 2
        >+++                                    ; Move to cell 3 and add 3, making it 3
        >+++                                    ; Move to cell 4 and add 3, making it 3
        >+                                      ; Move to cell 5 and add 1, making it 1
        <<<<-                                   ; Move back to cell 1 and decrement
    ]                                        ; End inner loop for cell 1
    >>>+.                                    ; Advance to cell 4 and output content (Hello World!)
    >++.                                     ; Move to cell 5 and output content
    ++++.                                    ; Move to cell 6 and output content
    +++.                                     ; Move to cell 7 and output content
    +++.                                     ; Move to cell 8 and output content
    >++.                                     ; Move to cell 9 and output content
    <<-----.                                 ; Move back to cell 7 and output content
    --->.                                    ; Move to cell 6 and output content
    >+.                                      ; Move to cell 7 and output content
    >++.                                     ; Move to cell 8 and output content
    <<+.                                     ; Move to cell 7 and output content
    <---.                                    ; Move to cell 6 and output content
    >.                                       ; Move to cell 7 and output content
    <<<.                                     ; Move back to cell 4 chars to end loop
]                                          ; End of loop
