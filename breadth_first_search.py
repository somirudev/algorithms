def breadth_first_search(to_search_dict, start_vertex, target):
    if start_vertex == target:
        return True, 0, [start_vertex]

    queue = [start_vertex]
    visited = {start_vertex}
    nodes_per_depth = [[start_vertex]]
    current_depth = 0

    while queue:
        next_depth_nodes = []
        for _ in range(len(queue)):
            current_vertex = queue.pop(0)
            if current_vertex == target:
                return True, current_depth, nodes_per_depth

            for neighbor in to_search_dict.get(current_vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    next_depth_nodes.append(neighbor)

        if next_depth_nodes:
            nodes_per_depth.append(next_depth_nodes)
            current_depth += 1

    return False, -1, nodes_per_depth


def main():
    test_dict = {
        "A": ["B"],
        "B": ["C", "J", "L", "O", "A"],
        "C": ["D", "B"],
        "D": ["E", "H", "C"],
        "E": ["F", "G", "D"],
        "F": ["E"],
        "G": ["E"],
        "H": ["I", "D"],
        "I": ["H"],
        "J": ["K", "B"],
        "K": ["O", "J"],
        "L": ["M", "N", "B"],
        "M": ["N", "L"],
        "N": ["L", "M"],
        "O": ["P", "B", "K"],
        "P": ["O"],
    }

    to_find = "N"
    root = "A"
    found, depth, path = breadth_first_search(test_dict, root, to_find)
    print(f"If {to_find} is in the graph: {found}")
    print(f"The 'layers' searched for {to_find}: {path}")
    print(f"{to_find} is found at depth: {depth}")


if __name__ == "__main__":
    main()
