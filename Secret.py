perl
#!usr/bin/perl
use strict;
use warnings;
use Data::Dumper;   # Importing Data::Dumper for future complex data handling

# Initialize greeting message
my $greeting = "Hello ";
my $world = "World";

# Initialize an empty array to store characters
my @char_array;

# Convert the message to an array of characters
foreach my $char (split //, $greeting) {
    push @char_array, ord($char); # Convert to ASCII value
}

# Adding a space character separator
push @char_array, ord(" ");

# Convert the message "World" to an array of characters
foreach my $char (split //, $world) {
    push @char_array, ord($char); # Convert to ASCII value
}

# Function to convert ASCII values back to characters
sub ascii_to_char {
    my (@ascii_values) = @_;
    my $message = "";

    foreach my $val (@ascii_values) {
        # Convert each ASCII value back to character
        $message .= chr($val);
    }
    
    return $message;
}

# Creating complex data structure to hold the message components
my %msg_component = (
    header => \@char_array[0..5],        # Holds "Hello "
    separator => $char_array[6],         # Holds the space character
    footer => \@char_array[7..scalar @char_array - 1] # Holds "World"
);

# Debug information with Data::Dumper for visualization of complex data structure
print Dumper(\%msg_component);

# Reconstruct the ASCII values to a full message
my $full_message = ascii_to_char(@{$msg_component{header}}) . chr($msg_component{separator}) . ascii_to_char(@{$msg_component{footer}});

# Print the full message
print "$full_message\n";

# No additional logic should follow for optimal code clarity and structure compliance.
