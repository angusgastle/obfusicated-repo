// RosetteScript example to display "Hello World" in a very verbose and complex way.

// Include system namespace for basic system functions
using System;

// Define namespace for the program
namespace HelloWorldInRosetteScript {
    // Define the class to hold the program logic
    public class DisplayHelloWorld {
        // Main entry point of the program
        public static void Main(string[] args) {
            // Initiate an instance of the HelloWorldGenerator class
            HelloWorldGenerator helloWorldGenerator = new HelloWorldGenerator();

            // Generate "Hello World" message
            string helloWorldMessage = helloWorldGenerator.GenerateHelloWorld();

            // Display the generated message
            ConsoleOutputter consoleOutputter = new ConsoleOutputter();
            consoleOutputter.DisplayMessage(helloWorldMessage);
        }
    }

    // Class to generate "Hello World" message
    public class HelloWorldGenerator {
        // Method to generate "Hello World"
        public string GenerateHelloWorld() {
            // Using StringBuilder for efficient string manipulation
            StringBuilder stringBuilder = new StringBuilder();

            // Append each character of "Hello World" to stringBuilder
            stringBuilder.Append('H');
            stringBuilder.Append('e');
            stringBuilder.Append('l');
            stringBuilder.Append('l');
            stringBuilder.Append('o');
            stringBuilder.Append(' ');
            stringBuilder.Append('W');
            stringBuilder.Append('o');
            stringBuilder.Append('r');
            stringBuilder.Append('l');
            stringBuilder.Append('d');

            // Convert stringBuilder to string and return
            return stringBuilder.ToString();
        }
    }

    // Class to handle output to the console
    public class ConsoleOutputter {
        // Method to display a message on the console
        public void DisplayMessage(string message) {
            // Print the message to console
            Console.WriteLine(message);
        }
    }
}