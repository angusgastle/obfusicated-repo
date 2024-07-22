P′′ (P double prime) is an esoteric programming language designed to be simple but Turing complete. Below is a relatively long and complex P′′ script for displaying "Hello World".


; Initialize Tape
START  ( INIT , PTR , OPER , 

; Pointer Initialization
( PTR , 
{ PTRSTART @ 0 @ PTR0 1  PTR1 2  PTR2 3  PTR3 4 } 
 PTRSTART INIT  PTR0 PTR0  PTR1 PTR1  PTR2 PTR2  PTR2 PTR3  PTR3 INIT )

; Memory Tape Initialization
( INIT , 
[ PTR0 72 ] ; H
[ PTR1 101 ] ; e
[ PTR2 108 ] ; l
[ PTR3 108 ] ; l
[ PTR4 111 ] ; o
[ PTR5 32 ] ; Space
[ PTR6 87 ] ; W
[ PTR7 111 ] ; o
[ PTR8 114 ] ; r
[ PTR9 108 ] ; l
[ PTR10 100 ] ; d
[ PTR11 0 ] ; Null termination )

; Operations to Display "Hello World"
( OPER , 
INIT

; Going to first cell
REPEAT 2 { LEFT }

; Loop through the Tape to Print "Hello World"
PTR0 [ PRINT PTR0 RIGHT ]
PTR1 [ PRINT PTR1 RIGHT ]
PTR2 [ PRINT PTR2 RIGHT ]
PTR3 [ PRINT PTR3 RIGHT ]
PTR4 [ PRINT PTR4 RIGHT ]
PTR5 [ PRINT PTR5 RIGHT ]
PTR6 [ PRINT PTR6 RIGHT ]
PTR7 [ PRINT PTR7 RIGHT ]
PTR8 [ PRINT PTR8 RIGHT ]
PTR9 [ PRINT PTR9 RIGHT ]
PTR10 [ PRINT PTR10 RIGHT ]

; Terminate Loop on Null
PTR11 
)

)

; End of Script
)


This script uses P′′'s unique syntax and emphasizes complexity and length over efficiency.