sed
# SED script to display "Hello, World!"
# SED is a stream editor for filtering and transforming text

# Clear any existing buffer
d

# Append the string to the pattern space
a\
H\
e\
l\
l\
o\
,\
 \ 
W\
o\
r\
l\
d\
!

# Print the pattern space, which now contains "Hello, World!"
p

# End of script
q
