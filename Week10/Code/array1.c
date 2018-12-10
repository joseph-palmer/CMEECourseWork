/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: array1.c
 * Desc: Shows the use of arrays in C.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>

int main(void)
{
    // Arrays - can only be one data type
    int arraylength = 5;
    int intarray[arraylength];
    int implarray[] = {1, 2, 4, 5, 6, 7};

    // whats inside intarray?
    int i = 0;
    int x = 0;
    for (i = 0; i < arraylength; ++i) {
        x = intarray[i];
        printf("Value at intarray[%i] is: %i\n", i, x);
    }
    
    for (i = 0; i < 10; ++i) {
        x = implarray[i];
        printf("Value at implarray[%i] is: %i\n", i, x);
    }
    
    // putting information into an array
    for (i = 0; i < arraylength; ++i) {
        intarray[i] = i + 1;
        printf("The value of intarray[%i] is %i\n", i, intarray[i]);
    }

    /* Concatonating arrays - awkward in c, you need to make a 3rd array and
     * then add the contents of the arrays together */
    int joinedarray[arraylength + 6];

    for (i = 0; i < (arraylength + 6); ++i) {
        if (i < arraylength) { 
            joinedarray[i] = intarray[i];
        }
        joinedarray[i + arraylength] = implarray[i];
        printf("The value of joinedarray[%i] is %i\n", i, joinedarray[i]);
    }

    return 0;
}
