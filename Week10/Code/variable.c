/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: variable.c
 * Desc: Shows the use of variables in c.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>


int main(void)
{
    int x = 1; // Safest option is to always initiaize a variable
    float y = 2.03;
    float z = 0;
   
    // Load y and x with 2.03 and 1 respectivley,
    // Load r1
    // move y to r1 (2.03) in that register -> type promotion, promoted x(int) to float.
    // Add x to r1, making it 3.03
    // Load z and move r1 to Z
    z = x + y;


    printf("The value of z: %f\n", z);

    return x;
}

