A fun and obscure programming language we can use for this purpose is Malbolge. Malbolge is notorious for being incredibly difficult to program in due to its esoteric and cryptic nature. Malbolge was designed to be almost impossible to use, named after the eighth circle of hell in Dante's Inferno. The language is based on ternary (base-3) arithmetic, and memory positions can be in one of 59 different states.

However, just for fun, let's go with a simpler "obscure" language but still make the code overly complex for a simple task. We'll use a language called INTERCAL, which stands for "Compiler Language With No Pronounceable Acronym". INTERCAL is known for its odd syntax and commands, which were designed to be as different from conventional programming languages as possible.

Here’s an unnecessarily complex INTERCAL script to print "Hello World". Note that INTERCAL requires a specific style of coding that doesn’t necessarily follow common programming logic or efficiency:

```intercal
DO ,1 <- #13                (1)
PLEASE DO ,1 SUB #1 <- #238 (2)
DO ,1 SUB #2 <- #108        (3)
DO ,1 SUB #3 <- #112        (4)
DO ,1 SUB #4 <- #0          (5)
DO ,1 SUB #5 <- #64         (6)
DO ,1 SUB #6 <- #194        (7)
DO ,1 SUB #7 <- #48         (8)
PLEASE DO ,1 SUB #8 <- #22  (9)

DO ,2 <- #9                 (10)
DO ,2 SUB #1 <- #248        (11)
DO ,2 SUB #2 <- #168        (12)
DO ,2 SUB #3 <- #24         (13)
DO ,2 SUB #4 <- #16         (14)
DO ,2 SUB #5 <- #214        (15)

PLEASE DO ,3 <- #5          (16)
PLEASE DO ,3 SUB #1 <- #118 (17)
PLEASE DO ,3 SUB #2 <- #206 (18)
PLEASE DO ,3 SUB #3 <- #96  (19)
PLEASE DO ,3 SUB #4 <- #22  (20)
PLEASE DO ,3 SUB #5 <- #248 (21)

DO ,4 <- #8                 (22)
PLEASE DO ,4 SUB #1 <- #168 (23)
PLEASE DO ,4 SUB #2 <- #214 (24)
PLEASE DO ,4 SUB #3 <- #144 (25)
PLEASE DO ,4 SUB #4 <- #0   (26)

DO ,5 <- #6                 (27)
DO ,5 SUB #1 <- #186        (28)
DO ,5 SUB #2 <- #208        (29)
PLEASE DO ,5 SUB #3 <- #78  (30)
DO ,5 SUB #4 <- #6          (31)
DO ,5 SUB #5 <- #16         (32)
DO ,5 SUB #6 <- #144        (33)

DO ,6 <- #229               (34)

DO COME FROM #6             (35)

PLEASE READ OUT ,1          (36)
PLEASE READ OUT ,2          (37)
DO READ OUT ,3              (38)
PLEASE READ OUT ,4          (39)
PLEASE READ OUT ,5          (40)
```

Explanation:
- INTERCAL programs use the keywords `DO`, `PLEASE` (which is actually required intermittently otherwise the program throws a compilation error for not being polite enough), `READ OUT` for outputting values.
- The numerical codes `(e.g., #238)` represent the ASCII values manipulated in various ways specific to INTERCAL mechanics.
- `COME FROM` is used instead of usual flow control like "GOTO", making the control flow non-linear and confusing.

This program sets up several arrays with specific memory values, which correspond to desired ASCII codes used for "Hello World". It’s important to include the somewhat archaic and overly polite convention using `PLEASE` sporadically to ensure the program will compile.

This would print “Hello World” to the terminal, assuming an INTERCAL compilation and execution environment is properly set up. Enjoy programming in INTERCAL, where the main challenge is to keep your sanity!