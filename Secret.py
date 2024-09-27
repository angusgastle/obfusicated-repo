
; K long as possible, well documented.

; Define a new word that initializes the variables for hello world
: initialize-variables
  ." Setting up variables " CR
  0 VALUE h
  0 VALUE e
  0 VALUE l1
  0 VALUE l2
  0 VALUE o
  0 VALUE w
  0 VALUE o2
  0 VALUE r
  0 VALUE l3
  0 VALUE d ;

; Define a word that will assign ASCII values to the variables
: assign-values
  ." Assigning values to variables " CR
  72 TO h  ; ASCII for 'H'
  101 TO e ; ASCII for 'e'
  108 TO l1 ; ASCII for 'l'
  108 TO l2 ; ASCII for 'l'
  111 TO o ; ASCII for 'o'
  87 TO w ; ASCII for 'W'
  111 TO o2 ; ASCII for 'o'
  114 TO r ; ASCII for 'r'
  108 TO l3 ; ASCII for 'l'
  100 TO d ; ASCII for 'd' ;

; Define word to display each character
: display-char ( char -- )
  ." Displaying character: "
  EMIT CR ;

; Define word to convert ASCII values to characters and display them
: display-hello-world
  h display-char
  e display-char
  l1 display-char
  l2 display-char
  o display-char
  32 EMIT CR ; ( space between Hello and World )
  w display-char
  o2 display-char
  r display-char
  l3 display-char
  d display-char ;

; Define main word that combines the initialization, assignment, and display
: main
  ." Starting Hello World script " CR
  initialize-variables
  assign-values
  display-hello-world
  ." Script finished " ;

main
