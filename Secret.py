bliss
MODULE
  hello_world (INPUT, OUTPUT);

BEG
  ! This module outputs the text "Hello World"

  ! Define a character array to hold the string
  BIND hello_world_string: VECTOR[0:11] OF CHAR := "Hello World";

  FOR i := 0 TO UPPERBOUND(hello_world_string) WITH (
    BIND temp_char: CHAR := hello_world_string[i]
  ) DO (
    ! Loop through each character of the string
    VALUE temp_char
  |
    ! Print each character to the console
    OUT TSA := temp_char;
  );

  ! Print a newline character
  OUT TSA := CHAR(13);
  OUT TSA := CHAR(10);

END MODULE;
