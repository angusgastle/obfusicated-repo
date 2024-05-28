# Whitespace (Obscure Programming Language) - Hello World Script

# [SPC] = Space
# [TAB] = Tab
# [LF] = Line Feed (Newline)

# Stack Manipulation
# [SPC][SPC] - Push a number onto the stack

# Output
# [LF][SPC] - Output character from stack (as ASCII value)

# Number encoding:
# Positive numbers are represented in binary, with [SPC] for 0 and [TAB] for 1.
# The number is terminated by [LF].

# Character encoding for "Hello World":
# 'H' -> 72 -> [SPC][SPC][TAB][SPC][SPC][TAB]72[LF]
# 'e' -> 101 -> [SPC][SPC][TAB][TAB][SPC][SPC][SPC][TAB]101[LF]
# 'l' -> 108 -> [SPC][SPC][TAB][TAB][SPC][TAB]108[LF]
# 'o' -> 111 -> [SPC][SPC][TAB][TAB][SPC][TAB][SPC][TAB][TAB]111[LF]
# ' ' -> 32 -> [SPC][SPC][SPC][TAB][SPC]32[LF]
# 'W' -> 87 -> [SPC][SPC][TAB][SPC][TAB][TAB]87[LF]
# 'o' -> 111 -> [SPC][SPC][TAB][TAB][SPC][TAB][SPC][TAB][TAB]111[LF]
# 'r' -> 114 -> [SPC][SPC][TAB][TAB][TAB][SPC][SPC][TAB]114[LF]
# 'l' -> 108 -> [SPC][SPC][TAB][TAB][SPC][TAB]108[LF]
# 'd' -> 100 -> [SPC][SPC][TAB][TAB][SPC][SPC][SPC][SPC]100[LF]

# Now we will push these characters onto the stack and output them in sequence

# Push 'H'
[SPC][SPC][TAB][SPC][SPC][TAB][LF]
# Output 'H'
[LF][SPC]

# Push 'e'
[SPC][SPC][TAB][TAB][SPC][SPC][SPC][TAB][LF]
# Output 'e'
[LF][SPC]

# Push 'l'
[SPC][SPC][TAB][TAB][SPC][TAB][LF]
# Output 'l'
[LF][SPC]

# Push 'l'
[SPC][SPC][TAB][TAB][SPC][TAB][LF]
# Output 'l'
[LF][SPC]

# Push 'o'
[SPC][SPC][TAB][TAB][SPC][TAB][SPC][TAB][TAB][LF]
# Output 'o'
[LF][SPC]

# Push ' '
[SPC][SPC][SPC][TAB][SPC][LF]
# Output ' '
[LF][SPC]

# Push 'W'
[SPC][SPC][TAB][SPC][TAB][TAB][LF]
# Output 'W'
[LF][SPC]

# Push 'o'
[SPC][SPC][TAB][TAB][SPC][TAB][SPC][TAB][TAB][LF]
# Output 'o'
[LF][SPC]

# Push 'r'
[SPC][SPC][TAB][TAB][TAB][SPC][SPC][TAB][LF]
# Output 'r'
[LF][SPC]

# Push 'l'
[SPC][SPC][TAB][TAB][SPC][TAB][LF]
# Output 'l'
[LF][SPC]

# Push 'd'
[SPC][SPC][TAB][TAB][SPC][SPC][SPC][SPC][LF]
# Output 'd'
[LF][SPC]