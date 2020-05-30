def bfs(graph, root):
    queue = [root]
    visited = []

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)

            next_node_list = list(graph[node])
            queue.extend(next_node_list)

    return visited


if __name__ == '__main__':
    graph = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
    root_node = 1

    print([1,3,4,5,2,6] == bfs(graph, root_node))
