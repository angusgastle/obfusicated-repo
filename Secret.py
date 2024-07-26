brainfuck
++[----->++<]>.   The initial increment when combined with the loop sets cell 1 to 8.
+[-->+++<]>.      Adds 24 to cell 2.

+++[----->+++<]>. Adjusts the value in cell 2.
+.                Adds one more to output 'H'.

++++[->+++<]>.    Fills cell 3 to get to the desired value.
-.                Adjusts to output 'e'.

++++++++++.       Simply adds 10 at current position.
-----.            Subtracts 5 to result in 'l'.
>++++++[->+++<]>. Another complex loop to increment cell 4.

--------.         Subtract 8 points.
<+++++++.         Adjust cell for 'W'.

++[->+++++<]>+    Loop manipulation for next value.
+++[->+++<]>.     Adjust and move for subsequent value.
+.                Increment for desired value.

++++.[->--<]>.    Another complex adjustment for 'o'.
<.                Move back to correct position.

+++++++[->++<]>.  Move and adjust for space.
---------.        Subtract a significant value.

++++++.[->+++<]>. Loop adjustment for ' '.
.                 Final increment for resulting value 'd'.
