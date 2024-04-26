whitespace
		space	tab	space	 	push
tab		space	space	space	space	push	0 (The ASCII value of newline, will be used later)
		space	tab	space	 	push
tab		space	space	space	space	push	0
		space	tab	space	 	push
tab		space	space	space	!	push	100 (ASCII d)
		space	tab	space	 	push
tab		space	space	space	l	push	108 (ASCII l)
		space	tab	space	 	push
tab		space	space	space	o	push	111 (ASCII o)
		space	tab	space	 	push
tab		space	space	space	W	push	87 (ASCII W)
		space	tab	space	 	push
tab		space	space	space	space	push	32 (ASCII space)
		space	tab	space	 	push
tab		space	space	o	push	111 (ASCII o)
		space	tab	space	 	push
tab		space	space	l	push	108 (ASCII l)
		space	tab	space	 	push
tab		space	space		e	push	101 (ASCII e)
		space	tab	space	 	push
tab		space	space	H	push	72 (ASCII H)

		space	space	space	 	duplicate top of the stack (H)
		space	tab	tab	 	output as character
		space	space	space	 	duplicate top of the stack (e)
		space	tab	tab	 	output as character
		space	space	space	 	duplicate top of the stack (l)
		space	tab	tab	 	output as character
		space	space	space	 	duplicate top of the stack (l)
		space	tab	tab	 	output as character
		space	space	space	 	duplicate top of the stack (o)
		space	tab	tab	 	output as character
		space	space	space	 	duplicate top of the stack (space)
		space	tab	tab	 	output as character
		space	space	space	 	duplicate top of the stack (W)
		space	tab	tab	 	output as character
		space	space	space	 	duplicate top of the stack (o)
		space	tab	tab	 	output as character
		space	space	space	 	duplicate top of the stack (r)
		space	tab	tab	 	output as character
		space	space	space	 	duplicate top of the stack (l)
		space	tab	tab	 	output as character
		space	space	space	 	duplicate top of the stack (d)
		space	tab	tab	 	output as character
		space	space	tab	 	push newline character from earlier
		space	tab	tab	 	output as character
space	space	space	 	End Program


This piece of code is written in Whitespace, a programming language that only uses spaces, tabs, and linefeeds (newlines) as its commands.