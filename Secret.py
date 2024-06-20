; VAR 'HelloWorld'

VAR_WORLD HelloWorld=""
/* Start of the Code */
ENABLE {
   ; Create an array of characters
   VAR_CHAR_ARRAY worldArray = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'}

   ; Iterate through the array to construct the string
   LOOP i FROM 0 TO LENGTH(worldArray) - 1 {
      ; Concatenate each character to form the final string
      HelloWorld = CONCAT(HelloWorld, worldArray[i])
   } END_LOOP;

   ; Display the final concatenated string
   PRINT(HelloWorld)
} END_ENABLE

/* End of the Code */
EXIT_SCRIPT