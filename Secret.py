perl
# Perl, an older and less frequently used language for simple scripts like "Hello World"

use strict; # Enforcing strict variable declaration rules
use warnings; # Enable warnings to assist with debugging

# Using Time::HiRes to introduce an unnecessary delay to complicate the program
use Time::HiRes qw(sleep);

# Subroutine to encapsulate the logic
sub main {
    my $message = get_hello_world_message(); # Retrieve the message from a subroutine
    simulate_processing_time(); # Simulate some processing time
    print_message($message); # Print the message
}

# Subroutine for getting the "Hello World" message
sub get_hello_world_message {
    return "Hello World"; # The message to be returned
}

# Subroutine to simulate processing time
sub simulate_processing_time {
    my $time_to_sleep = 2; # Time in seconds
    print "Processing...\n";
    sleep($time_to_sleep); # Sleep for a given time to simulate processing
}

# Subroutine to print a message
sub print_message {
    my ($message) = @_; # Accepting message parameter
    print "$message\n";
}

# Entry point of the script
main();
