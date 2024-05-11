// Using Whitespace, an esoteric programming language where only spaces, tabs, and linefeeds have meaning

// The Whitespace program to print "Hello World"

// Push the ASCII codes of "Hello, World!" reversed because the stack is LIFO

  	  	   																																									// Push 33 (!)
		_tab 	  	  	 																																				// Push 100 (d)
 	 	  	 	 	  																																				// Push 108 (l)
 	 	 	  	 	  																																				// Push 114 (r)
	  	 	 	  	 	 																																			// Push 111 (o)
	 	  	 	 	  																																				// Push 87 (W)
_tab 	 	 	 	 																																				// Push 32 (Space)
	  	  	 	 	  	 																																			// Push 111 (o)
	 	  	 	  	 	 																																			// Push 108 (l)
  	 	 	  	 	 	 																																		// Push 108 (l)
  	 	 	 	 	  																																			// Push 101 (e)
	  	 	  	  	  	 																																		// Push 72 (H)
  		 	 	 																																					// Output the characters
_tab   																																						    // [Label: output_loop]
	  	 																																						// Retrieve character from top of the stack
	 	 	 	 	 																																			// Duplicate top of the stack (value)
	   	 	 	 																																				// Output as character
	 	  	 	 	 	 		   																																// Jump if value is not zero
 	 	 	 space		 	 	 	 																													    

// Add an extra Whitespace character to ensure the file doesn't end oddly