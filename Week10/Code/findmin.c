/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: findmin.c
 * Desc: Finds the minimum and maximum of a list of numbers, also sorts them.
 * Date: Dec-2018 */
 
// Library Imports //
#include <stdio.h>

int main(void)
{
    /* The main program function */
    // make an array of numbers to look for and initialise the iterator,
    // the minimum and the maximum values.
    int numbers_length = 12;
    int numbers[] = {123, 747, 768, 2742, 988, 1121, 109, 999, 727, 1030, 999, 2014, 1402};
    int i = 0;
    int minval = 1000000;
    int maxval = 0;

    // Loop through the items in the array and check each against the minimum.
    // if the array item is greater/less than the min/max value, overwrite them.
    for (i = 0; i <= numbers_length; ++i) {
        if (numbers[i] < minval) {
            minval = numbers[i];
        }
        if (numbers[i] > maxval) {
            maxval = numbers[i];
        }
    }

    // Write the values to the buffer.
    printf("The min value is: %i\n", minval);
    printf("The max value is: %i\n", maxval);

    // sort the array - bubble sort method -
    // declare variables for use
    int c = 12;
    int n = 12;
    int d = 12;
    int swap = 0;

    for (c = 0; c < n - 1; c++) {
        for (d = 0; d < n - c - 1; d++) {
            if (numbers[d] > numbers[d+1]) {
                swap = numbers[d];
                numbers[d] = numbers[d+1];
                numbers[d+1] = swap;
            }
        }
    }

    for (c = 0; c < n; c++) {
        printf("%d ", numbers[c]);
    }
    printf("\n");


    return 0;
}











