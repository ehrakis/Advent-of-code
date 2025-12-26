with open("2025/day_11/input.txt", "r") as file:
    data = file.read().splitlines()


class Node:
    def __init__(self, name, parent_node=None):
        self.name = name
        self.parent_node = [parent_node]
        self.child_nodes: list[Node] = []
        self.different_paths_to_output = {}

    def _compute_number_of_paths_to_out(self, target, path):
        return sum(
            [
                (
                    (
                        child.get_different_paths_to_output(target, path)
                        if child.name != "out"
                        else 0
                    )
                    if child.name != target
                    else 1
                )
                for child in self.child_nodes
            ]
        )

    def get_different_paths_to_output(self, target, parent_name=None, path=None):
        if path is None:
            path = set()

        if parent_name:
            if (parent_name, str(self.name)) in path:
                return 0
            path.add((parent_name, self.name))

        if not target in self.different_paths_to_output:
            self.different_paths_to_output[target] = (
                self._compute_number_of_paths_to_out(target, path)
            )
        return self.different_paths_to_output[target]

    def find_child(self, child_name):
        if self.name == child_name:
            return True
        return any(child.find_child(child_name) for child in self.child_nodes)


nodes: dict[str, Node] = {}

for line in data:
    node_name, childs = line.split(":")
    childs = childs.strip().split()

    if not node_name in nodes:
        nodes[node_name] = Node(node_name)

    for child_node in childs:
        if not child_node in nodes:
            nodes[child_node] = Node(child_node, parent_node=nodes[node_name])
        nodes[node_name].child_nodes.append(nodes[child_node])

print(
    nodes["svr"].get_different_paths_to_output(target="fft")
    * nodes["fft"].get_different_paths_to_output(target="dac")
    * nodes["dac"].get_different_paths_to_output(target="out")
)
