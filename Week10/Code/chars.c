/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: chars.c
 * Desc: Shows character arithmatic.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>

int main(void)
{
    // Character arithmatic
    char c1 = 'a';
    char c2 = 'c';
    char case_offset;
    
    case_offset = c2 - c1;

    printf("case_offset evaluates to: %i\n", (int)case_offset);

    return 0;
}
