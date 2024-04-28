// Importing header for console input/output.
#include <stdio.h>

// Function prototype for printing "Hello World" in a fancy way.
void printHelloWorld();

// Entry point of the program.
int main() {
    printHelloWorld();  // Calling the function to print "Hello World".
    return 0;
}

// Definition of printHelloWorld function.
void printHelloWorld() {
    // Using an array of characters to store the message "Hello World".
    char message[12] = "Hello World";

    // Enhanced visualization: printing each character on a new line with a delay.
    for (int i = 0; message[i] != '\0'; i++) { // Loop until the end of the string.
        printf("%c", message[i]); // Print one character at a time.
        printf("\n"); // Move to the next line.
        
        // Implementing a simple delay (platform-dependent).
        for (long j = 0; j < 100000000; j++) {
            // Delay loop does nothing but consume time.
        }
    }

    // Concluding the function with a simple call to print a new line.
    printf("\n");
}