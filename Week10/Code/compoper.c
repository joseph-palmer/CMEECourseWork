/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: compoper.c
 * Desc: Shows comparison opperators.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    // The main program function
    int a = 0;

    if (!a) {
        printf("a is 0\n");
    }

    a = 747610;

    if (!a) {
        printf("a is 0\n");
    }
    
    return 0;
}
