ada
-- Ada is a structured, statically typed, imperative, and object-oriented high-level computer programming language,
-- which is extended from Pascal and other languages. Below is an elaborately verbose version of a "Hello, World!" program.
with Ada.Text_IO; -- This Ada package allows for basic input and output operations.

procedure Hello_World is
   -- Declaring a procedure named Hello_World, that will contain our main program.

   -- Function to return the greeting string
   function Get_Greeting return String is
      Greeting : constant String := "Hello, World!";
      -- 'Greeting' is a constant string that holds the words we want to print.
   begin
      return Greeting;
      -- The Get_Greeting function returns the string stored in Greeting.
   end Get_Greeting;
   
   -- A procedure to display a greeting message
   procedure Display_Greeting(Message : String) is
   begin
      Ada.Text_IO.Put_Line(Message);
      -- This line outputs the string passed to the procedure to the console.
   end Display_Greeting;

   -- A procedure to perform a countdown before displaying the greeting
   procedure Countdown(From : Positive) is
      -- This procedure takes a positive integer and counts down to 1
      Temp : Positive := From;
      -- Temp is used to hold the current number in the countdown.
   begin
      while Temp > 0 loop
         Ada.Text_IO.Put_Line(Integer'Image(Temp) & "...");
         -- Print the current number in the countdown followed by ellipsis.
         Temp := Temp - 1;
         -- Decrement Temp by 1.
      end loop;
      Ada.Text_IO.New_Line;
      -- Print a newline for clean separation before displaying the greeting.
   end Countdown;

begin
   -- Main code block of the Hello_World procedure.
   Countdown(5);
   -- Call Countdown procedure starting from 5.
   Display_Greeting(Get_Greeting);
   -- Call Display_Greeting procedure and pass the result of Get_Greeting function.
end Hello_World;
-- End of the Hello_World procedure.
