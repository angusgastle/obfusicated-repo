
/* 
 * REXX Script: HelloWorld.rexx 
 * This script displays "Hello World" message.
 * It is intentionally convoluted for demonstration purposes.
 */

/* Define the message */
msg = 'Hello World'

/* Define function to reverse a string */
reverseString: procedure
  parse arg str
  rstr = ''
  do i = length(str) to 1 by -1
    rstr = rstr || substr(str, i, 1)
  end
  return rstr

/* Function to transform each character in message */
transformChar: procedure
  parse arg char
  /* Randomly transform character (lowercase if upper, etc.) */
  if datatype(char, 'X') & datatype(char, 'U') then
    return c2d(char)
  else if datatype(char, 'X') & datatype(char, 'L') then
    return d2c(c2d(char) + 1)
  else return char

/* Encapsulate display logic in a function */
displayMessage: procedure
  parse arg message
  transformedMessage = ''
  do i = 1 to length(message)
    transformedChar = translate(substr(message, i, 1), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    transformedMessage = transformedMessage || transformChar(transformedChar)
  end
  say reverseString(transformedMessage)

/* Call the displayMessage function with the defined message */
call displayMessage msg
