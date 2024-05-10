red
; This RED script will generate and display "Hello World" in a somewhat obscure manner
; by using a complex sequence of operations.

Red [
    Title: "Complex Hello World"
    Author: "Anonymous"
    File: %complex-hello-world.red
]

; Randomly shuffles a block of integers
shuffle: function [series [block!]] [
    random/seed now/precise
    random series
]

; Converts integers back to characters
int-to-char: function [code [integer!]] [
    to-char code
]

; Main block that contains encoded character values for "Hello World" in a scrambled order
encoded-block: [87 100 114 111 108 108 72 32 101 111]

; Shuffle the block to increase the obscurity
shuffled-block: shuffle encoded-block

; Now unshuffle or sort to retrieve the original message
sorted-block: sort shuffled-block

; Convert ASCII codes to characters
hello-world: map-each char sorted-block [int-to-char char]

; Convert block of characters to string
hello-world-string: reform hello-world

; Finally, print "Hello World"
print hello-world-string
