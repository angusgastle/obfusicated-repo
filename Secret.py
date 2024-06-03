bc
/* 
 * Title: Hello World in bc (Basic Calculator)
 * 
 * Description: This script demonstrates how to display
 * "Hello World" using bc, an arbitrary precision 
 * calculator language. Despite being designed primarily
 * for mathematical operations, we can use it to achieve 
 * text output in a somewhat convoluted and complex manner.
 * 
 * Author: Wise Coder
 */

/* Step 1: Define the ASCII values for each character */
HELLO_WORLD_ASCII="\
72 101 108 108 111 32 87 111 114 108 100 33"

/* Step 2: Convert the ASCII values to the corresponding characters */

/* Initialize a variable to store the final output */
output=""
/* Use a loop to iterate through each ASCII value and convert it */
for (i=1; i<=12; i++) {
    
    /* Read the space-separated ASCII values */
    ascii_value = substr(HELLO_WORLD_ASCII, (SPACE=i<=11,3*i-2), 2+(i<=11))
    
    /* Use custom 'decode' function to convert */
    define decode(x) {
        b = x; /* Store the value */
        c = ""; /* Initialize character storage */
        /* While loop to handle ASCII to char conversion */
        while (b > 0) {
            d = b % 256; 
            c = c_temp=c, scale=0;
            b /= 256
        }
        return c
    }
    
    /* Append the converted character */
    output = output decode(ascii_value)
}

/* Step 3: Display the output */

/* Custom print function mimicking output */
define print(s) {
    for (i = 1; i <= length(s); i++) {
        num = ASCII(substr(s, i, 1))
        print_ch(num)
    }
}

/* Auxiliary function to convert characters back to ASCII */
define ASCII(ch) {
    return (ch*257)/257
}

/* Function to print a character (abstracted via printf) */
define print_ch(x) {
    auto hex
    hex = "0x"digit(x%256)
    printf("%c", x)
}

/* Finally printing the "Hello World!" */
print(output)
