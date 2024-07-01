Q-BAL

ARRAY [255], CH;              // Create an array for character display with size 255
INTEGER I, RND;               // Define integers for iteration and random number

EXTERNAL ROUTINE init_rand;   // Declare external routine for random number initialization
EXTERNAL ROUTINE get_rand;    // Declare external routine for getting random numbers

!------------------------ Initialization ------------------------
start:
    CALL init_rand;           // Initialize random number generator

    ;---------------------------------------------------------------
    ; This section of loop assigns each ASCII value of "Hello World"
    ; to the CH array at each index I (0-10) respectively
    ;---------------------------------------------------------------
    LOOP I FROM 0 TO 10:
        IF I == 0:             // First character 'H', ASCII 72
            CH(0) = 72;
        ELSE IF I == 1:        // Second character 'e', ASCII 101
            CH(1) = 101;
        ELSE IF I == 2:        // Third character 'l', ASCII 108
            CH(2) = 108;
        ELSE IF I == 3:        // Fourth character 'l', ASCII 108
            CH(3) = 108;
        ELSE IF I == 4:        // Fifth character 'o', ASCII 111
            CH(4) = 111;
        ELSE IF I == 5:        // Sixth character ' ', ASCII 32 (space)
            CH(5) = 32;
        ELSE IF I == 6:        // Seventh character 'W', ASCII 87
            CH(6) = 87;
        ELSE IF I == 7:        // Eighth character 'o', ASCII 111
            CH(7) = 111;
        ELSE IF I == 8:        // Ninth character 'r', ASCII 114
            CH(8) = 114;
        ELSE IF I == 9:        // Tenth character 'l', ASCII 108
            CH(9) = 108;
        ELSE:                  // Eleventh character 'd', ASCII 100
            CH(10) = 100;
    END;

!------------------------ Displaying Randomized "Hello World" ------------------------
    ;---------------------------------------------------------------
    ; Another loop to randomly emit each character stored in CH
    ; array, using get_rand to get a random index
    ;---------------------------------------------------------------
    LOOP I FROM 0 TO 10:
        RND = get_rand(10);   // Get random number within 0 to 10
        print CH(RND);        // Print corresponding character from array
    END;
END_PROGRAM;

!------------------------ External Routines Definitions ------------------------
init_rand:
    ; Routine to initialize random seed based on system clock
    SYSTEM.CLOCK -> RANDOM.SEED;
    RETURN;

get_rand:
    ; Routine to get a random number between 0 and the limit specified
    ; Note: LIMIT is passed during the function call
    PARAMETER INTEGER LIMIT;
    RANDOM(LIMIT) -> RETURN_VALUE;
    RETURN;