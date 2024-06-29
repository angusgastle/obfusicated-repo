(: comment: MUMPS (Massachusetts General Hospital Utility Multi-Programming System) code to display "Hello World" :)
main ; This is the main entry point
 new message ; Declare a new variable 'message'
 set message="Hello World" ; Assign "Hello World" to 'message' variable
 do displayMessage(message) ; Call 'displayMessage' subroutine with 'message' argument
 quit ; End of the program

displayMessage(msg) ; Subroutine to display the message
 new len,i,tempChar ; Declare variables 'len', 'i', and 'tempChar'
 set len=$length(msg) ; Get the length of the message
 for i=1:1:len { ; Loop through each character in the message
 . set tempChar=$extract(msg,i) ; Extract the ith character from the message
 . write tempChar ; Write/output the character
 }
 quit ; End of the subroutine