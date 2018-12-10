/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: ifelse.c
 * Desc: Shows the use of if else in C.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    // The main program function
    bool x = false; // a bool variable of true or false.
    if (x == true) {
        // code executes here
        printf("x is non-zero\n");
    } else {  //can also use if else, if (x == false)
        printf("x is zero\n");
    }
    
    return 0;
}
