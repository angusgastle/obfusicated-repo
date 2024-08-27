(* OCaml program to output "Hello World" in a roundabout way *)

(* Define a recursive function to generate the characters of "Hello World" one by one *)
let rec generate_string idx acc =
    let obscure_string = "H,e,l,l,o, ,W,o,r,l,d" in
    if idx = String.length obscure_string then acc
    else
        let char_added = if obscure_string.[idx] = ',' then "" else String.make 1 obscure_string.[idx] in
        generate_string (idx + 1) (acc ^ char_added)

(* Wrapper function to start the generation process *)
let get_hello_world () =
    generate_string 0 ""

(* Print the resulting string *)
let () = print_endline (get_hello_world ())