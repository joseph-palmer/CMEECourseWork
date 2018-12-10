/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: operators.c
 * Desc: Shows the use of operators
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>

int main(void)
{
    // The main function
    int a = 7;
    float b = 2;
    float c = 0;

    c = a / b;
    printf("The result of %i divided by %f is: %f\n", a, b, c);    
    return 0;
}
