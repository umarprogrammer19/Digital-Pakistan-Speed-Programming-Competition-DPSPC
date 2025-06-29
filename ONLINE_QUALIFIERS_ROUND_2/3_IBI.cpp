#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

class TreeNode
{
public:
    char value;
    TreeNode *left_child;
    TreeNode *right_child;

    TreeNode(char val)
    {
        value = val;
        left_child = nullptr;
        right_child = nullptr;
    }
};

TreeNode *construct_tree(const string &bin_string)
{
    if (bin_string.empty())
        return nullptr;

    TreeNode *root_node = new TreeNode(bin_string[0]);
    vector<TreeNode *> queue;
    queue.push_back(root_node);

    for (size_t i = 1; i < bin_string.size(); ++i)
    {
        TreeNode *new_node = new TreeNode(bin_string[i]);
        TreeNode *current = queue.back();

        if (bin_string[i] == '0')
        {
            current->left_child = new_node;
        }
        else
        {
            current->right_child = new_node;
        }

        queue.push_back(new_node);
    }

    return root_node;
}

void traverse_inorder(TreeNode *node, string &output)
{
    if (!node)
        return;
    traverse_inorder(node->left_child, output);
    output += node->value;
    traverse_inorder(node->right_child, output);
}

int binary_to_decimal(const string &binary_str)
{
    int result = 0;
    for (char ch : binary_str)
    {
        result = result * 2 + (ch - '0');
    }
    return result;
}

int process_number(int num)
{
    string binary;
    while (num > 0)
    {
        binary = char('0' + (num % 2)) + binary;
        num /= 2;
    }

    TreeNode *tree_root = construct_tree(binary);

    string traversal_result;
    traverse_inorder(tree_root, traversal_result);

    return binary_to_decimal(traversal_result);
}

int main()
{
    int number;
    cin >> number;
    cout << process_number(number) << endl;
    return 0;
}
