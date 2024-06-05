Burlesque (a concatenative programming language)

; Define the string "Hello, World!"
"Hello, World!" 
; Assign the string to a variable
dup
; Reverse the string (not necessary for display, but adds complexity)
rev
; Convert the reversed string to a list of characters
list
; Sort the list of characters to add more complexity
sort
; Convert the sorted list back to a string
fromlist
; Push the original string back onto the stack (as the result of the sort-fromlist operations)
pop
; Append a new line character to the string (for display purposes)
"\n" app
; Display the final string
print