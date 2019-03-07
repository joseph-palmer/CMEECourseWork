/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: JoiningStrings.c
 * Desc: Joins 2 strings together
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

int get_string_length(char *str1)
{
    /* Gets the length of a given string*/
    int strlen = 0;
    while(str1[strlen]) {
        strlen++;
    }

    return strlen;
}

char* concat_str(char *str1, char *str2)
{
    /* Concatonates two strings together*/

    int str1_len = get_string_length(str1);
    int str2_len = get_string_length(str2);
    int i = 0;
    char *combined; // a pointer to the place to store the output
    char space = ' ';

    // get the memory space in main for the concatonated strings
    combined = malloc(sizeof(char) * (str1_len + str2_len + 1));

    // loop through the length of the combined strings (+ a space!)
    for (i = 0; i < (str1_len + str2_len + 1); ++i) {
        // if still working on first string, copy it over to the new string
        if (i < str1_len) {
            combined[i] = str1[i]; 
        // if at the end of the first string insert a space
        } else if (i == str1_len) {
            combined[i] = space;
        // set the rest of the new string as the second string
        } else {
            combined[i] = str2[i - str1_len - 1];
        }
    }

    // end the string with the null character
    combined[str1_len + str2_len + 1] = '\0';

    return combined;

}

int main(void)
{
    // concatonate two strings!
    char str1[] = "The quick brown fox";
    char str2[] = "jumped over the lazy dog";
    char *concat;
    concat = concat_str(str1, str2);
    printf("%s\n", concat);

    
    return 0;
}
