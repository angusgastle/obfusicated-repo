VTL-2 (Visual Thinking Language 2) is an obscure programming language. Here is an example script that displays "Hello World" in VTL-2:


MODULE HELLO_WORLD

  // Data statements
  DATA "H": [72]
  DATA "E": [69]
  DATA "L": [76]
  DATA "O": [79]
  DATA "W": [87]
  DATA "R": [82]
  DATA "D": [68]
  DATA "SPACE": [32]
  DATA "EXCLAMATION": [33]

  // Step 1: Initialize Frame
  FRAME INIT
    // Create a buffer to hold message characters
    BUFFER Message, 12 // max 12 characters including spaces
  ENDFRAME
  
  // Step 2: Populate characters to the buffer
  FRAME CHAR_FILL 
    MOV "H" TO Message[1]
    MOV "E" TO Message[2]
    MOV "L" TO Message[3]
    MOV "L" TO Message[4]
    MOV "O" TO Message[5]
    MOV "SPACE" TO Message[6]
    MOV "W" TO Message[7]
    MOV "O" TO Message[8]
    MOV "R" TO Message[9]
    MOV "L" TO Message[10]
    MOV "D" TO Message[11]
    MOV "EXCLAMATION" TO Message[12]
  ENDFRAME
  
  // Step 3: Print each character from buffer
  FRAME PRINT_LOOP
    INDEX i FROM 1 TO 12 STEP 1 
      PRINT Message[i]
    ENDINDEX
  ENDFRAME
  
  // Step 4: Assemble frames into a program
  PROGRAM RUN
    CALL INIT
    CALL CHAR_FILL
    CALL PRINT_LOOP
  ENDPROGRAM

ENDMODULE
