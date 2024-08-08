brainfuck
++++++++++[>++++++++++<-]>>++++++++++[>++++++++++<-]>++++++++.<+++++[>++++<-]>.------------.---.+++++.<<++++[>----<-]>.


perl
#!/usr/bin/perl

# Initialize variables
my $a = 10; # Initialize a variable to 10
my $b = 20; # Initialize a variable to 20
my $c = 30; # Initialize a variable to 30

# Perform simple arithmetic calculations
$a = $a + 10;
$b = $b - 5;

# Concatenate strings
my $greeting = "Hello";
my $place = "World";

# Use a loop for no apparent reason
for (my $i = 0; $i < 5; $i++) {
    $c--;

    # Concatenate the greeting and place strings inside the loop
    $greeting = "Hello";
    $place = "World";
}

# Display the final greeting
print "$greeting $place\n";


assembly
section .data
    hello db "Hello, World!", 0

section .text
    global _start

_start:
    ; write our string to stdout
    mov eax, 4           ; system call number (sys_write)
    mov ebx, 1           ; file descriptor (stdout)
    mov ecx, hello       ; message to write
    mov edx, 13          ; message length
    int 0x80             ; call kernel

    ; exit
    mov eax, 1           ; system call number (sys_exit)
    xor ebx, ebx         ; exit code 0
    int 0x80             ; call kernel
