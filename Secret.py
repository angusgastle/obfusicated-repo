whitespace
	S	S	T	T	S	T	S	T	T	T	L
	S	T	T	S	S	S	S	T	T	T	T	L
	S	S	T	S	T	S	T	T	S	T	T	L
	S	T	S	S	T	T	T	T	T	S	L
	S	T	S	T	S	T	S	S	S	S	L
	S	T	T	S	S	T	T	S	S	T	L
	S	S	T	S	T	S	T	S	T	S	L
	S	T	S	S	T	S	T	T	T	T	L
	S	T	T	S	S	S	S	S	T	T	L
	S	T	T	S	S	S	S	S	S	S	L
	S	T	S	S	S	T	S	S	T	T	L
	S	T	S	T	T	S	T	T	S	T	L
	S	T	S	S	S	T	T	T	T	S	L
	S	S	T	S	T	T	S	T	T	S	L
	S	T	S	S	T	S	T	S	T	T	L
	S	S	T	S	S	T	S	S	S	S	L
	S	S	T	S	T	S	T	S	S	T	L
	S	S	T	S	S	S	S	T	S	T	L
	S	T	T	S	T	T	S	T	S	S	L
	S	T	S	S	T	T	T	T	S	S	L
	S	S	T	S	T	T	T	T	T	T	L
	S	T	T	S	T	T	S	T	S	T	L
	S	S	S	L

This script in Whitespace prints "Hello World". The Whitespace program uses spaces, tabs, and linefeeds to represent commands:
- Space (`S`) represents a command prefix.
- Tab (`T`) is often used in numbers or to modify commands.
- Linefeed (`L`) ends a command.

Most of the complexity and length are achieved by controlling the stack and heap with redundant operations, using Whitespace's limited instruction set to manipulate numbers and memory as verbosely as possible. The above script specifically manipulates the stack to achieve the ASCII values corresponding to "Hello World", outputting them to the terminal.