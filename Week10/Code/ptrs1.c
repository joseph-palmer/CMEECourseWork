/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: ptrs1.c
 * Desc: Using pointers
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    /* The main program function */
    // declare variables (including pointer)
    int index = 0;
    int* index_ptr = NULL; // initialise pointer as points to random place

    // initialise index_ptr
    index_ptr = &index;

    printf("Tha value of index: %i\n", index);
    printf("The value of index by indirection through pointer: %i\n", *index_ptr);

    // can also asign through the indirection
    *index_ptr = 71;

    printf("Tha value of index: %i\n", index);
    printf("The value of index by indirection through pointer: %i\n", *index_ptr);


    // more using poiters!
    int x = 3;
    int y = 7;

    int* inptr1 = &x;
    int* inptr2 = &y;

    int z = 0;

    z = *inptr1 * *inptr2;

    printf("%i\n", z);

        
            
        
    return 0;
}
