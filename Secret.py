whitespace
	S S S	T	LF	; Push "H" (72)
	T	S	S	S	S	S	T	T	T	T	LF
	S S	T	LF	; Push "e" (101)
	T	S	S	S	S	S	S	T	T	LF
	S S	T	LF	; Push "l" (108)
	T	S	S	S	S	S	S	T	L	S	LF
	S	S	T	LF	; Push another "l"
	T	S	S	S	S	S	S	T	L	S	LF
	S S	T	LF	; Push "o" (111)
	T	S	S	S	S	S	S	T	T	S	LF
	S S	T	T	LF	; Push space " " (32)
	T	T	T	LF
	S S	T	LF	; Push "W" (87)
	T	S	S	S	S	S	T	T	T	T	S	LF
	S S	T	LF	; Push "o" (111)
	T	S	S	S	S	S	S	T	T	S	LF
	S S	T	LF	; Push "r" (114)
	T	S	S	S	S	S	S	T	T	LF
	S S	T	LF	; Push "l" (108)
	T	S	S	S	S	S	S	T	L	S	LF
	S S	T	LF	; Push "d" (100)
	T	S	S	S	S	S	S	L	L	LF
	S S	T	T	LF	; Push "!" (33)
	T	T	T	T	T	S	T	LF
	S	LF		S LF	; Label for loop start (Print loop)
	T	LF	S	T	LF	; Print top of stack
	N	S	S	LF	 L	T	LF	S	T	T	LF	; Jump to loop start if stack not empty
	LF

This Whitespace program pushes the ASCII values of the characters of "Hello World!" onto the stack, then enters a loop to print each character and check if the stack is empty, jumping back to print again if it is not. Each command consists of spaces, tabs, and line feeds, which denote different commands in Whitespace.