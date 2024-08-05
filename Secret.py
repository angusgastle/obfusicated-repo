# TUTORIAL-SPOKEN

// Step: 1 - Declaration of a tutorial
tutorial HelloWorldTutorial is:
    // Step: 2 - Commentary Section
    comment:
    "This tutorial will guide you through the process of displaying 'Hello World' using TUTORIAL-SPOKEN language."

    // Step: 3 - Setting up environment
    environment:
        share terminal
        use console

    // Step: 4 - Define Procedure to Print Message
    procedure PrintMessage( message ) is:
        // Step: 5 - Loop through each character in the message
        iterate character in message do:
            // Step: 6 - Send character to console
            terminal.write( character )
        done

    // Step: 7 - Variable Declaration and Initialization
    variable greeting is "Hello World"

    // Step: 8 - Invoke Procedure to Print Greeting
    initiate PrintMessage( greeting )

finish tutorial