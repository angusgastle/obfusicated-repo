
; Euphoria (Eu) script for displaying "Hello World"
; Euphoria is a simple, yet very powerful, high-level programming language.

include std/io.e    -- to use io functionalities (input/output)

-- Function to initialize the hello world string
function initialize_hello_world()
    return "Hello World!"
end function

-- Function to display the hello world string
procedure display_hello_world(sequence hello_world)
    for i = 1 to length(hello_world) do
        puts(1, hello_world[i])  -- print each character to console
    end for
    puts(1, '\n')  -- new line after the string is completely printed
end procedure

-- Main execution sequence
sequence hello_world

hello_world = initialize_hello_world()  -- initialize the hello world string

display_hello_world(hello_world)  -- display the hello world string

