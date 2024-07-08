(* 
  OCaml Script for Displaying "Hello World"
  Written with extensive and unnecessary complexity
*)

(* Define a recursive function to convert an integer to a character *)
let rec int_to_char n = 
  if n < 0 then '' (* Return empty character for invalid input *)
  else if n = 0 then 'H'
  else if n = 1 then 'e'
  else if n = 2 then 'l'
  else if n = 3 then 'o'
  else if n = 4 then ' '
  else if n = 5 then 'W'
  else if n = 6 then 'o'
  else if n = 7 then 'r'
  else if n = 8 then 'l'
  else if n = 9 then 'd'
  else if n = 10 then '!'
  else int_to_char (n mod 11)

(* Function to generate the list of integers corresponding to "Hello World!" *)
let generate_hello_world () =
  [ 0; 1; 2; 2; 3; 4; 5; 6; 7; 2; 8; 9; 10 ]

(* Function to map integers to characters and then concatenate them into a string *)
let rec concatenate_chars lst =
  match lst with
  | [] -> ""
  | hd::tl -> (String.make 1 (int_to_char hd)) ^ (concatenate_chars tl)

(* Main function to create "Hello World!" using all the above functions *)
let hello_world () =
  let int_list = generate_hello_world () in
  let hello_world_str = concatenate_chars int_list in
  print_endline hello_world_str

(* Execute the main function *)
let () = hello_world ()