/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: structures_1.c
 * Desc: Shows the use of structures for a student register
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

typedef struct Product {
    char *name;
    int stock;
    float price;
} Product;

void itemsold(struct Product *ptr)
{
    if ((*ptr).stock < 1) {
        return;
    }
    (*ptr).stock--;
}


int main(void)
{
    struct Product p1;
    p1.name = "Iphone 6";
    p1.stock = 200;
    p1.price = 500.00;

    // make a pointer and assign to it p1
    struct Product *ptr;
    ptr = &p1;

    printf("Name: %s\nStock: %i\nPrice: %f\n", p1.name, p1.stock, p1.price);

    itemsold(ptr);
    printf("Name: %s\nStock: %i\nPrice: %f\n", p1.name, p1.stock, p1.price);

    return 0;
}
