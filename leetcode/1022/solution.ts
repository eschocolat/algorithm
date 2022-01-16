/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function sumRootToLeaf(root: TreeNode | null): number {
  return dfs(root, 0);
}

function dfs(node: TreeNode, cur: number) {
  if (!node) {
    return 0;
  }
  const sum = (cur << 1) + node.val;
  if (node.left == null && node.right == null) {
    return sum;
  }
  return dfs(node.left, sum) + dfs(node.right, sum);
}
