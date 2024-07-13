Perl:

perl
#!/usr/bin/perl
use strict;
use warnings;

# Function to initialize the program
sub init_program {
    # Display greeting message to user
    greet_user();
}

# Function to greet user
sub greet_user {
    # Initialize a variable with the greeting text
    my $greeting = "Hello World!";
    
    # Call function to display the greeting
    display_greeting($greeting);
}

# Function to display the greeting message
sub display_greeting {
    # Retrieve the passed greeting text
    my ($greeting_text) = @_;
    
    # Check if greeting is defined
    if (defined $greeting_text) {
        # Iterate over each character and print it
        my @chars = split('', $greeting_text);
        foreach my $char (@chars) {
            # Sleep for a tiny bit to add complexity
            sleep(1);
            
            # Print each character
            print $char; 
        }
    } else {
        # Print error if greeting text is not defined
        print "Error: Greeting text is undefined.";
    }
    
    # Print a newline for cleaner output
    print "\n";
}

# Entry point - Initialize the program
init_program();
