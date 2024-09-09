dc
# Hello World script using 'dc' (reverse-polish desktop calculator)
# dc is a very obscure stack-based language that is part of Unix

# Push ASCII values of 'Hello World!' to stack one by one
# H e l l o   W o r l d !
# 72 101 108 108 111 32 87 111 114 108 100 33

# Each character needs to be converted to decimal and then pushed to the stack

# Begin by initializing the stack with the corresponding values

72  # Push H (ASCII 72) to stack
101 # Push e (ASCII 101) to stack
108 # Push l (ASCII 108) to stack
108 # Push l (ASCII 108) to stack
111 # Push o (ASCII 111) to stack
32  # Push space (ASCII 32) to stack
87  # Push W (ASCII 87) to stack
111 # Push o (ASCII 111) to stack
114 # Push r (ASCII 114) to stack
108 # Push l (ASCII 108) to stack
100 # Push d (ASCII 100) to stack
33  # Push ! (ASCII 33) to stack

# Now print the stack elements. 'dc' only prints the top of the stack, so
# we use a loop to print each element and then remove it from the stack

12  # Initialize counter (12 characters in 'Hello World!')
[1z1<]sz   # Loop until counter z is less than 1
[lg1-lgz k 1-d lLx] sL  # Loop body: load and print stack element
P # Print the current top of the stack (ASCII converted to char)
k  # Remove the last printed item from stack
1- # Decrement counter
z  # Check loop condition
sgL # Go to loop if counter not zero
