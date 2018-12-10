/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: structs.c
 * Desc: Shows the use of structs in C.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>


// using structs to store in information, all used in paralel, more usefull
typedef struct safe_intarray {
    int* intdata; // as struct does not make any code no need to initialise.
    int  nelems;
} safe_intarray;


//void set_int_data(struct int* sarray, int index)
//{
    
//}

int get_int_data(safe_intarray* sarray, int index)
{   
    // get the data
    int res = 0;
    if (index < (*sarray).nelems) {
        //res = (*sarray).intdata[index]; // These two do the same thing
        res = sarray -> intdata[index];
    } else {
        printf("Error: subscript out of bounds\n");
        exit(EXIT_FAILURE);
    }

    return res;
}

int main(void)
{
    struct safe_intarray a1;

    int nelems = 10;

    a1.intdata = (int*)calloc(nelems, sizeof(int));
    a1.nelems  = nelems;

    a1.intdata[1] = 2;

    printf("Attempt to read out of bounds: %i\n", get_int_data(&a1, 17));
    printf("Attempt to read within bounds: %i\n", get_int_data(&a1, 1));



    return 0;
}

