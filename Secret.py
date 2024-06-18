APL (A Programming Language) - Hello World

⍝ Define the message to be displayed
message ← 'Hello World'

⍝ Calculate the length of the message
msgLength ← ≢message

⍝ Create a vector of indices from 1 to the length of the message
indices ← ⍳msgLength

⍝ Define a function to retrieve characters from a string
getChar ← {message[indices[⍵]]}

⍝ Create an empty vector to store the characters
output ← ⍳0

⍝ Loop through each index, get the corresponding character, and store it in the output vector
output ← output , getChar ⍵ ⍵ :⍪⍨ indices

⍝ Convert the output vector to a string
finalOutput ← ∊output

⍝ Display the final message
finalOutput

⍝ Print message to console (specific to some APL systems)
⎕ ← finalOutput