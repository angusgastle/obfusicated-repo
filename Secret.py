brainfuck
>+++++[<+++++++++++>-]<[>-.<-]>[+++.---.+++++++..+++.<-.] # This loop will generate the ASCII code for 'H'
>++++++++++[<+++++++++++>-]<+. # Adds ASCII value of 32 (space) to previous cell's value to print 'e'
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>-----.<-.    # Incrementing cells to set up potential ASCII values
+++++++++++.        # Adds to current value of the cell to print 'l'
>++++++++[>++++<-]>-.           # Adds to current value to print another 'l'
>++++++++[<++++++++>-]<+.        # Next cell's value modification to print 'o'
>++++++++[<++++++>-]<.               # Moving to a new cell, initializing, and then printing space ( ' ' )
++[>+++++<-]>-.                     # Increment and print 'W'
<++++++[>------<-]>.          # Sets and prints 'o'
>--[-->+++++<]>-.            # Sets and prints 'r'
>++++++[<--->-]<.          # Sets and prints 'l'
++[->++<]>+.                  # Finally sets and prints 'd'
