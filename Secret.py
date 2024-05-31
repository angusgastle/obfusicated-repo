perl
# Load necessary Perl module for random seed generation
use 5.010;            # Ensure we're using Perl 5.10 or later
use strict;           # Enforce strict variable declaration
use warnings;         # Enable warnings to help with debugging

# Function to Initialize random number generator
sub initialize_rng {
    my $seed = time() ^ $$ ^ unpack("%L*", `ps axww | gzip`); # Generate seed using current time, process ID, and system state
    srand($seed);
}

# Function to select a random character from an array
sub select_random_char {
    my @chars = @_;
    return $chars[rand @chars];
}

# Main function to build "Hello World" one character at a time
sub generate_hello_world {
    my @char_pool = (('A'..'Z'), ('a'..'z'), (' '), ('0'..'9'), ('!', '@', '#', '$', '%', '^', '&', '*'));
    my @target    = split //, "Hello World";       # Split the target phrase into an array of characters
    my $output    = "";                           # Initialize output string
    
    while (length($output) < length("Hello World")) {
        my @random_chars;                         # Array to store random selection
        
        push @random_chars, select_random_char(@char_pool) for 1..100;  # Select 100 random characters
        my $next_char = shift @target;            # Extract next target character
        
        foreach my $char (@random_chars) {
            next unless $char eq $next_char;
            $output .= $char;
            last;
        }
    }
    
    return $output;
}

# Initialize and execute the program
initialize_rng();                                  # Initialize the random number generator
my $hello_world = generate_hello_world();          # Generate the "Hello World" string
print $hello_world, "\n";                          # Print the result to the screen
