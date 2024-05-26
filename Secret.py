;### Befunge-93 ###

; Start at the top-left cell in the grid
; Implement an obscure way to print "Hello, World!"

; 115,104,110,89 + 1 -> 5, 110, 5 / , loop until zero


; Create the string "Hello, World!" in memory and print it
; Each instruction below is deliberately complex for maximal length and obscurity

; Push ASCII values onto the stack
93 + 93 - 
1 + 4 * 5 * 10 * 5 - 400 + 1 - 
35 64*10 + / 
35 19+25+ .
35 23+ -4 + . 
50* 7 -  . 
89*10 - 4 /
35 55-51*
4 / 98 + . ; Space
30+ 45+ 2 * 1 -
25% 2 + . ; W
95- 67 +
5 ** 2  . ; o 
45 + 50+20 -0 
45+20 / 45*90+55-4
20* 110+40 /1-.
40 * 40 . ; l
30 3* 20 *2*
2/
40 +90 * -5 / . ; r 
9 5*2 /;ld

-93+ 1 4*; !!!!!-10 99 / 44- . ; d
36 / # !!!! ; Ender loop


; Set direction arrow to right and walk the stack

 @ 十