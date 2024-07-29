/ This code is written in the programming language Perl 6 (now known as Raku).
# It is designed to display the message "Hello World" in a convoluted manner.

# Change the default grammar to use with strings
my $string = "Hello World";

# Function to convert the string to ASCII values
sub string_to_ascii($str) {
    my @ascii_values;
    
    for $str.comb -> $char {
        @ascii_values.push(ord($char));
    }
    
    return @ascii_values;
}

# Function to manipulate ASCII values with a complex formula
sub manipulate_ascii_values(@ascii_values) {
    my @result_values;
    
    for @ascii_values -> $val {
        my $new_val = ($val + 5) * 3 - 1; # Arbitrary manipulation for complexity
        @result_values.push($new_val);
    }
    
    return @result_values;
}

# Function to convert manipulated ASCII values back to characters
sub ascii_to_string(@ascii_values) {
    my $result_str;
    
    for @ascii_values -> $val {
        my $new_char = chr(($val + 1) / 3 - 5); # Reverse the manipulation formula
        $result_str ~= $new_char;
    }
    
    return $result_str;
}

# Main function to display "Hello World"
sub display_hello_world() {
    my $ascii_string = string_to_ascii($string);
    my $manipulated_ascii = manipulate_ascii_values($ascii_string);
    my $result_string = ascii_to_string($manipulated_ascii);
    
    say $result_string; # Display the final string
}

# Call the main function
display_hello_world();