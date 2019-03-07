/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: structs_1.c
 * Desc: Another example of using structs.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char* team;
    int*  total_power;
} players;

typedef struct {
        char* name;
        int age;
        int power;
        players* team;
} person;

void loose_power(person *ptr)
{
    int old_power = (*ptr).power;
    (*ptr).power = old_power - 10;
    
}

int main(void)
{
    // assign things to the struct
    person p1;
    person *p1_ptr = &p1;
    players = p11;

    p1.age = 32;
    p1.name = "Joe";
    p1.power = 100;


    return 0;
}

// There is no dynamic memory allocation in this script! it is unsafe.
// how do I get the memory allocated?
