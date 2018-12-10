/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: funcintro.c
 * Desc: Shows hows to use functions in C.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>


int add_integers(int a, int b)
{
    /* Adds two integers together and returns the result */
    int result = 0;
    result = a + b;
    return result;
}


int main(void)
{
    // The main program function
    // This is a function in itself.
    int a = 4;

    printf("The result is: %i\n", add_integers(a, 2));
    
    return 0;
}
