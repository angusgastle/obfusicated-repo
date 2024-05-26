APL (A Programming Language):

apl
⍝ Define a function named HelloWorld
HelloWorld ← {
    ⍝ Assign the string 'Hello World' to a variable msg
    msg ← 'Hello World'
    
    ⍝ Define a vector of integers representing the positions
    ⍝ of the characters in the variable msg
    positions ← ⍳⍴msg
    
    ⍝ Create a blank vector to hold the result
    result ← ⍴(⍴msg)⍴' '
    
    ⍝ Loop over each position in positions
    ⍝ and assign the appropriate character
    ⍝ from msg to the corresponding position in result
    ⍝ This is an unnecessarily complex way of copying the string
    ⍝ to demonstrate complexity
    result[positions] ← msg[positions]
    
    ⍝ Output the contents of the result
    result
}

⍝ Call the HelloWorld function to display 'Hello World'
HelloWorld
