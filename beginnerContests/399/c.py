from typing import List, Tuple

def find(parents: List[int], node: int) -> int:
    if parents[node] != node:
        parents[node] = find(parents, parents[node])
    return parents[node]


def unite(parents: List[int], heights: List[int], first: int, second: int) -> bool:
    root_first = find(parents, first)
    root_second = find(parents, second)
    if root_first == root_second:
        return False
    
    if heights[root_first] < heights[root_second]:
        parents[root_first] = root_second
    else:
        parents[root_second] = root_first
        if heights[root_first] == heights[root_second]:
            heights[root_first] += 1
    
    return True

def count_removable_edges(node_count: int, edges: List[Tuple[int, int]]) -> int:
    parents = list(range(node_count + 1))
    heights = [0] * (node_count + 1)
    remove_count = 0
    
    for src, dst in edges:
        if not unite(parents, heights, src, dst):
            remove_count += 1
    
    return remove_count

node_count, edge_count = map(int, input().split())
edges = []
for _ in range(edge_count):
    src, dst = map(int, input().split())
    edges.append((src, dst))

result = count_removable_edges(node_count, edges)
print(result)
