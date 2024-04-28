#include <iostream>
using namespace std;

class node
{
public:
    int data;
    node *left, *right;
};

class BST
{
public:
    node *root;
    void create(node *&);
    void insert(node *&, node *);
    void search(node *, int);
    int longestPath(node *);
    int small(node *);
    void swapNodes(node *);
    void inorder(node *);
    BST()
    {
        root = NULL;
    }
};

void BST::create(node *&root)
{
    int data;
    cout << "Enter data for the node: ";
    cin >> data;
    node *temp = new node;
    temp->data = data;
    temp->left = NULL;
    temp->right = NULL;
    if (root == NULL)
    {
        root = temp;
    }
    else
        insert(root, temp);
}

void BST::insert(node *&root, node *temp)
{
    if (root->data > temp->data)
    {
        if (root->left == NULL)
            root->left = temp;
        else
            insert(root->left, temp);
    }
    else
    {
        if (root->right == NULL)
            root->right = temp;
        else
            insert(root->right, temp);
    }
}

void BST::search(node *root, int key)
{
    if (root == NULL)
    {
        cout << "Element not found";
        return;
    }
    if (root->data == key)
        cout << "Element Found";
    else if (root->data > key)
        search(root->left, key);
    else
        search(root->right, key);
}

int BST::longestPath(node *root)
{
    if (root == NULL)
        return 0;
    int L = longestPath(root->left);
    int R = longestPath(root->right);
    if (L > R)
        return (L + 1);
    else
        return (R + 1);
}

int BST::small(node *root)
{
    if (root == NULL)
        throw std::invalid_argument("Tree is empty");
    while (root->left != NULL)
    {
        root = root->left;
    }
    return (root->data);
}

void BST::swapNodes(node *root)
{
    if (root == NULL)
        return;
    node *temp = root->left;
    root->left = root->right;
    root->right = temp;
    swapNodes(root->left);
    swapNodes(root->right);
}

void BST::inorder(node *root)
{
    if (root == NULL)
        return;
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

int main()
{
    node *r = NULL;
    BST tree;
    tree.create(r);
    int n, k;
    char ch;
    cout << "Enter number of nodes you want to insert: ";
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        tree.create(r);
    }
    cout << "\nThe no. of nodes on the longest path: " << tree.longestPath(r) << endl;
    cout << "Minimum data value in tree: " << tree.small(r) << endl;
    cout << "\nBefore swapping nodes: ";
    tree.inorder(r);
    cout << endl;
    tree.swapNodes(r);
    cout << "After swapping nodes: ";
    tree.inorder(r);
    cout << endl;
    tree.swapNodes(r);
    do
    {
        cout << "\nEnter the key you want to search: ";
        cin >> k;
        tree.search(r, k);
        cout << "\nDo you want to search again?";
        cin >> ch;
    } while (ch == 'y');
    return 0;
}