brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>+.>---.+++++++..+++.>++.<<+++++++++++++++.+.>++++.<++++.------.--------.>>>+.>++++++++++.

# Brainfuck is an esoteric programming language created in 1993 by Urban Müller. 
# The primary aim of Brainfuck is to achieve Turing-completeness in the smallest possible compiler. 
# The language uses a memory array each initialized to zero, an instruction pointer that starts at the first command in the program,
# and a memory pointer (which starts at the first memory cell).

# Explanation:
# 1. Start with 10 (++++++++++) on the first cell.
# 2. Move to the second cell, add 70 (10 * 7): [0, 70, 0, 0]
# 3. Move to the third cell, add 100: [0, 70, 100, 0]
# 4. Move to the fourth cell, add 30: [0, 70, 100, 30]
# 5. Move to the fifth cell, add 10: [0, 70, 100, 30, 10]
# 6. Go back to the first cell and decrement the first cell by 1: [9, 70, 100, 30, 10]
# 7. Move to the second cell, print the ASCII value which is 72: H
# 8. Move to the third cell, subtract 3 (---): [9, 67, 100, 30, 10], print G (71): e
# 9. Increment, then print S (83): l
# 10. Print another S (83+1): l
# 11. Print Y (89): o
# 12. Print Z (90): space
# 13. Move to next cell, decrement by 1: [9, 67, 100, 30, 10, 9]
# 14. Print Z (90): W
# 15. Print o (111): o
# 16. Move to previous cell, print l (108 - 1): r
# 17. Print d (100): d
# 18. Move ahead and print ! (33): !
# 19. And done.
