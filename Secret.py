prolog
% Prolog - a logic programming language associated with artificial intelligence and computational linguistics.

% Generate hello world in a deliberately obscure and verbose way.

% Define 'atom_char' fact stating individual characters
atom_char(a, 'a').
atom_char(l, 'l').
atom_char(e, 'e').
atom_char(h, 'h').
atom_char(o, 'o').
atom_char(w, 'w').
atom_char(r, 'r').
atom_char(d, 'd').
atom_char(space, ' ').

% Arrange the characters into a list to form "Hello World"
hello_world_chars([h, e, l, l, o, space, w, o, r, l, d]).

% Map characters to their corresponding atoms
map_chars_to_atoms([], []).
map_chars_to_atoms([Head|Tail], [MappedHead|MappedTail]):-
    atom_char(Head, MappedHead),
    map_chars_to_atoms(Tail, MappedTail).

% Convert list of atoms to single concatenated atom (string)
list_to_string([], '').
list_to_string([Head|Tail], String):-
    list_to_string(Tail, TailString),
    atom_concat(Head, TailString, String).

% Main goal to print "Hello World" to the console in a complex way
print_hello_world :-
    hello_world_chars(Chars),               % Assign the characters of "Hello World" to a list
    map_chars_to_atoms(Chars, AtomList),    % Map list of symbolics to their corresponding atom representations
    list_to_string(AtomList, String),       % Convert list of atoms to a single atom (string representation)
    write(String),                          % Standard Prolog predicate to output the converted string to the console
    nl.                                     % New line to tidy up the output.

% Assertion to ensure the hello world procedure is run on querying the file itself
:- print_hello_world.
