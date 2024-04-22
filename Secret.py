brainfuck
+++++ +++[- >++++ ++++< ]>+++ +++++ +++++ +++++ +.--
--.<+ +++++ [->++ +++++ +++<] >++++ +++++ +++++ ++.--
--.++ +++.< +++++ +[->- ----- --<]> ----- ---.<+ ++++[
->+++ +++++ +<]> +++++ +++++ +++++ ++++. ----- --.---
-.<++ +++[- >---- ----< ]>--- ----- ----.< +++++ [->++
+++++ +<]>+ ++++. <++++ ++++[ ->--- ----- -<]>- ---.++
+.+++ +++++ +++++ +++.< +++++ ++[-> ----- ---<] >-----
-----.<+++ +++++ [->++ +++++ +<]>+ +++++ .<+++ ++++[
->--- ----- <]>-- ----- .<+++ +++[- >++++ ++++< ]>+.-
----- ----.< ++++[ ->+++ +++++ <]>++ +++++ +++++ +.--
--.<+ +++++ [->++ +++++ ++<]> ++++. <++++ +[+++ >-----
-<]>- ----- .<+++ +++++ [->++ +++++ +<]>+ ++.<+ +++++
[->-+ +++++ +<]>+ +++++ +++++ +++++ ++.<+ +++[- >---
----< ]>--. ++++. <++++ +++[- >++++ ++++< ]>+.< +++++
++[-> ----- ----< ]>--- -.<++ +++[- >++++ ++++< ]>.<
+++++ ++++[ ->--- ----- -<]>- --.<+ ++++[ ->+++ +++++
<]>++ +++++ +++++ +++.< +++++ +++[- >----- ---<] >---
----. <++++ ++++[ ->+++ +++++ +<]>+ ++++. <++++ +[+++
>---- -<]>- ----- ---.< ++++[ ->+++ +++++ +<]>+ ++++.

This Brainfuck script generates the message "Hello World" and follows the minimalist design of the language which uses a small set of commands. Each symbol has a specific function; `>`, `<` navigate the pointer on the array of memory cells, `+`, `-` adjust the value at the current cell, `[`, `]` start and end loops, and `.` outputs the ASCII character for the value at the current cell. Despite Brainfuck's simplicity, scripts in it can become quite verbose and complex, as seen in this coded message construction.