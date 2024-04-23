whitespace
	[Space][Space][Space][LF]		Push 72 (H)
[Tab][Space][Space][Space][Space][Space][Space][Space][Space][Space][LF]	Push 101 (e)
[Tab][Space][Space][Space][Space][Space][Space][Space][Space][Space][Space][Space][LF]	Push 108 (l)
[Tab][Space][Space][Space][Space][Space][Space][Space][Space][Space][Space][LF]	Push 108 (l)
[Tab][Space][Space][Space][Space][Space][Space][Space][Space][Space][Space][Space][LF]	Push 111 (o)
[Tab][Space][Space][LF]	Push 32 (space)
[Tab][Space][Space][Space][Space][Space][Space][Space][Space][LF]	Push 87 (W)
[Tab][Space][Space][Space][Space][Space][Space][Space][Space][LF]	Push 111 (o)
[Tab][Space][Space][Space][Space][Space][Space][LF]	Push 114 (r)
[Tab][Space][Space][Space][Space][Space][Space][Space][Space][LF]	Push 108 (l)
[Tab][Space][Space][Space][Space][Space][LF]	Push 100 (d)

[LF][LF][LF]	Start a loop for output

[Space][Space]	[Tab][Tab][LF]	Copy the top of the stack which is "H", and print it as char
[Space][Space]	[Tab][Tab][LF]	Copy the next top of the stack, which is "e", and print it as char
[Space][Space]	[Tab][Tab][LF]	Copy next top of the stack, which is "l", and print it as char
[Space][Space]	[Tab][Tab][LF]	Copy next top of the stack, which is "l", and print it as char
[Space][Space]	[Tab][Tab][LF]	Copy next top of the stack, which is "o", and print it as char
[Space][Space]	[Tab][Tab][LF]	Copy next top of the stack, which is "space", and print it as char
[Space][Space]	[Tab][Tab][LF]	Copy next top of the stack, which is "W", and print it as char
[Space][Space]	[Tab][Tab][LF]	Copy next top of the stack, which is "o", and print it as char
[Space][Space]	[Tab][Tab][LF]	Copy next top of the stack, which is "r", and print it as char
[Space][Space]	[Tab][Tab][LF]	Copy next top of the stack, which is "l", and print it as char
[Space][Space]	[Tab][Tab][LF]	Copy the bottom of the stack, which is "d", and print it as char
[Space][Space]	[LF][LF]	Mark the end of the output loop

[Space][Space][Tab][LF][LF]	End of program


The code above uses the Whitespace programming language, which is an esoteric programming language composed entirely of spaces, tabs, and linefeeds. It pushes ASCII values onto the stack which represent the characters of the string "Hello World", and then sequentially pops and outputs them.