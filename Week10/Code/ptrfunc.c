/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: ptrfunc.c
 * Desc: Shows the use of pointers in functions.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>

void index_through_array(int mynumbers[5], int* index)
{
    while (*index < 5) {
        printf("Element %i: %i\n", *index, mynumbers[*index]);
        ++(*index);
    }
    printf("Values of index at end of function call: %i\n", *index);
    return;
}

int *ptr_2_array(int* intarray, int index, int arraymax)
{
    int* result = NULL;
    if (index < arraymax) {
        result = &intarray[index];
    }

    return result;
}

int main(void)
{
    /* The main program function */
    int index = 0;
    int mynums[] = {19, 81, 4, 8, 10};
    int* x_ptr = NULL;
    char c = '@';
    char* cptr = &c;

    // setting pointers to void
    void* anydata = NULL;
    
    x_ptr = &mynums[3];
    anydata = (void*)x_ptr;
    anydata = (void*)cptr;

    printf("Dereferencing anydata: %c\n", *((char*)anydata));





    printf("Values of i before function call: %i\n", index);
    index_through_array(mynums, &index);
    printf("Value of i after functions call: %i\n", index);

    int *valptr;
    valptr = ptr_2_array(mynums, 1, 5);

    printf("Value in mynums at position %i: %i\n", 1, *valptr);
    
    return 0;
}
