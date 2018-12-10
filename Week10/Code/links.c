/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: links.c
 * Desc: Shows how to make a linked list using structs in c.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

// make a linked struct - inside the the structs set pointers.
typedef struct link {
    int index;
    struct link* next;
    struct link* back;
} link;

void traverse_list(link* s)
{
    printf("Visiting link %i\n", s->index);
    if(s -> next != NULL) {
        traverse_list(s->next);
    }
}


int main(void)
{
    link l1;
    link l2;
    link l3;

    l1.index = 0;
    l1.next = &l2;

    l2.index = 1;
    l2.next = &l3;
    
    l3.index = 2;
    l3.next = NULL;

    traverse_list(&l1);

    
    return 0;
}
