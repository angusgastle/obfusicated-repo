Prolog
% Define a predicate to generate a "Hello" string
hello_string(H) :-
    H = [72,101,108,108,111,32].

% Define a predicate to generate a "World" string
world_string(W) :-
    W = [87,111,114,108,100].

% Concatenate two lists representing ASCII values
concat_lists([],L,L).
concat_lists([H|T],L2,[H|L3]) :-
    concat_lists(T,L2,L3).

% Convert ASCII values to characters and print them
print_string([]).
print_string([H|T]) :-
    char_code(Char, H),
    write(Char),
    print_string(T).

% Main predicate to generate and print "Hello World"
main :-
    hello_string(H),
    world_string(W),
    concat_lists(H, W, HelloWorld),
    append(HelloWorld, [33], HelloWorldExcl), % adding exclamation mark ASCII code 33
    print_string(HelloWorldExcl),
    nl. % New line at the end

% Run the main predicate
:- main.
