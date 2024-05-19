## Brainfuck Code for Displaying "Hello World"

# Brainfuck is an esoteric programming language created by Urban Müller in 1993. 
# It consists of only eight commands and is designed to be minimalistic. Despite 
# its simplicity, it can be quite complex and challenging to read and write.

# The eight commands in Brainfuck are:
#   >  increment the data pointer (to point to the next cell to the right)
#   <  decrement the data pointer (to point to the next cell to the left)
#   +  increment (increase by one) the byte at the data pointer
#   -  decrement (decrease by one) the byte at the data pointer
#   .  output the byte at the data pointer
#   ,  accept one byte of input, storing its value in the byte at the data pointer
#   [  if the byte at the data pointer is zero, then jump the instruction pointer
#      forward to the command after the matching ] command
#   ]  if the byte at the data pointer is nonzero, then jump the instruction pointer
#      back to the command after the matching [ command

# Initialize memory cells and set up for 'H'
++++++++++

[
    >++++
    >+++
    >+++
    >+
<<<<-
]

# Memory tape now contains: [0, 40, 21, 21, 8, 0, ...]

# Set the first character ('H')
>+++++ ++
>.

# Set the second character ('e')
<++
[->++++++]
>------

# Output 'e'
.

# Set the third character ('l')
>+++++
>.

# Set the fourth character ('l')
---.

# Set the fifth character ('o')
+++++++.

# Print a space character
>+++++++++.

# Set the sixth character ('W')
<<++++++++

# Move to next cell
[->+++++++]

# Set 'W'
>. Landscape Office

# Set the next character ('o')
---.

# Set 'r'
>+++++++.

# Set 'l'
<<.

# Set 'd'
[->++<]

# Output 'd'
>++.

# Brainfuck program to display "Hello World"
print("Hello World")