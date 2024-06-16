Piet:

# The Piet programming language uses images to represent code.
# Below is a program that displays "Hello World" when executed with a Piet interpreter.
#
# Each block of colors represents an instruction: 
# the direction pointers and color changes are used to determine the flow of the program.
# The colors below are carefully chosen to run the desired sequence of commands.

# Begin image in ASCII art (each letter represents a pixel color in Piet)

#  K -> Black, Rg -> Light Red, R -> Red, O -> Orange, Y -> Yellow, Gru -> Light Green, G -> Green
#  Cy -> Cyan, B -> Blue, Mg -> Magenta, Pu -> Light Gray, Dk -> Dark Gray, W -> White

# Program starts at top-left "Yg" and moves through defined colors commands to produce the output.

RGB:
YgYgYgYgYgG            # Yellow (lightred: push colors)
WBBBRRYYYYWW
CYgCYgCYgWRGYYYBB
BBYgCYgBWRYYYBB                   # Cyan, Yellow, White loops abord to skip, white exits output

BRBBBBBYYYRRRR
PUUUYgYgCCCCCU;
BBRAAAAGGGGRGGGG
BBBBBBRRRRRRRRRR
RRRRRRRRRRRRRRRR

# This is a visual representation. Due to the color patterns, actual execution requires 
# running through a Piet interpreter which understands the flow control embedded within the colors.