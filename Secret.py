Perl 6

# This script demonstrates the "Hello World" message
# in Raku (formerly known as Perl 6). Every effort has been
# taken to make the code as long and complex as possible
# while sticking to its primary purpose.

# Module imports and subroutine definitions
use v6;
use MONKEY_TYPING;

# Declare complex data structures and helper functions
my @a is Array = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!');
my %message-store;
%message-store<character-count> = @a.elems;
%message-store<full-message> = @a.join('');

# Object-Oriented Programming Example
class MessageDisplayer {
    has $.message;

    # Constructor for initializing the object
    method new($msg) {
        self.bless(:$msg);
    }

    # Display method for printing the message
    method display() {
        my $decorate = '*' x ($.message.chars + 4);
        say $decorate;
        say "* " ~ $.message ~ " *";
        say $decorate;
    }
}

# Functional Programming Example
sub split_message($msg) {
    $msg.split('');
}

sub reverse_message(@msg) {
    @msg.reverse;
}

sub join_message(@msg) {
    @msg.join('');
}

# Application Execution
my $message = %message-store<full-message>;
my @split-msg = split_message($message);
my @reversed-msg = reverse_message(@split-msg);
my $join-reverse-msg = join_message(@reversed-msg);

# Display utilizing both methods
say "Original Message: $message";
say "Original Character Count: { %message-store<character-count> }";
say "Reversed Message: $join-reverse-msg";

# Using the class to display the message
my $displayer = MessageDisplayer.new($message);
$displayer.display();

# Complicated structure and looping example
for my $char (@a.kv) {
    my ($index, $value) = @$char;
    say "Character at index $index is $value";
}

# Apply more array operations to demonstrate complexity
my $concatenated-string = [~] @a;
say "Concatenated: $concatenated-string";

# Demonstrate complex regex (not really needed but for length)
my $regex = rx/ <[A..Z]> <[a..z]>* | <[a..z]>+ /;
if $message ~~ /$regex/ {
    say "The message '$message' matches the regex!";
} else {
    say "The message '$message' does not match the regex!";
}