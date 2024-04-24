prolog
% Prolog isn't typically used for simple I/O tasks, making this example inherently "obscure" in usage.
% This Prolog program will display "Hello World" once you consult the file and run the hello_world predicate.

% Predicate to initialize the program
start :-
    format('Starting the program...~n', []),
    init_hello_world.

% Predicate to prepare greeting message
init_hello_world :-
    create_message("Hello", "World", Message),
    display_message(Message).

% Predicate to combine parts of the greeting into a single string
create_message(PartOne, PartTwo, Message) :-
    string_concat(PartOne, " ", TempMessage),
    string_concat(TempMessage, PartTwo, Message).

% Predicate to print the final message
display_message(Message) :-
    format('Your message: "', []),
    format(Message, []),
    format('"~n', []),
    format('Program finished.~n', []).

% Entry point for the Prolog interpreter
hello_world :-
    start.

% To run this script, consult the file in your Prolog environment and execute the predicate:
% ?- hello_world.
