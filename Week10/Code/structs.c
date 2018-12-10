/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: structs.c
 * Desc: Shows the use of structs in C.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>


// one way of showing a point in 2d shape (x,y)
float x_points[] = {0.73, 0.44, 0.32, 0.43};
float y_points[] = {1.52, 2.34, 3.87, 3.13};

// using structs to store in information
struct point_s {
    float x;
    float y;
};

int main(void)
{
    struct point_s pt1;
    struct point_s pt2;

    pt1.x = x_points[0];
    pt1.y = y_p
    
    return 0;
}

