/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: linkedlist.c
 * Desc: Shows the use of a linked list.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

// Define structure
typedef struct Node {
    int data;
    struct Node* next;
} node_t;

int get_list_len(node_t* nd)
{
    int count = 0;
    while (nd != NULL) {
        count++;
        nd = nd -> next;
    }
    return count;
}

void insert_item(node_t** nd, int new_data)
{
    node_t* new_nd = malloc(sizeof(node_t));
    new_nd -> data = new_data;
    new_nd -> next = (*nd);
    (*nd) = new_nd;
}

int main(void)
{
    node_t* n1 = NULL;
    int result = 0;
    insert_item(&n1, 100);
    result = get_list_len(n1);
    printf("%i\n", result);


    

    return 0;
}
