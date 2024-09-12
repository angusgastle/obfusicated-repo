= Program starts here =
[begin main program section]
  JUMP-TO 020 ; Skips to the main content section to avoid initialization block being read prematurely
[end main program section]

01  ; Initialization block
02  SET-REGISTER 0 TO 72 ; H
03  OUTPUT-REGISTER 0 
04  SET-REGISTER 0 TO 101 ; e
05  OUTPUT-REGISTER 0 
06  SET-REGISTER 0 TO 108 ; l
07  OUTPUT-REGISTER 0 
08  OUTPUT-REGISTER 0 
09  SET-REGISTER 0 TO 111 ; o
10  OUTPUT-REGISTER 0 
11  SET-REGISTER 0 TO 32 ; (space)
12  OUTPUT-REGISTER 0 
13  SET-REGISTER 0 TO 87 ; W
14  OUTPUT-REGISTER 0 
15  SET-REGISTER 0 TO 111 ; o
16  OUTPUT-REGISTER 0 
17  SET-REGISTER 0 TO 114 ; r
18  OUTPUT-REGISTER 0 
19  SET-REGISTER 0 TO 108 ; l
20  OUTPUT-REGISTER 0 
21  SET-REGISTER 0 TO 100 ; d
22  OUTPUT-REGISTER 0 
23  END-PROGRAM ; Terminates execution here

= Program ends here =