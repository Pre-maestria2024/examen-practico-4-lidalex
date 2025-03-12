from collections import defaultdict
from queue import PriorityQueue, Queue

def build_tree(edges, n):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    return tree

def dfs(tree, node, parent, path, paths):
    path.append(node)
    if len(tree[node]) == 1 and tree[node][0] == parent:
        paths.append(path.copy())
    else:
        for neighbor in tree[node]:
            if neighbor != parent:
                dfs(tree, neighbor, node, path, paths)
    path.pop()

def find_all_paths(tree, root):
    paths = []
    dfs(tree, root, -1, [], paths)
    return paths

def backtrack(paths, k, used, index, groups, best_groups):
    if index >= len(paths):
        if len(groups) > len(best_groups[0]):
            best_groups[0] = groups.copy()
        return
    
    path = paths[index]
    i = 0
    while i + k <= len(path):
        group = path[i:i + k]
        if all(node not in used for node in group):
            for node in group:
                used.add(node)
            groups.append(group)
            backtrack(paths, k, used, index + 1, groups, best_groups)
            groups.pop()
            for node in group:
                used.remove(node)
        i += 1
    
    backtrack(paths, k, used, index + 1, groups, best_groups)

def max_groups(paths, k):
    used = set()
    best_groups = [[]]
    backtrack(paths, k, used, 0, [], best_groups)
    return len(best_groups[0]), best_groups[0]

def main():
    n, k = map(int, input().split())
    edges = []
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    tree = build_tree(edges, n)
    paths = find_all_paths(tree, 0)
    num_groups, groups = max_groups(paths, k)
    return num_groups, groups

if __name__ == '__main__':
    main()
