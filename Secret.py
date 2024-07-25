# Factor

USING: kernel io math.sequences math formatting splitting combinators ;
IN: hello-world

: hello-world ( -- )
    "Hello"  "World" [ " " split ] bi@
    [ 
        2array swap 2array swap 
        2array append-array
    ] 
    [ println ]
    bi@ ;

: display-hello-world ( -- )
    hello-world each ;

! Execute the function to display Hello World
display-hello-world