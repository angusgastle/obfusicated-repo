whitespace
	S S S		push "H" character (72)
	T	S S S	L	push 0 (final L sets the sign to positive)
	T	S T	S	S	multiply by 256 (prepare for next)
	S S T		push "e" character (101)
	T	T	S	S	add to previous result
	T	S T	S	S	multiply by 256 (prepare for next)
	S S L	S	push "l" character (108)
	T	T	S	S	add to previous result
	T	S T	S	S	multiply by 256 (prepare for next)
	S S L	S	push "l" character (108)
	T	T	S	S	add to previous result
	T	S T	S	S	multiply by 256 (prepare for next)
	S S T	T	push "o" character (111)
	T	T	S	S	add to previous result
	T	S T	S	S	multiply by 256 (prepare for next)
	S S S T	push space character (32)
	T	T	S	S	add to previous result
	T	S T	S	S	multiply by 256 (prepare for next)
	S S T	L	push "W" character (87)
	T	T	S	S	add to previous result
	T	S T	S	S	multiply by 256 (prepare for next)
	S S S T	push "o" character (111)
	T	T	S	S	add to previous result
	T	S T	S	S	multiply by 256 (prepare for next)
	S S L	T	push "r" character (114)
	T	T	S	S	add to previous result
	T	S T	S	S	multiply by 256 (prepare for next)
	S S S S	push "l" character (108)
	T	T	S	S	add to previous result
	T	S T	S	S	multiply by 256 (prepare for next)
	S S T	L	push "d" character (100)
	T	T	S	S	add to previous result
	
	N	S	T	T	output as character
	N	T	S	T	output as character
	N	T	S	T	output as character
	N	T	S	T	output as character
	N	T	S	T	output as character
	N	T	S	T	output as character
	N	T	S	T	output as character
	N	T	S	T	output as character
	N	T	S	T	output as character
	N	T	S	T	output as character
