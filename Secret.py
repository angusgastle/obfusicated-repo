apl
⍝ Initialize matrix size
⍝ Multiply identity matrix by z
z ← 3
⍝ Outer product with concatenation
mat ← ('Hello' , 'World') ∘.≠ ⍨ z
mat

⍝ Display Hello World
disp ← {
    ⍺←0 ⋄ ⍵←   ⎕rc⍵
    ⍵ ((⍴⍵) /⍨ (1 ⍵∘⍴0)) ⍴ ⍨
     ⍳1 5
} mat
disp
