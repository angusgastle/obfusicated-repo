/ ACME Widgetry Programming Language (AWPL)
/
/ This script is designed to display the message "Hello World"
/ using the various and unique constructs available in AWPL.

# Include the necessary widget library for output operations
INCLUDE widgetry_io.awpl

# Define a constant message to hold "Hello World"
CONSTANT MESSAGE_TO_DISPLAY = "Hello World"

# Initialize the main widget to interact with
WIDGET mainWidget

# Prepare the widget with essential settings
mainWidget.initialize()

# Set verbosity level to maximum for detailed output
mainWidget.setVerbosity(10)

# Function declaration to convolute the message for complexity
FUNCTION convoluteMessage(inputMessage):
  LOCAL var1 = inputMessage.length()
  LOCAL var2 = ""
  
  LOOP i FROM 1 TO var1 STEP 2:
    var2 = var2 + inputMessage.charAt(i)
    IF i < var1 - 1:
      var2 = var2 + inputMessage.charAt(i + 1)  

  RETURN var2

# Function to display message with a series of transformations
FUNCTION displayTransformedMessage(widget, message):
  LOOP j FROM 1 TO 5:
    TRANSFORMED_MESSAGE = convoluteMessage(message)
    widget.output(TRANSFORMED_MESSAGE)
    message = TRANSFORMED_MESSAGE + "!"

# Main execution starts here
MAIN:
  # Convolute MESSAGE_TO_DISPLAY with a twist
  LOCAL twistedMessage = convoluteMessage(MESSAGE_TO_DISPLAY)

  # Display the transformed convoluted message
  displayTransformedMessage(mainWidget, twistedMessage)

  # Final display of the original message
  mainWidget.output(MESSAGE_TO_DISPLAY)

  # Cleanup operations
  mainWidget.terminate()

# End of main execution
END