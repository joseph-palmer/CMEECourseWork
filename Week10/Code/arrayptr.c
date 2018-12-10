/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: arrayptr.c
 * Desc: Using pointers with arrays.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

void print_intarray(int arraylen, int* intarray)
{
    int i = 0;
    for (i = 0; i < arraylen; ++i) {
        printf("%i ", *(intarray + i));
    }
    printf("\n");
}


int main(void)
{
    /* The main program function */
    // The array is a block of memory 
    int intarr[] = {41, 22, 33};
    int* intptr = NULL;

    intptr = &intarr[0]; // place the arrays first element address in pointer!
    intptr = intarr; // can also use this, as the compiler treats this as an address.

    printf("Array poisition 0 by indirection: %i\n", *intptr);

    print_intarray(3, intarr);
    print_intarray(3, intptr);
    
    return 0;
}
