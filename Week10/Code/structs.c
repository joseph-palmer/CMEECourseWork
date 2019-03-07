/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: structs.c
 * Desc: Shows the use of structs in C.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

struct site_data {
	float lat;
	float longit; // `'long` is a reserved keyword, so using this instead
	float elev;
    int *spp_IDs; // A pointer to ID's of species counts
	int num_IDs; // The number of elements in this pointer ('array')
};

struct int_ptrs {
	int *pt1;
	int *pt2;
};

int main(void)
{
    struct site_data mysite1;
    mysite1.lat = 32.045;
    mysite1.longit = -104.181;
    
    int my_int = 0;
    struct int_ptrs twoints;

    twoints.pt1 = &my_int;

    *twoints.pt1 = 12;
    
    return 0;
}

