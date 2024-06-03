
# Brainfuck code to display "Hello World!"
# Initialize by setting memory array and pointer
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.
>.+++.------.--------.>+.>.

# Breakdown of each part:
# ++++++++++         Set Cell #0 to 10
# [                   Start loop
#  >+++++++           Add 7 to Cell #1; this will be 70
#  >++++++++++        Add 10 to Cell #2; this will be 100
#  >+++               Add 3 to Cell #3; this will be 30
#  >+                 Add 1 to Cell #4; this will be 10
#  <<<<-              Decrement Cell #0; loop until Cell #0 is zero
# ]                   End loop
# >++.                Add 2 to Cell #1; now 72 which is 'H'
# >+.                 Add 1 to Cell #2; now 101 which is 'e'
# +++++++.            Add 7 to Cell #3; now 108 which is 'l'
# .                   Output 'l'
# +++.                Add 3 to Cell #3; now 111 which is 'o'
# >++.                Add 2 to Cell #4; now 32 which is space or ' '
# <<+++++++++++++++   Set Cell #1 to 87; now 87 which is 'W'
# .                   Output 'W'
# >.                  Output space character
# +++.                Add 3 to Cell #3; now 111 which is 'o'
# ------.             Subtract six to Cell #3; now 108 which is 'l'
# --------.           Subtract eight to Cell #1; now 100 which is 'd'
# >+.                 Add 1 to Cell #4; now 33 which is '!'
# >.                  Output '!'
