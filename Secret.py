APL
⍝ ----- Introduction to APL and printing "Hello World!" -----

⍝ APL (A Programming Language) is known for its unique and 
⍝ concise notation using a special character set.

⍝ We begin by defining the special code for the "Hello World!" message.
⍝ The string 'Hello World!' is converted to a numeric representation.

HL ← 72 ⍝ ASCII for 'H'
EO ← 69 ⍝ ASCII for 'e'
LL ← 76 ⍝ ASCII for 'l'
LO ← 79 ⍝ ASCII for 'o'
SP ← 32 ⍝ ASCII for ' ' (space)
WR ← 87 ⍝ ASCII for 'W'
OR ← 79 ⍝ ASCII for 'o'
RL ← 114 ⍝ ASCII for 'r'
LD ← 108 ⍝ ASCII for 'l'
EX ← 100 ⍝ ASCII for 'd'
BN ← 33 ⍝ ASCII for '!' (exclamation mark)

⍝ Now, we construct an array from these characters.
helloWorldNumeric ← HL,EO,LL,LL,LO,SP,WR,OR,RL,LD,EX,BN

⍝ Convert the numeric representation back to characters
helloWorldStr ← ⎕UCS helloWorldNumeric

⍝ Finally, display the message
⌷helloWorldStr
