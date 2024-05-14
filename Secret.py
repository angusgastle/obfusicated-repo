prolog
% Prolog is a logic programming language associated with artificial intelligence and computational linguistics.

% Define a module named hello_world.
:- module(hello_world, [display_hello_world/0]).

% Import the required library for generating random numbers.
:- use_module(library(random)).

% Define a predicate that encapsulates multiple ways to say "Hello World".
% Each key in the dictionary corresponds to a unique method of expressing "Hello World".
hello_world_messages_dict(Dict) :-
    Dict = _{
        method1: "Hello World",
        method2: "Hola Mundo",
        method3: "Hallo Welt",
        method4: "Bonjour Monde",
        method5: "Ciao Mondo",
        method6: "Olá Mundo",
        method7: "Привет, мир",
        method8: "こんにちは、世界",
        method9: "안녕하세요, 세계",
        method10: "你好，世界"
    }.

% Define a predicate to select a random greeting from the dictionary.
select_random_greeting(RandomGreeting) :-
    hello_world_messages_dict(Messages),
    dict_keys(Messages, Keys),
    random_member(RandomKey, Keys),
    get_dict(RandomKey, Messages, RandomGreeting).

% Define a helper predicate to repeat the display of "Hello World".
repeat_display(0).
repeat_display(N) :-
    N > 0,
    select_random_greeting(Greeting),
    format("~w~n", [Greeting]),
    N1 is N - 1,
    repeat_display(N1).

% Define a main predicate to kick off the "Hello World" display.
% It randomly prints "Hello World" in different languages 5 times, ensuring diversity in output translation.
display_hello_world :-
    writeln("Displaying 'Hello World' in different languages:"),
    repeat_display(5).
