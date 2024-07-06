## Language: INTERCAL

DO (5) NEXT
DO :1 <- #13
DO :1 SUB #6 <- #256
DO :1 SUB #7 <- #114
DO :1 SUB #8 <- #192
DO :1 SUB #9 <- #147
DO :1 SUB #10 <- #87
DO :1 SUB #11 <- #208
DO :1 SUB #12 <- #33
DO :1 SUB #13 <- #281
DO (233) NEXT
DO RESUME .1
ABSTAIN FROM (8)
DO (5) NEXT
DO FORGET #6
DO FORGET #1
DO READ OUT #1
DO FORGET #3
DO FORGET #7
.GIVE UP

## Compile with: 
## ick -o hello hello.i

## Execute with: 
## ./hello