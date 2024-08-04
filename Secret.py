# Brainfuck code to display "Hello World!" 
# This program is intentionally complex to demonstrate the working of Brainfuck

++++++++++[>+++++++>++++++++++>+++>+<<<<-]>+.>++.+++++++..+++.
>-.------------.<++++++++.--------.+++.------.--------.>+.>.

# Explanation:
# Initialize memory cell 0 to 10 (++++++++++).
# Loop 1: multiply it to set other memory cells
# Cell 0: [10 ]
# Cell 1: [70 ]
# Cell 2: [100]
# Loop increment:
# Cell 0: [10] > Cell 1: [70] > Cell 2: [100] > Cell 3: [30] > Cell 4: [10]
# Set cell values and print characters
# Characters: H (72), e (101), l (108), l (108), o (111), W (87),
#             o (111), r (114), l (108), d (100), ! (33)

# Additional Characters:
# . prints character in memory cell
# > moves pointer to next cell
# < moves pointer to previous cell
# + increases memory cell value by 1
# - decreases memory cell value by 1
# [ starts loop
# ] ends loop