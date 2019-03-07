/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: ReverseString.c
 * Desc: Reverses a string
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

char get_string_length(char *x)
{
    /* Gets the length of the string provided */

    // Set the length of string to 0 as a start
    int strlen = 0;

    // Loop through the strings elements until null character reached.
    // increment the string length each time.
    while(*(x + strlen) != '\0') {
        strlen++;
    }

    // Return the length of the string provided
    return strlen;
}


void reverse_rec(char *x, int begin, int end)
{
    /* Takes a pointer to a string, a begging and end point.
     * Recursivley goes through the string from both directions,
     * seting the left position as equal tot he right position until
     * the middle point is reached */

    // once both sides have been swapped up tot eh middle value exit
    if (begin > end)
       return;

    // set a variable to store the new left side position
    char c = *(x+begin);

    // Swap the end and beging positions
    *(x+begin) = *(x+end);
    *(x+end) = c;

    // call the function again to move on to the next position.
    reverse_rec(x, ++begin, --end);
}

void check_palindrome(char *x, int strlen)
{
    /* Checks if a string is a palendrome */

    // make a copy of the input string to reverse
    char copystr[strlen];

    // while the string is not finished copy the positions over to the end
    // most unocupied position.
    int i = 0;
    while(*(x + i) != '\0') {
        *(copystr + ((strlen -1) - i)) = *(x + i);
        i++;
    }

    // close the copied string
    *(copystr + strlen) = '\0';

    // check if the two strigs are pelendromes
    if (*copystr == *x) {
        printf("Palendrome found!!!\n");
    }
}



int main(void)
{
    // declare variables
    char str1[] = "racecar";
    int string_length = get_string_length(str1);
    
    // reverse the string in place
    reverse_rec(str1, 0, string_length -1);

    // display the reversed string
    printf("%s\n", str1);

    // check if it is a palendrome
    check_palindrome(str1, string_length);

    return 0;
}



























