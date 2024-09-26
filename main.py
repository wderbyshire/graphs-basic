from stack import Stack

graph = {
    "A": ["B", "C"],
    "B": ["A", "K"],
    "C": ["A", "D", "F"],
    "D": ["C", "G", "E", "H"],
    "E": ["D"],
    "F": ["C", "G", "J"],
    "G": ["F", "D"],
    "H": ["D", "J"],
    "J": ["F", "H"],
    "K": ["B"]
}

# Depth first traversal
# ------------------------------

# Create a stack
stack_obj = Stack()

# Set the current node to the starting node
current_node = "J"

# Create a visited list containing the starting node
visited_list = [current_node]

# Push starting node to the stack
stack_obj.push(current_node)

# Traversal loop continues until the stack is empty
while stack_obj.get_size() > 0:
    # Create a temporary node that saves the current node for later
    temp_current = current_node

    # Loop through all the current nodes neighbours (in alphabetical order)
    for neighbour in sorted(graph[current_node]):
        # If the neighbour hasn't been visited, set the current node to the neighbour, push it to the stack, append
        # it to the visited list and break out of the loop
        if neighbour not in visited_list:
            current_node = neighbour
            stack_obj.push(current_node)
            visited_list.append(current_node)
            break

    # After the loop has exited, if there has been no change to the current node (no unvisited neighbour was found) then
    # pop the stack and set current node to be the returned node
    if temp_current == current_node:
        current_node = stack_obj.pop()

