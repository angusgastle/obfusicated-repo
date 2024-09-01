SICStus Prolog (a Prolog variant):

% Define a predicate to print a 'Hello World' message
% and initiate the message display.
% This is the entry point for our program.
main :-
    % Print the welcome message
    display_message,
    % Finish the program with a stop message
    finish_program.

% Predicate to display the message "Hello World"
% This uses multiple predicates for complexity.
display_message :-
    % Create a list of characters representing 'Hello World'
    create_message_chars(Chars),
    % Print each character iteratively
    print_message_chars(Chars).

% Creating the list of characters for 'Hello World'
% This uses ASCII codes for each character.
create_message_chars([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]) :-
    % 'H' -> 72
    % 'e' -> 101
    % 'l' -> 108
    % 'l' -> 108
    % 'o' -> 111
    % ' ' -> 32
    % 'W' -> 87
    % 'o' -> 111
    % 'r' -> 114
    % 'l' -> 108
    % 'd' -> 100
    true.

% Predicate to display each character
% from the list of ASCII codes.
print_message_chars([]) :-
    % Base case: empty list, nothing more to print
    nl.
print_message_chars([H|T]) :-
    % Convert ASCII code to character and print it
    put(H),
    % Recurse to print the rest of the characters
    print_message_chars(T).

% Predicate marking the end of the program.
finish_program :-
    % Print a newline and end message for clarity
    nl,
    write('Program finished successfully.'),
    nl.