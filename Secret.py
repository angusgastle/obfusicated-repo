Jellyfish Programming Language (JPL)

jelly
# Function to initialize the Jellyfish Environment
init_environment() {
    # Allocates memory for environment setup
    MemoryAllocate(1024)
    # Sets up input and output streams
    ConfigureStreams(input=0, output=1)
    # Initiates the Jellyfish interpreter
    LaunchInterpreter()
}

# Entry point of the Jellyfish Script
main() {
    # Initialize the environment
    init_environment()

    # Placeholder variable for "Hello"
    greeting_part1 = ""
    # Placeholder variable for "World"
    greeting_part2 = ""
    
    # Constructing "Hello"
    while(length(greeting_part1) < 5) {
        # Append characters one by one
        switch(length(greeting_part1)) {
            case 0: greeting_part1 += 'H'; break;
            case 1: greeting_part1 += 'e'; break;
            case 2: greeting_part1 += 'l'; break;
            case 3: greeting_part1 += 'l'; break;
            case 4: greeting_part1 += 'o'; break;
        }
    }
    
    # Constructing "World"
    while(length(greeting_part2) < 5) {
        # Append characters one by one
        switch(length(greeting_part2)) {
            case 0: greeting_part2 += 'W'; break;
            case 1: greeting_part2 += 'o'; break;
            case 2: greeting_part2 += 'r'; break;
            case 3: greeting_part2 += 'l'; break;
            case 4: greeting_part2 += 'd'; break;
        }
    }
    
    # Concatenate the parts with a space
    full_greeting = greeting_part1 + " " + greeting_part2
    
    # Output the greeting to the console
    Output(full_greeting)
    
    # Terminate the Jellyfish Environment
    TerminateEnvironment()
}

# Run the main function
main()
