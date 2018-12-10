/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: counting_primes.c
 * Desc: Counts prime numbers between 1 and 100
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>


int prime_check(int a)
{
    /* Check if the number is a prime, if so return 1, else return 0 */
    if (a == 0) {
        return 0;
    }
    
    int i = 0;

    for (i = 1; i <= a; ++i) {
        if (i == 1 || i == a) {
            continue;
        } else if (a % i == 0) {
            return 0;
        }
    }

    return 1;
}


int main(void)
{
    /* The main program function */
    int i = 0;
    
    for (i = 0; i <= 100; ++i) {
        if (prime_check(i) == 1) {
            printf("%i is a prime!\n", i);
        }
    }

    
    return 0;
}
