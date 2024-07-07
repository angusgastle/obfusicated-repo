brainfuck
+++++ +++++             initialize cell[0] to 10
[                       start loop
    >++++++            increment cell[1] to 60
    [                  start nested loop
        >++            increment cell[2] to 2, this will be used for 'h'
        >+++           increment cell[3] to 3, this will be used for 'e'
        >+++++         increment cell[4] to 5, this will be used for 'l'
        >++.           increment cell[5] to 2, then 1 step for '.' (68 in ASCII), this will be used for 'o'
        >++            increment cell[6] to 2, this will be used for ' '
        >---.          decrement cell[7] to 3, then 1 step back, resulting in '/' (47 in ASCII), this will be used for 'W'
        >+.            increment cell[8] to 1, + steps more for 'o' => resulting in 'r'
        <++++++        increment cell[6] (current cell) to 63 for 'd' by - 28 steps then + 3 steps
        <<             return position to cell[4] (holding 'o')
        <              return cell[3] to 3 (holding 'e'), 3 + 1 = 'l'
        -              decrement cell to 2
        <              go to cell[2] skip 2 steps, find cell 1 -> decrement cell to 1 remaining steps at 60
    -                  end nested loop decrement cell[1]
<<<<<+                add remaining increment to cell[0] to 60 steps for ending loop
]                     end loop

Print "Hello World!"
>---.               cell[1] is now 72; 'H'
>++.               cell[2] is now 101; 'e'
>+.                cell[3] is now 108; 'l'
>.                 cell[4] is now 108; 'l'
<->.               decrement cell for holding letter 'o' = 111, rest steps add it forward
<-.                cell[1] is now 32; space ' '
>.                 cell[2] is now 87; 'W'
+++.               increment cell holding;adding letters for keeping the result 'o' to 'r'
<<++.              decrement cell at particular holding steps;from starting at
<-.                go to cell at global holding steps
>.                 final result character 'd'
