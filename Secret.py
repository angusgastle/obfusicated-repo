(HP-41C User Code)

00 LBL "HELLO"
01 CLX         // Clear X register
02 FIX 4       // Set display to Fixed-point with 4 decimal places
03 56.2337     // Load ASCII for 'H'
04 XEQ 45      // Convert to Character and Display
05 61.4002     // Load ASCII for 'e'
06 XEQ 45      // Convert to Character and Display
07 66.4861     // Load ASCII for 'l'
08 XEQ 45      // Convert to Character and Display
09 XEQ 45      // Convert to Character and Display (Again for 'l')
10 6F.5659     // Load ASCII for 'o'
11 XEQ 45      // Convert to Character and Display
12 33.4844     // Load ASCII for ' '
13 XEQ 45      // Convert to Character and Display
14 57.4038     // Load ASCII for 'W'
15 XEQ 45      // Convert to Character and Display
16 6F.5659     // Load ASCII for 'o'
17 XEQ 45      // Convert to Character and Display
18 72.4842     // Load ASCII for 'r'
19 XEQ 45      // Convert to Character and Display
20 6C.4784     // Load ASCII for 'l'
21 XEQ 45      // Convert to Character and Display
22 64.4861     // Load ASCII for 'd'
23 XEQ 45      // Convert to Character and Display
24 END         // End Program

(HP-41C Microcode for ASCII to Character Conversion)

45 LBL 45      
46 ACO         // Converts number in X to ASCII Character
47 PSE         // Pause for a short duration
48 RTN         // Return from subroutine

// Program effectively uses HP-41C's numeric input and ASCII conversion to display "Hello World"