whitespace
push "H"
push "e"
push "l"
push "l"
push "o"
push ","
push " "
push "W"
push "o"
push "r"
push "l"
push "d"
push "!"

mark PrintLoop
  dup
  jz End
  putchar
  jmp PrintLoop

mark End
  push 0
  end

# Whitespace characters:
# [Space]   : Stack Manipulation
# [Tab][Space] : Arithmetic
# [Tab][Tab]   : Heap access
# [LF]     : Flow Control
# [Tab][LF] : I/O

# Commands used:
# "push x" : Pushes the ASCII value of character x on the stack.
# "dup"    : Duplicates the top item on the stack.
# "jz"     : Jump if zero. Used here to end string printing when ASCII 0 is encountered.
# "putchar": Output the character at the top of the stack.
# "jmp"    : Jump unconditionally to the given label.
# "push 0" : Cleanly exits the program by pushing 0 and then using "end".
