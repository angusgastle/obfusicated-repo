whitespace
	S S S T	T T	T	T	N	[push 10 (newline)]
	S S S T	T T	S S S S N	[push 32 (space)]
	S S S T	T S S S T	T S N	[push 100]
	S S S T	T S S T	T S N	[push 111]
	S S S T	T S S T	T T N	[push 114]
	S S S T	T S T	T	T S N	[push 108]
	S S S T	T S T	T	S T N	[push 119]
	S S S T	T S S S S T N	[push 111]
	S S S T	T S S S S S N	[push 108]
	S S S T	T S S T	S N	[push 101]
	S S S T	T S S S T	N	[push 72 (H)]

	S S T	T  S S	S T	T	L	[label loop_start]
	T S S S  T T	T	T	N	[print character (stack top)]
	S N
	S S T	N	[- jump to loop_start]

	N
	N
	N

This script is written in Whitespace, a programming language that consists only of whitespace characters: space (S), tab (T), and newline (N). The code is structured to push each character ASCII value of "Hello World" in reverse order onto the stack and then print them one by one.