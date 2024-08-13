APL
⍝ APL Script to display "Hello World" in a complex manner

⍝ Random seed for reproducibility
⎕RL←12345

⍝ Define "Hello" and "World" as variables
hello←'Hello'
world←'World'

⍝ Create a concatenation function
concat←{⍵,⍺}

⍝ Create a function to apply uppercase to first letter
capitalize←{(⍵[1]),↑⍕1↓⍵}

⍝ A function to reverse a string
reverse←{⍵⌽⍨⍳⍴⍵}

⍝ Generate a random number
random_number←{(1+?⍵)←⍵}

⍝ Determine the length of the word "Random"
length_hello←≢hello
length_world←≢world

⍝ Create a random offset
offset←random_number 3

⍝ Generate a transformation matrix
transformation_matrix←(⊂hello),¨⍳length_hello

⍝ Apply reverse operation based on random offset
transformed_matrix←offset⊥⌽⍨⍳length_world

⍝ Transform "World" into reverse order based on the matrix
reversed_world←world[transformed_matrix]

⍝ Capitalize both words
capitalized_hello←capitalize(hello)
capitalized_world←capitalize(reversed_world)

⍝ Concatenate the strings with a space
concatenated_greeting←capitalized_hello concat ' ' concat capitalized_world

⍝ Display the result
concatenated_greeting
