from queue import PriorityQueue
from queue import Queue

def main():
    import sys
    from collections import defaultdict

    n, k = map(int, sys.stdin.readline().split())
    if n == 0 or k == 0:
        print(0)
        return
    tree = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        tree[u].append(v)
        tree[v].append(u)

    root = 0
    parent = {}
    children = defaultdict(list)
    visited = set([root])
    q = Queue()
    q.put(root)

    while not q.empty():
        u = q.get()
        for v in tree[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                children[u].append(v)
                q.put(v)

    # Post-order traversal iterativo
    post_order = []
    stack = [(root, False)]
    while stack:
        node, processed = stack.pop()
        if processed:
            post_order.append(node)
        else:
            stack.append((node, True))
            for child in reversed(children[node]):
                stack.append((child, False))

    chain = [0] * n
    groups = [0] * n

    for u in post_order:
        max_chain = 0
        total_groups = 0
        for v in children[u]:
            if chain[v] > max_chain:
                max_chain = chain[v]
            total_groups += groups[v]
        current_chain = 1 + max_chain
        num_groups = current_chain // k
        remaining_chain = current_chain % k
        chain[u] = remaining_chain
        groups[u] = total_groups + num_groups

    print(groups[root])

if __name__ == '__main__':
    main()
