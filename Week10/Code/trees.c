/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: trees.c
 * Desc: Shows how to make trees using structs.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

// define a structure
typedef struct {
    struct node *left;
    struct node *right;
    int data;
} node;

void add_node_right(node* n)
{
    node branch;
    branch.data = 1;
    n -> right = &branch;
}

int main(void)
{
    node root;
    node *root_ptr = &root;
    // root = malloc(sizeof(node));
    
    root_ptr -> data = 1;

    add_node_right(root_ptr);    

    
    return 0;
}
