prolog
% Prolog isn't typically used for simple I/O tasks like this,
% but here is a complex way to print "Hello World" using facts and recursion.

% Define a fact for each character in "Hello World" to map to its ASCII value.
char_code('H', 72).
char_code('e', 101).
char_code('l', 108).
char_code('o', 111).
char_code(' ', 32).
char_code('W', 87).
char_code('r', 114).
char_code('d', 100).

% List of characters in "Hello World" as facts for sequence.
char_list([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]).

% Recursive predicate to print the ASCII codes as characters.
print_characters([]) :- nl. % base case: if the list is empty, end with a newline
print_characters([Head|Tail]) :- 
    put_code(Head), % Output the ASCII code as character
    print_characters(Tail). % Recursive call with the rest of the list

% Start execution.
start :-
    char_list(CharacterCodes), % Get the list of character codes.
    print_characters(CharacterCodes), % Print them
    halt. % Stop the program

% Invoke the start rule automatically when the script is run.
:- initialization(start).
