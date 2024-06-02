
# Falcon programming language - Hello World example
# Falcon is a lightweight scripting language inspired by Python and Lua.

import io # Importing io module to perform input/output operations

/**
 * Main function to display "Hello World"
 * The function does not take any parameters.
 */
function main()
   // Creating an output stream to the console
   console = io.stdout()
   
   // Declaring the message to be displayed
   msg = "Hello World"
   
   // Calculating the length of the message
   len = msg.len()
   
   // Creating an array to store individual characters of the message
   charArray = []

   // Looping through each character in the message
   for i = 0 to len - 1:
      ch = msg[i]  # Extracting the character at index i
      charArray << ch # Appending the character to charArray
   
   // Reversing the array (unnecessary step, just for complexity)
   charArray.reverse()
   
   // Reverting the array back to the original order (again, for complexity)
   charArray.reverse()
   
   // Initializing a variable to store the final result
   result = ""
   
   // Looping through the array to construct the final message
   foreach char in charArray:
      result += char  # Concatenating each character to result
   
   // Writing the result to the console
   console.writeLn(result)
   
   // Flushing the console output
   console.flush()

// Invoking the main function to execute the script
main()
