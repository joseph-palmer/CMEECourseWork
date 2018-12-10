/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: bitwise1.c
 * Desc: Shows the use of bitwise opperations.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>

int main(void)
{
    /* The main program function */
    signed char c1 = -1;
    signed char c2 = 0b0111; // binary code - 
    signed char c3 = 1b000111;

    c2 = c2 << 8;

    printf("cs is now: %u\n", (unsigned int)c2);

    
    return 0;
}
