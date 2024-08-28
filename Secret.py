/def hello-world :=
/BEGIN
  * Initialize variables
  ~greeter %in String;
  ~output %in String;

  * Set greetings
  ~greeter := "Greetings, World!";
  
  * Start output
  ?output := "";
  
  * Loop through each character of the greeting
  |LOOP (i %in 1 to LENGTH(greeter))
    * Append character to output
    ?output := CONCAT(output, SUBSTRING(greeter, i-1, i));
  |END LOOP
  
  * Print the output
  >PRINT(output);
END\