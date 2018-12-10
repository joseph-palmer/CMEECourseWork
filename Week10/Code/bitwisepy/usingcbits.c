/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: usingcbits.c
 * Desc: Functions to use cbits.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>
#include "cbits/cbits.h"

int main(void)
{
    // create instances of the cbit objects
    CBit a = newCBit(200);
    CBit b = newCBit(200);
    CBit c = newCBit(200);

    // set cbits
    CBitSet(71, a);
    CBitSet(14, a);
    CBitSet(71, b);
    CBitSet(72, b);
    CBitSet(44, b);

    // test the bitwise AND opperation
    if (CBitAND(NULL, a, b)) {
        printf("Bitwise AND returns TRUE\n");
    } else {
        printf("Bitwise AND returns FALSE\n");
    }

    CBitAND(c, a, b);

    
    return 0;
}
