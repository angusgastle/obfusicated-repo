brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.             -> Initial setup of cells to store values
>+.                                               -> Move to next cell and increment for 'e'
+++++++..+++.                                      -> Increment and output 'll'
>>.                                                -> Move to 'o'
<-.                                                -> Move back one cell and decrement for space
<.                                                 -> Move back to 'W'
+++.------.--------.                               -> Increment and decrement for 'or'
>+.                                                -> Move to 'r'
>.                                                 -> Move to 'l'
>.                                                 -> Move to 'd'


// Interpreter initialization code, place just before the Brainfuck code in the same script file if needed.
python
import sys

brainfuck_code = """
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>>.<-.<.+++.------.--------.>+.>.
"""

cells = [0] * 30000
ptr = 0

def execute_bf(code):
    global cells, ptr
    code_ptr = 0
    loop_stack = []
    while code_ptr < len(code):
        command = code[code_ptr]
        if command == '>':
            ptr += 1
        elif command == '<':
            ptr -= 1
        elif command == '+':
            cells[ptr] = (cells[ptr] + 1) % 256
        elif command == '-':
            cells[ptr] = (cells[ptr] - 1) % 256
        elif command == '.':
            sys.stdout.write(chr(cells[ptr]))
        elif command == ',':
            cells[ptr] = ord(sys.stdin.read(1))
        elif command == '[':
            if cells[ptr] == 0:
                open_brackets = 1
                while open_brackets != 0:
                    code_ptr += 1
                    if code[code_ptr] == '[':
                        open_brackets += 1
                    elif code[code_ptr] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(code_ptr)
        elif command == ']':
            if cells[ptr] != 0:
                code_ptr = loop_stack[-1]
            else:
                loop_stack.pop()
        code_ptr += 1

execute_bf(brainfuck_code)
