Perl 6

perl6
# Define a class for our "Hello World" message
class HelloWorld {
    # Define an attribute to hold the message
    has Str $.message is rw;

    # Constructor to set the default message
    method new(Str $msg = "Hello World") {
        self.bless(:$msg);
    }

    # Method to display the message
    method display() {
        say $!message;
    }

    # Method to change the message
    method change-message(Str $new-msg) {
        $!message = $new-msg;
    }
}

# Define a role that can be mixed into our class
role Greeter {
    # Method to greet a user with a custom message
    method greet($name) {
        say "Hello, $name!";
    }
}

# Mix the role into our class
my class HelloGreeter is HelloWorld does Greeter {}

# Instantiate our class with the default message
my $hello = HelloGreeter.new;

# Display the default message
$hello.display();

# Change the message to a new one
$hello.change-message("Greetings, Universe!");

# Display the new message
$hello.display();

# Use the role to greet a user
$hello.greet("Alice");
