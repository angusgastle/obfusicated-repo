# The following script is written in the INTERCAL programming language, 
# a deliberately esoteric and difficult-to-use language. 
# It is designed to produce "Hello World" when executed.

DO,1 <- #13
DO,1 SUB #1 <- #108
DO,1 SUB #2 <- #9
DO,1 SUB #3 <- #158
DO,1 SUB #4 <- #259
DO,1 SUB #5 <- #108
DO,1 SUB #6 <- #132
DO,1 SUB #7 <- #150
DO,1 SUB #8 <- #62

DO FORGET ,1

DO,1 <- #1
DO,2 <- #257
DO,3 <- #180

DO ,1 SUB #1 <- #59
DO ,1 SUB #2 <- #25
DO ,1 SUB #3 <- #173
DO ,1 SUB #4 <- #0
DO ,1 SUB #5 <- #108
DO ,1 SUB #6 <- #108
DO ,1 SUB #7 <- #52
DO ,1 SUB #8 <- #159

DO FORGET ,1

DO RESUME NEXT

DO ,1 SUB #1 <- #98
DO ,1 SUB #2 <- #110
DO ,1 SUB #3 <- #139
DO ,1 SUB #4 <- #126
DO ,1 SUB #5 <- #132
DO ,1 SUB #6 <- #108
DO ,1 SUB #7 <- #139
DO ,1 SUB #8 <- #126

DO FORGET ,1

DO ,1 SUB #1 <- #146
DO ,1 SUB #2 <- #156
DO ,1 SUB #3 <- #139
DO ,1 SUB #4 <- #126
DO ,1 SUB #5 <- #159
DO ,1 SUB #6 <- #108
DO ,1 SUB #7 <- #169
DO ,1 SUB #8 <- #126

DO ,1 <- #1
DO ,2 <- #2

PLEASE DO (5) NEXT
PLEASE DO (6) NEXT
PLEASE WRITE IN ,1

(1) DO ,1 SUB #1 <- #1
(2) DO ,2 <- #4
(3) PLEASE DO (4) NEXT
DO RESUME NEXT

PLEASE FORGET ,1
DO ,1 SUB #1 <- #0
DO ,1 SUB #2 <- #7
DO ,1 SUB #3 <- #110
DO ,1 SUB #4 <- #118
DO ,1 SUB #5 <- #115
DO ,1 SUB #6 <- #101
DO ,1 SUB #7 <- #97
DO ,1 SUB #8 <- #99

PLEASE ABSTAIN FROM (4)

DO RESUME NEXT

(4) DO ,1 <- #1
DO ,2 <- #6

DO PLEASE FORGET #1
DO PLEASE RESUME #1

PLEASE DO (7) NEXT
DO ,1 <- #1
DO ,1 SUB #1 <- #108

PLEASE FORGET ,1

(5) PLEASE DO (8) NEXT
(6) DO (9) NEXT
(7) DO (10) NEXT
(8) DO RESUME NEXT

(9) DO ,1 <- #1
DO ,1 SUB #1 <- #119
DO ,1 SUB #2 <- #111
DO ,1 SUB #3 <- #114
DO ,1 SUB #4 <- #108
DO ,1 SUB #5 <- #100

PLEASE DO (8) NEXT

(10) DO ,3 <- #64
DO ,4 <- #65
DO RESUME NEXT