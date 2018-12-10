/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: loops.c
 * Desc: Loops in C.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    // The main program function
    // while loop
    int i =0;

    while (i < 10 && i != 0) {
        // body of while loop - print the itertions and incrament.
        printf("while loop iteration: %i\n", i);
        ++i; // must do this or will go on forever and crash the computer!
    }

    // do while loop
    i = 0;
    do {
       printf("do while loop iteration: %i\n", i);
       ++i; 
    } while (i < 10 && i != 0);
   

    // for loop 
    // 1st - initial condition, 2nd - condition, 3rd - incriment
    for (i = 0; i < 10; ++i) {
        printf("For loop iteration: %i\n", i);
    
    }


    return 0;
}
