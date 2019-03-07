/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Script: struct_tree.c
 * Desc: Traverses a tree structure using C.
 * Date: Dec-2018 */
    
// Library Imports //
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    char *seq;
    struct node *left_child;
    struct node *right_child;
} node;

struct node* newNode(int data) {
    struct node* node = (struct node*) malloc(sizeof(struct node));

    node -> data = data;
    node -> left_child = NULL;
    node -> right_child = NULL;
    return node;
}

struct node* leaf(char *seq) {
    struct node* node = (struct node*) malloc(sizeof(struct node));

    node -> seq = seq;
    return node;
}

void temptree()
{
    char sequence[] = "A";
    struct node *root = newNode(0);
    root -> left_child = leaf(sequence);
    root -> right_child = newNode(0);

}

int main(void)
{
    // create root
    /*
    struct node *root = newNode(1);
    root -> left_child = newNode(2);
    root -> right_child = newNode(3);
    root -> left_child -> left_child = newNode(4); 

     * will look something like this
     *          / 1 \
     *         /     \
     *        2       3
     *       / \     / \
     *      4  NULL NULL NULL
     *     / \
     *  Null  NULL
     */

    temptree();
    
    return 0;
}  
