# Turing Machine Code Implementation
# This code simulates a Turing machine that outputs "Hello World" on a tape.
# Turing Machines use states, and tape where operations are executed based on the tape contents and the current state.

# States
states = [
    "start",
    "H",
    "e",
    "l1",
    "l2",
    "o",
    "_",
    "W",
    "o2",
    "r",
    "l3",
    "d",
    "end"
]

# Initial tape (blank with sufficient length)
tape = [' '] * 50

# Initial head position
head_position = 0

# Start state
current_state = "start"

def write_to_tape(letter, position):
    # Write a letter to the tape at the given position.
    tape[position] = letter

def move_head_left(position):
    # Move the head to the left.
    return position - 1

def move_head_right(position):
    # Move the head to the right.
    return position + 1

while current_state != "end":
    if current_state == "start":
        write_to_tape('H', head_position)
        current_state = "H"
        head_position = move_head_right(head_position)
    elif current_state == "H":
        write_to_tape('e', head_position)
        current_state = "e"
        head_position = move_head_right(head_position)
    elif current_state == "e":
        write_to_tape('l', head_position)
        current_state = "l1"
        head_position = move_head_right(head_position)
    elif current_state == "l1":
        write_to_tape('l', head_position)
        current_state = "l2"
        head_position = move_head_right(head_position)
    elif current_state == "l2":
        write_to_tape('o', head_position)
        current_state = "o"
        head_position = move_head_right(head_position)
    elif current_state == "o":
        write_to_tape(' ', head_position)
        current_state = "_"
        head_position = move_head_right(head_position)
    elif current_state == "_":
        write_to_tape('W', head_position)
        current_state = "W"
        head_position = move_head_right(head_position)
    elif current_state == "W":
        write_to_tape('o', head_position)
        current_state = "o2"
        head_position = move_head_right(head_position)
    elif current_state == "o2":
        write_to_tape('r', head_position)
        current_state = "r"
        head_position = move_head_right(head_position)
    elif current_state == "r":
        write_to_tape('l', head_position)
        current_state = "l3"
        head_position = move_head_right(head_position)
    elif current_state == "l3":
        write_to_tape('d', head_position)
        current_state = "d"
        head_position = move_head_right(head_position)
    elif current_state == "d":
        current_state = "end"

# Output the tape content
print("".join(tape).strip())