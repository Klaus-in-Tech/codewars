def tree_by_levels(node):
    if not node:
        return []
    result,q,curr_level = [],[],0
    q.append(node)
    while q:
        len_q = len(q)
        result.append([])
        for _ in range(len_q):
            root = q.pop(0)
            result[curr_level].append(root.value)
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
        curr_level+=1
    return [item for sublist in result for item in sublist]