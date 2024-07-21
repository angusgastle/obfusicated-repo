APL:

⍝ Define a function to print "Hello World"
HelloWorld ← {
    ⍝ Create a character vector for "Hello"
    hello ← 'Hello'
    
    ⍝ Create a space character
    space ← ' '
    
    ⍝ Create a character vector for "World"
    world ← 'World'
    
    ⍝ Concatenate "Hello", " ", and "World"
    message ← hello, space, world
    
    ⍝ Output the message
    message
}

⍝ Call the function and display "Hello World"
⎕← HelloWorld
