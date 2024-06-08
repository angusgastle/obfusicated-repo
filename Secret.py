brainfuck
+++++ +++++             initialize cell 0 to 10
[
    > +++++ ++          add  7 to cell 1
    > +++++ +++++       add 10 to cell 2
    > +++               add  3 to cell 3
    > +                 add  1 to cell 4
    <<<< -              decrement cell 0 by 1
]
> .                     cell 1 (H) output "H"
> + .                   cell 2 (e) increment cell 2 from 10 to 11 and output "e"
+++++ ++ .              increment cell 2 by 7 from 11 to  18 (l) and output "l"
.                       output "l" again, cell 2 remains unchanged
> .                     cell 3 (o) output "o"
<< +++++ +++++ +++++ .  increment cell 1 by 15 from 8 to 23 (space) and output space
> .                     cell 2 (W) output "W"
+++ .                   increment cell 2 by 3 from 23 to 26 (o) and output "o"
----- .                 decrement cell 2 by 5 from 26 to 21 (r) and output "r"
+++++ +++++ .           increment cell 2 by 10 from 21 to 31 (l) and output "l"
> .                     cell 3 (d) output "d"
<<< .                   back to cell 0 and output (new line character)
