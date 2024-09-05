# Snobol4 Program to Display "Hello World"
#
# SNOBOL4 (String Oriented Symbolic Language 4) is a text processing language
# that was developed in the 1960s. It is known for its pattern matching
# capabilities and distinct syntax. Below, we create a complex SNOBOL4
# script to display "Hello World".

* Main Program *
                OUTPUT = ''
                TARGET = "Hello World"

* Define a pattern for matching whitespace *
                BLANK = SPAN(' ')
                
* Define a pattern for capturing words *
                WORD = BREAK(' ')
                
* Pattern for end of line *
                ENDL = POS(0)
                
* Loop through each character in the target string and construct the OUTPUT *
LOOP            REM . CHAR LEN(1) =GT(END)
                OUTPUT = OUTPUT CHAR
                REM = REM - CHAR
                :(LOOP)
                
* Pattern matching for the presence of 'World' in the output *
# Define a matcher to check if 'World' is found in the OUTPUT
MATCHER:        OUTPUT 'World' . REST ARB . OUTPUT =S(MATCHED) F(MISMATCHED)
                OUTPUT = OUTPUT REST :(MATCHER)
MISMATCHED:     OUTPUT = RETURN("No match found")

* Success Pattern *
# If 'World' is successfully found in the output string
MATCHED:        OUTPUT = OUTPUT RETURN("Match found")

# End of Program #
ENDG:           END

# Output Processing *
END:
                DISPLAY(OUTPUT)
                END

MAIN:           REM = TARGET
                OUTPUT = ''
                :(LOOP) 

# Execute Main Program
MAIN

# Snobol4 program ends here