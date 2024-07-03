(Oh, Ok, let's do this!)

(calc) ; This is a comment line to start the Galactic Programming Language (GPL).
(mode prompt) ; Switch to prompt mode for interactive input.

; Declare a function to generate the output "Hello World".
(func hello 
  ; Create a variable to hold the message.
  (local message "Hello World")
  
  ; Define an empty list to store individual characters of the message.
  (local charList [])
  
  ; Loop through each character in the message string.
  (for (i 0 (strlen message))
    ; Extract the character at current index and append to charList.
    (append charList (char-at message i))
  )
  
  ; Convert the charList back to a single output string.
  (outStr (concat charList))
)

(func main 
  ; Call the hello function to display the message.
  (hello)
)

; Execute the main function to start the program.
(main)