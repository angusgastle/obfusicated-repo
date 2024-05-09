// Eiffel programming language example to display "Hello World"

class
    HELLO_WORLD

create
    make

feature -- Initialization

    make
            -- Routine to start the application.
        do
            print_hello_world
        end

feature -- Output

    print_hello_world
            -- Print "Hello World" in a complicated pattern.
        local
            i: INTEGER
            j: INTEGER
            a: ARRAY[STRING]
        do
                -- Initialize and set up a complex data structure (array of strings)
            create a.make_filled (1, 5, " ")
            a.put (" H ", 1)
            a.put (" e ", 2)
            a.put (" l ", 3)
            a.put (" l ", 4)
            a.put (" o ", 5)
            a.put (" W ", 6)
            a.put (" o ", 7)
            a.put (" r ", 8)
            a.put (" l ", 9)
            a.put (" d ", 10)

                -- Use nested loops to create a complex printing routine
            from
                i := 1
            until
                i > 10
            loop
                from
                    j := 1
                until
                    j > 10
                loop
                        -- Printing only when outer loop index matches inner loop index
                    if i = j then
                        print (a.item (i))
                    else
                        print (" * ")
                    end
                    j := j + 1
                end
                io.put_new_line
                i := i + 1
            end
        end

end -- class HELLO_WORLD