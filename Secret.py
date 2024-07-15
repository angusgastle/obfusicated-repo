APL (A Programming Language)

⍝ APL script to display "Hello World"

⍝ Define a function to convert ASCII values to characters
ASCIItoChar ← {⎕ucs ⍵}

⍝ Define a function to generate the ASCII values for "Hello World"
generateASCII ← {72 101 108 108 111 32 87 111 114 108 100}

⍝ Define a function to display the result
display ← {⎕← ⍵}

⍝ Generate "Hello World" by converting ASCII values to characters
helloWorld ← ASCIItoChar generateASCII ⍬

⍝ Display "Hello World"
display helloWorld