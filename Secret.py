brainfuck
++[>++[>++[>++[>++[>++[>++[>++[>++[>++[>++[>++[>++[>++[<
]<]<]<]<]<]<]<]<]<]<]<]<] # Initialize memory cells
>++++[>++++<-]>  # Prepare value 16 in cell
>[>++++++[>++<-]>  # Prepare value 1,024 in cell
++++++[<<]]>  # Move to next value
>[>++++++[>++<-]>[>++++++[>++<-]>  # Prepare value 1,024 in cell
++++++[<<]]>  # Move to next value
>[>++++++[>++<-]>[>++++++[>++<-]>[>++++++[>++<-]>  # Prepare value 1,024 in cell
++++++[<<]]>]! # Output ASCII character for "H"
++[<++>-]  # Increment next cell
>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>  # Move to next value
>[>++++++[>++<-]>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>]! # Output ASCII character for "e"
++[<++>-]  # Increment next cell
>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>  # Move to next value
>[>++++++[>++<-]>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>]! # Output ASCII character for "l"
++[<++>-]  # Increment next cell
>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>  # Move to next value
>[>++++++[>++<-]>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>]! # Output ASCII character for "l"
++[<++>-]  # Increment next cell
>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>  # Move to next value
>[>++++++[>++<-]>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>]! # Output ASCII character for "o"
++[<++>-]  # Increment next cell

# Space
>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>  # Move to next value
>[>++++++[>++<-]>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>]! # Output ASCII character for space

# World
++[<++>-]  # Increment next cell
>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>  # Move to next value
>[>++++++[>++<-]>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>]! # Output ASCII character for "W"
++[<++>-]  # Increment next cell
>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>  # Move to next value
>[>++++++[>++<-]>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>]! # Output ASCII character for "o"
++[<++>-]  # Increment next cell
>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>  # Move to next value
>[>++++++[>++<-]>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>]! # Output ASCII character for "r"
++[<++>-]  # Increment next cell
>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>  # Move to next value
>[>++++++[>++<-]>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>]! # Output ASCII character for "l"
++[<++>-]  # Increment next cell
>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>  # Move to next value
>[>++++++[>++<-]>[>++++++[>++<-]>[>++++++[>++<-]>++++++[<<]]>]! # Output ASCII character for "d"
++[<++>-]  # Increment next cell
