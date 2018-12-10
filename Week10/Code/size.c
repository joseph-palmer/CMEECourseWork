/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: size.c
 * Desc: works out size of variable types in C.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    printf("Size of char on this system: %zu bytes\n", sizeof(char)); 
    printf("Size of int on this system: %zu bytes\n", sizeof(int));
    printf("Size of float on this system: %zu bytes\n", sizeof(float));
    printf("Size of long double on this system: %zu bytes\n", sizeof(long double));

    return 0;
}
