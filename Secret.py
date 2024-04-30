prolog
% Prolog is a logic programming language associated with artificial intelligence 
% and computational linguistics. Here, we implement a complex version of "Hello, World!".

% Predicate to print Hello, World!
print_hello_world :- 
    % Using format/2 to construct the output string
    format('Hello, World!~n').

% Complex predicate to decide what to do
% We are making this unnecessarily complex for the sake of the task.
decide_action(Action, Message) :- 
    % Multi-branch condition to handle different scenarios
    (   Action = say_hello -> print_hello_world;
        Action = log_hello -> writeln(Message);
        Action = complex_hello -> complex_hello_world_process;
        true -> writeln('No valid action provided')
    ).

% An unneeded complex process function to print Hello World
complex_hello_world_process :-
    % Drawing from multiple predicates to finally print Hello World
    create_hello(Hello),
    create_world(World),
    atom_concat(Hello, ', ', HelloComma),
    atom_concat(HelloComma, World, Greeting),
    writeln(Greeting).

% Helper predicate to construct "Hello"
create_hello(Hello) :-
    % Simply bind the atom 'Hello' to the passed variable
    Hello = 'Hello'.

% Helper predicate to construct "World"
create_world(World) :-
    % Simply bind the atom 'World' to the passed variable
    World = 'World'.

% Init predicate serves as the main entry point when running the script
init :-
    % More complex decision making, unnecessary for a simple print
    decide_action(say_hello, ''),
    decide_action(log_hello, 'Logging: Hello, World! Executed.'),
    decide_action(complex_hello, '').

% Ensure the init predicate is called automatically when the script is started
:- initialization(init).
