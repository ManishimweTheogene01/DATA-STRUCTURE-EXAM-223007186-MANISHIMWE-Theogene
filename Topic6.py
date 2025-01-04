# Topic 6: Implement a tree to represent hierarchical data in the volunteer management system for ngos.

class Volunteer:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}"

class TreeNode:
    def __init__(self, data):
        self.data = data  
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_name):
        self.children = [child for child in self.children if child.data.name != child_name]

    def __str__(self, level=0):
        representation = " " * (level * 2) + str(self.data) + "\n"
        for child in self.children:
            representation += child.__str__(level + 1)
        return representation

class VolunteerHierarchy:
    def __init__(self):
        self.root = None

    def set_root(self, volunteer):
        self.root = TreeNode(volunteer)

    def find_node(self, current_node, name):
        if current_node.data.name == name:
            return current_node
        for child in current_node.children:
            result = self.find_node(child, name)
            if result:
                return result
        return None

    def add_volunteer(self, supervisor_name, volunteer):
        if not self.root:
            print("Error: Root volunteer not set.")
            return
        supervisor_node = self.find_node(self.root, supervisor_name)
        if supervisor_node:
            supervisor_node.add_child(TreeNode(volunteer))
            print(f"Volunteer {volunteer.name} added under supervisor {supervisor_name}.")
        else:
            print(f"Error: Supervisor {supervisor_name} not found.")

    def remove_volunteer(self, name):
        if not self.root:
            print("Error: Tree is empty.")
            return
        if self.root.data.name == name:
            print("Error: Cannot remove the root volunteer.")
            return
        parent_node = self.find_parent(self.root, name)
        if parent_node:
            parent_node.remove_child(name)
            print(f"Volunteer {name} removed successfully.")
        else:
            print(f"Error: Volunteer {name} not found.")

    def find_parent(self, current_node, child_name):
        for child in current_node.children:
            if child.data.name == child_name:
                return current_node
            result = self.find_parent(child, child_name)
            if result:
                return result
        return None

    def display_hierarchy(self):
        if not self.root:
            print("The hierarchy is empty.")
        else:
            print(self.root)

# Example usage
if __name__ == "__main__":
    vh = VolunteerHierarchy()

    vh.set_root(Volunteer("Alice", "Director"))

    vh.add_volunteer("Alice", Volunteer("Bob", "Manager"))
    vh.add_volunteer("Bob", Volunteer("Charlie", "Coordinator"))
    vh.add_volunteer("Alice", Volunteer("Daisy", "Manager"))

    print("Hierarchy:")
    vh.display_hierarchy()

    vh.remove_volunteer("Charlie")

    print("\nHierarchy after removal:")
    vh.display_hierarchy()
