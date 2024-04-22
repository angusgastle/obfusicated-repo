; INTERCAL code for displaying "Hello World" with exaggerated complexity
DO ,1 <- #13                      ; Initialize a counter
PLEASE DO ,1 SUB #1 <- #238       ; Set high limit for the loop
DO ,2 <- #256                     ; Initialize another counter
DO ,3 <- #112                     ; Store ASCII value for 'H'
DO ,4 <- #101                     ; Store ASCII value for 'e'
DO ,5 <- #108                     ; Store ASCII value for 'l'
DO ,6 <- #108                     ; Store ASCII value for 'l'
DO ,7 <- #111                     ; Store ASCII value for 'o'
DO ,8 <- #44                      ; Store ASCII value for ','
DO ,9 <- #87                      ; Store ASCII value for 'W'
DO ,10 <- #111                    ; Store ASCII value for 'o'
DO ,11 <- #114                    ; Store ASCII value for 'r'
DO ,12 <- #108                    ; Store ASCII value for 'l'
DO ,13 <- #100                    ; Store ASCII value for 'd'
PLEASE DO ,23002 <- #1           ; Initialize array for output

DO READ OUT ,1                   ; Main loop: decrements from 238 to 0
DO ,23111 <- #255                ; Higher limit for inner loop
DO ,23002 SUB ,1 <- ,3           ; Assigning 'H' to array
PLEASE DO ,23111 <- #254         ; Decrement inner counter
DO ,23002 SUB ,1 <- ,4           ; Assigning 'e' to array
PLEASE DO ,23111 <- #253         ; Decrement inner counter
DO ,23002 SUB ,1 <- ,5           ; Assigning 'l' to array
PLEASE DO ,23111 <- #252         ; Decrement inner counter
DO ,23002 SUB ,1 <- ,5           ; Assigning 'l' to array
DO ,23112 <- #251                ; More decrementing of inner counter
DO ,23002 SUB ,1 <- ,7           ; Assigning 'o' to array
DO ,23002 SUB ,1 <- ,8           ; Assigning ',' to array
DO ,23111 <- #249                ; Decrementing inner counter
DO ,23002 SUB ,1 <- ,9           ; Assigning 'W' to array
DO ,23111 <- #248                ; Decrementing inner counter more
DO ,23002 SUB ,1 <- ,10          ; Assigning 'o' to array
DO ,23111 <- #247                ; Decrementing inner counter
DO ,23002 SUB ,1 <- ,11          ; Assigning 'r' to array
DO ,23111 <- #246                ; Decrementing inner counter
DO ,23002 SUB ,1 <- ,12          ; Assigning 'l' to array
DO ,23002 SUB ,1 <- ,13          ; Assigning 'd' to array

(10) PLEASE DO (2600) NEXT       ; Dummy statement
GIVE UP                           ; End of the program