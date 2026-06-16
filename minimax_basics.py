
tree = [
    [[1, 10], [3, 4]],
    [[7, 11], [2, 9]]
]




def minimax(tree, is_max_turn):
    if type(tree[0]) == list:
        results = []
        for subtree in tree:
            results.append(minimax(subtree, not is_max_turn))
        
        if is_max_turn:
            return max(results)
        else:
            return min(results)
    else:
        if is_max_turn:
            return max(tree)
        else:
            return min(tree)
        
print(minimax(tree, True))
