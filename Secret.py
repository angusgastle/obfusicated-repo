
# Behold, the legendary "Hello World" script in INTERCAL, an obscure esolang designed to be as different from normal programming languages as possible.

# Load Numerical Constants
# DO is used to perform actions in INTERCAL
DO ,1 <- #13     ; Initialize variable ,1 with the decimal value 13 which represents the ASCII value for carriage return.
DO ,2 <- #10     ; Initialize variable ,2 with the decimal value 10 which represents the ASCII value for line feed.

# Define Variables
DO .1 <- #721     ; Define and initialize .1 to the decimal ending part of the ASCII codes we'll use for 'H' conversion.
DO .2 <- #33890   ; Define and initialize .2 to the decimal ending part of the ASCII codes we'll use for 'e', 'l', 'o', 'W', 'r', and 'd' conversion.

# Generate 'Hello World' String
DO .3 <- .1       ; Save .1 so we can modify .1 to build our characters
DO .4 <- .2       ; Save .2 so we have original value of .2 for our conversion

# First Character 'H'
DO ,3 <- #33      ; Initialize variable ,3 with value 33, the offset to calculate 'H' from 721
DO ,3 <- #28      ; Offset 28 from 721 gives us 72 which is ASCII 'H'

# Second Character 'e'
DO ,4 <- #340             ; Initialize ,4 with value 340 (the offset for 'e')
DO (.2) <- (.2) +1        ; Add No Operation to adjust value ensuring we get 101 (ASCII 'e')

# Third, Fourth Characters 'l'
DO .4 <- #33202           ; Set .4 with value 33202 offset for 'l'
DO .4 <- #33202           ; Since 'l' repeats, same offset

# Fifth Character 'o'
DO ,5 <- #479              ; Initialize ,5 for ASCII 'o' from 347 conversion

# Sixth Character 'W'
DO ,6 <- #129              ; Initialize ,6 for ASCII 'W' from 33890 conversion

# Seventh Character 'o'
DO ,7 <- #479              ; Use same value for 'o'

# Eighth Character 'r'
DO ,8 <- #375              ; Initialize ,8 for ASCII 'r' from 340 offset conversion adding +1

# Ninth Character 'l'
DO ,9 <- #33202           ; Use same conversion value for 'l'

# Tenth Character 'd'
DO ,10 <- #33220          ; Initialize ,10 for ASCII 'd'

# Concatenate All
DO WRITE IN <- ,1; ,2; ,3; ,4; ,5; ,6; ,7; ,8; ,9; ,10

# Print to Console
DO FORGET #1
DO RESUME NEXT
