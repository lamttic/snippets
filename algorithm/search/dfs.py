def dfs(graph, root):
    stack = [root]
    visited = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(list(graph[node])))

    return visited


if __name__ == '__main__':
    graph = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
    root_node = 1

    print([1,3,5,2,4,6] == dfs(graph, root_node))
