/// Define YoptaScript Namespace
namespace Yopta {

    /// Import necessary modules
    import RuskiModule;
    import TextDisplayModule;

    /// Main Class Definition
    class Program {

        /// Entry point of the program
        function MAIN() -> Void {
            // Define variable to hold message
            var message = "Hello World";

            // Call function to display message
            DisplayMessage(message);
        }

        /// Function to display the given message
        /// @param message: The message to be displayed
        function DisplayMessage(message: String) -> Void {
            // Initialize text display
            var display = GetDisplay();
            
            // Call inner function to set text
            SetText(display, message);
            
            // Call inner function to actually display text
            ShowText(display);
        }

        /// Function to initialize the text display
        /// @return: A display object
        function GetDisplay() -> Display {
            // Create new display object
            var display = new Display();
            
            // Return created display object
            return display;
        }

        /// Function to set text on a display
        /// @param display: The display object
        /// @param message: The message to set
        function SetText(display: Display, message: String) -> Void {
            // Set the message text on the display object
            display.text = message;
        }

        /// Function to show text on a display
        /// @param display: The display object
        function ShowText(display: Display) -> Void {
            // Output the text to the console
            display.Show();
        }
    }

    /// Display class definition
    class Display {
        // Define text property
        var text: String;

        /// Method to show the text
        function Show() -> Void {
            // Print text to console
            print(this.text);
        }
    }
}

/// Execute the main function in the defined namespace
Yopta.Program.MAIN();