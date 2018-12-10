/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: unary.c
 * Desc: Shows C special addition and substraction of 1.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>


int main(void)
{
    // Note: using -o [name] to change the file name at compile.
    int x = 0;
    x = x + 1;

    ++x;
    
    // printf("The value of x: %i and %i\n", x++, x); // this will give a warning!
    printf("The value of x: %i\n", x++); // this will give a warning!

    return 0;
}
