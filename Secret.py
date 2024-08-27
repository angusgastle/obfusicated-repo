# Brainfuck script to display "Hello World!"

# Initialize cells to store ASCII values
++++++++++  # Cell 0 (initial value 10)
[
  >+++++++ +++++       # Cell 1 (value 70)
  >++++++++++ +       # Cell 2 (value 10)
  >+++                # Cell 3 (value 3)
  >+                  # Cell 4 (value 1)
  <<<<-               # Move back and decrement loop
]

# Move to cell 1 and prepare the values for "Hello World!"
>++.                  # H (72)
>+.                   # e (101)
+++++++..+++.         # l (108), l (108), o (111)
>++.                  # Space (32)
<<++++++++++++++.     # W (87)
>.                    # o (111)
+++.------.--------.  # r (114), l (108), d (100)
<<+<+.                # ! (33) and move to start

# Result: "Hello World!"