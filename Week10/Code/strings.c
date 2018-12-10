/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: strings.c
 * Desc: Shows use of strings in C.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>

int main(void)
{
    // The main program function
    // both of these are strings
    char mystring1[] = "This is a string\n";
    char lstring[] = {'T', 'h', 'i', 's', '\0'};
    char five[] = "five"; // there are 5 characters, the null \0 is hidden 
    int i = 0;


    for (i = 0; mystring1[i]; ++i) {
        printf("%c", mystring1[i]);
    }


    return 0;
}
