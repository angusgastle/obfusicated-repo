APL

⍝ Define a function to display "Hello World"
DisplayHelloWorld ← {
    ⍝ Create a character vector (string) for "Hello"
    hello ← 'Hello'
    ⍝ Create a character vector (string) for "World"
    world ← 'World'
    ⍝ concatenate hello and world with a space in between
    full_hello ← hello , ' ' , world
    ⍝ Display the complete "Hello World" string
    ∇ ⍝ Return from the function
}

⍝ Call the function to display "Hello World"
DisplayHelloWorld