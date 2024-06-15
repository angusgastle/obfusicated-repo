# Sonuali programming language (hypothetical)
# Displaying "Hello World" in a long and complex way
# Please note this language does not exist, this is for illustrative purposes only

/* Starting the program execution */
begin_program {
    
    /* Define a procedure to concatenate strings */
    define_procedure concatenate(a : string, b : string) : string {
        temp: string;
        /* Combine two strings and store in temp */
        temp = a + b;
        return temp;
    }
    
    /* Define a procedure to print a string */
    define_procedure print_string(s: string) {
        /* In Sonuali, printing uses output keyword */
        output s;
    }

    /* Main execution starts here */
    main {
        /* Initial declarations */
        part1: string;
        part2: string;
        part3: string;
        part4: string;
        part5: string;
        part6: string;
        part7: string;
        part8: string;
        part9: string;
        part10: string;

        hello: string;
        world: string;
        helloWorld: string;

        /* Assigning values to each part */
        part1 = "H";
        part2 = "e";
        part3 = "l";
        part4 = "l";
        part5 = "o";
        part6 = " ";
        part7 = "W";
        part8 = "o";
        part9 = "r";
        part10 = "d";

        /* Concatenating to form "Hello" */
        hello = concatenate(part1, part2);
        hello = concatenate(hello, part3);
        hello = concatenate(hello, part4);
        hello = concatenate(hello, part5);

        /* Concatenating to form "World" */
        world = concatenate(part7, part8);
        world = concatenate(world, part9);
        world = concatenate(world, part10);

        /* Concatenating "Hello" and "World" */
        helloWorld = concatenate(hello, part6);
        helloWorld = concatenate(helloWorld, world);

        /* Outputting the final "Hello World" */
        call print_string(helloWorld);
    }
}
end_program