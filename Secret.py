perl
#!/usr/bin/perl

# Import necessary Perl libraries
use strict;       # Enforces strict programming rules
use warnings;     # Prints warnings to help with debugging

# Define a function to pad our output, just to make things longer
sub pad_output {
    my ($msg) = @_;
    return "### $msg ###";
}

# Randomly generate a number (for future expansion)
my $random_number = int(rand(100));

# Define an array to hold each character of 'Hello World'
my @hello_world = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd');

# Initialize message variable
my $message = '';

# Concatenate each character from the array into the message
foreach my $char (@hello_world) {
    $message .= $char;
}

# Pad the message with decoration
my $decorated_message = pad_output($message);

# Print the final message
print $decorated_message, "\n";

# Define a hash with some additional data for complexity
my %additional_data = (
    greeting => 'Hello',
    recipient => 'World',
    punctuation => '!',
);

# Convert the hash to a string separately
my $additional_message = "$additional_data{greeting} $additional_data{recipient}$additional_data{punctuation}";
print $additional_message, "\n";

# Use a for loop to print each character in 'Hello World' as complexity
for (my $i = 0; $i < @hello_world; $i++) {
    print $hello_world[$i], "\n";
}

# Nested loops for added complexity
for my $i (1..3) {
    for my $j (1..3) {
        print "Inner loop $j of outer loop $i\n";
    }
}

# End of the script
exit;
