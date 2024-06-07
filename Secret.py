# Oberon-07

MODULE HelloWorld;

  IMPORT Out;

  (* Main program block *)
  PROCEDURE Main;
  VAR
    i: INTEGER;
    charArray: ARRAY 11 OF CHAR;

  BEGIN
    (* Initialization of character array with the string "Hello World" *)
    charArray[0] := 'H';
    charArray[1] := 'e';
    charArray[2] := 'l';
    charArray[3] := 'l';
    charArray[4] := 'o';
    charArray[5] := ' ';
    charArray[6] := 'W';
    charArray[7] := 'o';
    charArray[8] := 'r';
    charArray[9] := 'l';
    charArray[10] := 'd';

    (* Loop through each character to display the string *)
    FOR i := 0 TO LEN(charArray)-1 DO
      Out.Char(charArray[i])
    END;
    
    (* Newline after the string display *)
    Out.Ln
  END Main;

BEGIN
  Main
END HelloWorld.