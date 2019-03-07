/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: Recursion.c
 * Desc: Shows the use of recursive functions
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

void recursive_count(int start)
{
    // uses recursion to count down
    printf("%i\n", start);
    if (start < 1){
        return;
    }
    start--;
    recursive_count(start);
}

int main(void)
{
    recursive_count(10);
    
    return 0;
}
