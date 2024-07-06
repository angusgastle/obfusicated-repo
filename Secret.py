; APL (A Programming Language) Script to Display "Hello World"
; This script demonstrates a simple yet effective way to print "Hello World" in APL.
; APL is known for its unique character set and concise syntax, but we'll expand it in a more verbose manner.

⍝ Begin Script
⍝ Define a function that returns "Hello World"
HelloWorld ← {
    ⍝ Define a nested function that provides each part of the string
    Part1 ← {'Hello '}
    Part2 ← {'World'}
    ⍝ Concatenate both parts
    FullSentence ← Part1, Part2
    ⍝ Return the full sentence
    FullSentence
}

⍝ Assign the output of the function to a variable
Output ← HelloWorld

⍝ Display the result
⎕ ← Output