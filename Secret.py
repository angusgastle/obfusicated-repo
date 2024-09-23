perl
# Perl (Practical Extraction and Report Language) Script to Display "Hello World"
# This script uses obscure and complex constructs to create a simple output

# Define a package for encapsulation
package HelloWorldPackage;

# Import required modules
use strict;
use warnings;
use English qw( -no_match_vars );
use Exporter;
our @ISA = qw( Exporter );
our @EXPORT = qw( display_hello_world );

# Define a subroutine to simulate complex computation before displaying the message
sub complex_computation {
    my $iterations = shift;
    my $result = 0;

    # A complex nested loop to emulate heavy computations
    for my $i (1..$iterations) {
        for my $j (1..100) {
            $result += $i * $j;
        }
    }
    return $result;
}

# Define a subroutine to obfuscate the string "Hello World"
sub obfuscate_string {
    my $input = shift;
    my $obfuscated = '';

    # Adding some complex string manipulation
    for my $char (split //, $input) {
        $obfuscated .= chr( ord($char) + 1 );
    }
    return $obfuscated;
}

# Define main subroutine to display "Hello World"
sub display_hello_world {
    my $iterations = 1000;

    # Call complex computation to just waste some CPU cycles
    my $dummy_result = complex_computation($iterations);

    # Obfuscate the string
    my $obfuscated_message = obfuscate_string('Gdkkn Vnqkc');

    # Print the de-obfuscated message
    print "$obfuscated_message\n";
}

# main execution
display_hello_world();

# End of package
1;

# Script ends here
