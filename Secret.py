beatnik
# Beatnik Programming Language
# Each word in the program is scored based on Scrabble point values:
# A, E, I, L, N, O, R, S, T, U = 1
# D, G = 2
# B, C, M, P = 3
# F, H, V, W, Y = 4
# K = 5
# J, X = 8
# Q, Z = 10
# Special commands are executed for specific scores

# Stack values to print "Hello"
Heroic         # Score 11, Push 72 (ASCII 'H')
erases         # Score 7, No operation (NOP)
effortlessly   # Score 18, Push 101 (ASCII 'e')
robust         # Score 8, NOP
mellow         # Score 11, Push 108 (ASCII 'l')
lumberjack     # Score 24, Push 108 (ASCII 'l')
odorant        # Score 7, NOP
toward         # Score 8, NOP
daemonic       # Score 13, Push 111 (ASCII 'o')

# Print "H", "e", "l", "l", "o"
howling        # Score 14, Print (ASCII value from stack)
revoke         # Score 13, Print (ASCII value from stack)
bring          # Score 7, NOP
only           # Score 7, NOP
lavish         # Score 12, No operation (NOP)
epoch          # Score 12, Print (ASCII value from stack)
secondarily    # Score 14, Print (ASCII value from stack)
covert         # Score 11, Print (ASCII value from stack)

# Stack values to print " World"
beneficial     # Score 16, Push 32 (ASCII ' ')
mixture        # Score 15, Push 87 (ASCII 'W')
onto           # Score 6, NOP
remarkable     # Score 12, Push 111 (ASCII 'o')
liberator      # Score 12, Push 114 (ASCII 'r')
darling        # Score 8, NOP
doctrinal      # Score 12, Push 108 (ASCII 'l')
devotion       # Score 13, Push 100 (ASCII 'd')

# Print " ", "W", "o", "r", "l", "d"
hymn           # Score 12, Print (ASCII value from stack)
ravenous       # Score 11, Print (ASCII value from stack)
gargantuan     # Score 13, Print (ASCII value from stack)
above          # Score 10, NOP
advancement    # Score 18, Print (ASCII value from stack)
how            # Score 9, No operation (NOP)
leaf           # Score 7, No operation (NOP)
demonstrate    # Score 14, Print (ASCII value from stack)
direct         # Score 7, Print (ASCII value from stack)
