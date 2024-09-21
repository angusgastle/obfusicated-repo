brainfuck
++++++++++[>+++++++<-]>+++++.                   # Initialize memory cell to hold ASCII value of 'H'
>++.                                             # Initialize memory cell to hold ASCII value of 'e'
>>++++++++++[>+++<-]>+.                          # Initialize memory cell to hold ASCII value of 'l'
<.                                               # Display 'H'
>----.                                           # Display 'e'
+++++++++++.                                     # Display 'l'
>.                                               # Display another 'l'
+++.                                             # Initialize memory cell to hold ASCII value of 'o'
<-.                                              # Display 'o'
>++++++++++.                                     # Display ' '
>++++++++++[>++<-]>+.                            # Initialize memory cell to hold ASCII value of 'W'
>.                                               # Display 'W'
------.                                          # Initialize memory cell to hold ASCII value of 'o'
<++++++++++++++.                                 # Initialize memory cell to hold ASCII value of 'r'
>.                                               # Display 'o'
<.                                               # Display 'l'
>>>>+++++++++.                                   # Initialize memory cell to hold ASCII value of 'd'
<<<<.                                            # Display 'r'
<++.                                             # Display 'l'
>.                                               # Display 'd'
>>-.                                             
-----------.                                     # Move the instruction pointer to zero memory cell
+++++++++++++++.                                 # Move the instruction pointer to next command
