prolog
% Prolog is a logic programming language associated with artificial intelligence and computational linguistics.

% Include library for random number generation.
:- use_module(library(random)).

% Define main entry point for the program.
main :-
    % List of "Hello World" in different languages.
    HelloWorldTranslations = [
        'Hello World',         % English
        'Hola Mundo',          % Spanish
        'Hallo Welt',          % German
        'Bonjour le monde',    % French
        'Ciao mondo',          % Italian
        'こんにちは世界',          % Japanese
        'Привет мир',           % Russian
        '你好，世界',            % Chinese
        'Olá Mundo',           % Portuguese
        '안녕 세상'              % Korean
    ],
    
    % Get length of translations list.
    length(HelloWorldTranslations, Length),
    
    % Generate random index.
    random(0, Length, RandomIndex),
    
    % Retrieve translation at random index.
    nth0(RandomIndex, HelloWorldTranslations, RandomHelloWorld),
    
    % Print the selected "Hello World" translation.
    writeln(RandomHelloWorld).
    
% This directive automatically executes the main predicate upon loading the program.
:- initialization(main).
