/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: comparestr.c
 * Desc: Compares two strings
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>


int nelm(char *a)
{
    // gets the number of elements in a char array
    int arraylen = 0;
    while(a[arraylen]) {
        arraylen++;
    }
    return arraylen;
}


int get_max(char *array1, char *array2)
{
    int a = nelm(array1);
    int b = nelm(array2);
    int maxval = a;
    if (b > a) {
        maxval = b;
    }
    return maxval;
}

int get_score(char *str1, char *str2)
{
    int score = 0;
    int i = 0;
    for (i = 0; i < nelm(str1); ++i) {
        if (str1[i] == str2[i]) {
            score++;
        }
    }
    return score;
}

void run_compare(char *array1, char *array2)
{
    int max_len = get_max(array1, array2);
    int i = 0;
    char str1[max_len];
    char str2[max_len];
    char dash = '-';
    
    for (i = 0; i < max_len; ++i) {
        if (i < nelm(array1)) {
            str1[i] = array1[i];
        } else {
            str1[i] = dash;
        }
    }
    for (i = 0; i < max_len; ++i) {
        if (i < nelm(array2)) {
            str2[i] =  array2[i];
        } else {
            str2[i] = dash;
        }
    }

    // end the strings
    str1[max_len] = '\0';
    str2[max_len] = '\0';

    int score = get_score(str1, str2);

    printf("%i\n", score);
    printf("%f\n", (float) score / max_len);

}

int main(void)
{
    char str_1[] = "ATTCGGTGGGCCTAATCCA";
    char str_2[] = "ATTGCCGTTGCCAATTGCA";

    run_compare(str_1, str_2);

    printf("\n");
    
    return 0;
}
