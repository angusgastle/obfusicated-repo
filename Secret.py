brainfuck
[ Written in Brainfuck, an esoteric programming language ]

++       Initialize cell 0 to 2
> +++++  Initialize cell 1 to 5
[        While cell 1 is not 0
    < +++       Increment cell 0 by 3 (cell 0 becomes 5)
    > -         Decrement cell 1 by 1
]
> ++++   Move to cell 2 and set it to 4
> +++    Move to cell 3 and set it to 3
> ++++  Set cell 4 to 4
> +     Set cell 5 to 1

[Begins to set up message]
<.      Print 'H' (ASCII 72 stored at cell 0)

[Preparation for e]
>       Move to cell 1 (nothing happens as it's 0)
< ++++++. Print 'e' (cell 0 increase to 101)
< +++++. Print 'l' (cell 0 increase to 108)
< +++++>+<-. Print 'l'
< ++++. Print 'o' (cell 0 increase to 111)

[Preparation for ' ' (space character)]
< < ++. Print space

[Preparation for W]
> +++++++. Print 'W'
< -----. Print 'o'
< ++++++. Print 'r'
< . Print 'l'
< -----. Print 'd'
< + ---. Print ! (exclamation)

[End of program]
. Print (newline character to end program)
