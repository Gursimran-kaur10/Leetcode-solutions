# Last element of postorder is root
        root_val = postorder[-1]

        # Create root node
        root = TreeNode(root_val)

        # Find root in inorder
        index = inorder.index(root_val)

        # Left subtree
        left_inorder = inorder[:index]

        # Right subtree
        right_inorder = inorder[index + 1:]

        # Number of elements in left subtree
        left_size = len(left_inorder)

        # Construct left subtree
        root.left = self.buildTree(
            left_inorder,
            postorder[:left_size]
        )

        # Construct right subtree
        root.right = self.buildTree(
            right_inorder,
            postorder[left_size:-1]
        )

        return root
