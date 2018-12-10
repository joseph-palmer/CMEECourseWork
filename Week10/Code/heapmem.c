/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: heapmem.c
 * Desc: How to alocate memory from the heap.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>


void print_intarray(int* array, int nelems)
{
    int i = 0;
    for (i = 0; i < nelems; ++i) {
        printf("%i ", array[i]);
    }
    printf("\n");
}


// important to dealocate memory - putting it in a function alows you to handle
// all evential outcomes you can foresee and catch errors. Its safest to work
// like this in C.
void destroy_intarray(int** intarray)
{
   if (*intarray) {
       free(*intarray);
       *intarray = NULL;
   }
}


int* make_intarray(int numelements)
{
    int *intarray = NULL;

    // void* malloc (size_t sizeofmem)
    //intarray = (int*)malloc(numelements * sizeof(int)); // int* type cast not required more explicit and can aid debugging later on!
    // void* calloc (size_t, nelems, sizet sizeofeach)
    intarray = (int*)calloc(numelements, sizeof(int));

    if (intarray == NULL) {
        printf("Error: unable to allocate sufficient memory\n");
        exit(EXIT_FAILURE);
    }

    print_intarray(intarray, numelements);
    return intarray;
}


int main(void)
{
    int numsites = 10;
    int* sitedata = NULL; // Treat as array of integer data

    sitedata = make_intarray(numsites);
    print_intarray(sitedata, numsites);

    destroy_intarray(&sitedata); 
    destroy_intarray(&sitedata);

    
    return 0;
}
