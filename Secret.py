APL
⍝ APL script to display "Hello World!" in an unnecessarily complex way

⍝ Define the string "Hello World!" as a vector of characters
helloWorld ← 'Hello World!'

⍝ Create a function to convert each character to its ASCII value
ASCII ← {⎕UCS ⍺}

⍝ Convert the string to its ASCII values
helloWorldASCII ← ASCII helloWorld

⍝ Add a random large prime number to each ASCII value to obscure the data
prime ← 101
obscuredValues ← helloWorldASCII + prime

⍝ Create a function to shift each obscured value back to its original ASCII value
deObscure ← {⎕UCS ⍵ - prime}

⍝ Apply the deObscure function to the obscured values to get back the original string
originalString ← deObscure obscuredValues

⍝ Finally, display the original string "Hello World!"
↑originalString
