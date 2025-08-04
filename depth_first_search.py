def depth_first_search(to_search_dict, start_vertex, target):
    if start_vertex not in to_search_dict or target not in to_search_dict:
        return False, []

    visited = set()  # Keep track of visited vertices to prevent cycles

    def dfs(current_vertex, current_path):
        visited.add(current_vertex)  # Mark as visited
        current_path.append(current_vertex)

        print(
            f"searching for {target} in {current_vertex} \n current path: {current_path}"
        )

        if current_vertex == target:
            return current_path

        for neighbor in to_search_dict[current_vertex]:
            if neighbor not in visited:
                found_path = dfs(neighbor, current_path[:])
                if found_path:
                    return found_path
        return None

    path = dfs(start_vertex, [])
    if path is None:
        return False, []
    else:
        return True, path


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

    to_find = "K"
    root = "A"
    found, path = depth_first_search(test_dict, root, to_find)
    print(f"If {to_find} is in the graph: {found}")
    print(f"The path to {to_find}: {path}")


if __name__ == "__main__":
    main()
