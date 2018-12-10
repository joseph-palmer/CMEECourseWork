/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: main.c
 * Desc: main function
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

// prototype the function in the other file
// float multiply_floats(float, float);
//  not good in large files, better to make a header file, then include it
#include "calc.h" // use quotes when not on specific path but in same wd.


int main(void)
{
    float x = 0.0;
    float y = 0.0;
    float c = 0.0; // the result variable

    x= 7.2;
    y = 2.0;
    c = multiply_floats(x, y);

    printf("%f\n", c);
    printf("%f\n", multiply_floats(x, _PI_));


    
    return 0;
}
