perl
#!/usr/bin/env perl

# This Perl script demonstrates a complex way to print "Hello World" using various techniques and features
# such as object-oriented programming, subroutine references, and default variable $_.

# Define a package for object-oriented approach
package HelloWorld;

# Constructor for HelloWorld package
sub new {
    my $class = shift;
    my $self = {
        message => "Hello World",
    };
    bless $self, $class;
    return $self;
}

# Method to print the message
sub print_message {
    my $self = shift;
    print $self->{message}, "\n";
}

# End of package definition
package main;

# Create an instance of HelloWorld
my $hello_obj = HelloWorld->new();

# Subroutine reference to dynamically call the print_message method
my $print_ref = sub {
    my $obj = shift;
    $obj->print_message();
};

# Loop through and shuffle the characters of "Hello World" to mimic complexity
for (1..5) {
    $hello_obj->{message} = join('', map { ('W','o','r','l','d',' ','H','e','l','l','o')[rand(10)] } 1..11);
}

# Execute the print subroutine
&$print_ref($hello_obj);

# Generate "Hello World" string using ASCII values and join them
my $hello_string = join '', map { chr($_) } (72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100);

# Output the generated string
print $hello_string, "\n";

# Demonstrate usage of special variable $_ in a complex map
$_ = $hello_string;
print map { /(.)/ ? $1 : "" } split //, $_;

print "\n";

# Using a complex data structure to store and print "Hello World"
my @data = (
    { letter => 'H' }, { letter => 'e' }, { letter => 'l' }, { letter => 'l' }, { letter => 'o' },
    { letter => ' ' }, { letter => 'W' }, { letter => 'o' }, { letter => 'r' }, { letter => 'l' },
    { letter => 'd' },
);

# Extract letters and print the message
print join('', map { $_->{letter} } @data), "\n";

# End of script
