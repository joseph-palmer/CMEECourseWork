/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: addarray.c
 * Desc: Shows more uses of functions in C, wih regards to adding arrays.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>

// functions need to be above where thay are called. to get around this we can
// put a forward declaration.
void concat_array(int result[], int reslength, int array1[], int array2[], int inputlen);

int main(void)
{
    /* The main program function */
    int array1[] = {1, 2, 3};
    int array2[] = {4, 5, 6};
    int array3[6];

    concat_array(array3, 6, array1, array2, 3);

    int i = 0;
    for (i = 0; i < 6; ++i) {
        printf("%i ", array3[i]);
    }
    printf("\n");
    
    return 0;
}

// then we can put the actual function further down!
void concat_array(int result[], int reslength, int array1[], int array2[], int inputlen)
{
    int i = 0;
    for (i = 0; i < inputlen; ++i) {
        if (i < inputlen) {
            result[i] = array1[i];
        }
        result[i + inputlen] = array2[i];
    }
}

