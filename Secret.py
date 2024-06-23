brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>>>+++++++.>++.+++++++..+++.>+
<--------.+++.------.--------.>+.<.

# This Brainfuck script outputs "Hello World!" character by character.
# Brainfuck uses a memory array of 30,000 cells, each initially zero.

# Initialize cells:
# 
# Cell 1 = 10
# Cell 2 = 70
# Cell 3 = 100
# Cell 4 = 30
# Cell 5 = 10
#
# Loop: 
# 
# Cell 2 = 70 (7 * 10) 
# Cell 3 = 100 (10 * 10) 
# Cell 4 = 30 (3 * 10)
# Cell 5 = 10 (1 * 10)

++++++++++             # Set Cell 1 to 10
[
  >+++++++             # Set Cell 2 to 70 (7 * 10)
  >++++++++++          # Set Cell 3 to 100 (10 * 10)
  >+++                 # Set Cell 4 to 30 (3 * 10)
  >+                   # Set Cell 5 to 10 (1 * 10)
  <<<<-                # Decrement Cell 1 to 0
]

# Output 'H'
>>>+++++++             # Cell 3 = 77
.
# Output 'e'
>++                    # Cell 4 = 32
.
# Output 'l'
+++++++                # Cell 5 = 39
.
# Output 'l'
.
# Output 'o'
+++                    # Cell 6 = 42
.
# Space
<
<--------            # Cell 1 = -8, adjusting the position.
.
# Output 'W'
+++
.
# Output 'o'
++++++                # Cell 4 = 40
.
# Output 'r'
------
.
# Output 'l'
--------              # Cell 3 = 60
.
 
# Output 'd'
>+
.
# Exclamation mark (!)
<
.
