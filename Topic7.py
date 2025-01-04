#Topic 7: Use Selection Sort to sort the volunteer management system for ngos data based on priority.

class Volunteer:
    def __init__(self, name, age, priority):
        self.name = name
        self.age = age
        self.priority = priority  

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Priority: {self.priority}"

class VolunteerManagement:
    def __init__(self):
        self.volunteers = []

    def add_volunteer(self, name, age, priority):
        volunteer = Volunteer(name, age, priority)
        self.volunteers.append(volunteer)
        print(f"Volunteer {name} added successfully.")

    def selection_sort_by_priority(self):
        n = len(self.volunteers)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.volunteers[j].priority < self.volunteers[min_index].priority:
                    min_index = j
            self.volunteers[i], self.volunteers[min_index] = self.volunteers[min_index], self.volunteers[i]
        print("Volunteers sorted by priority successfully.")

    def list_volunteers(self):
        if not self.volunteers:
            print("No volunteers to display.")
        else:
            print("Listing all volunteers:")
            for volunteer in self.volunteers:
                print(volunteer)

# Example usage
if __name__ == "__main__":
    vms = VolunteerManagement()

    vms.add_volunteer("Alice", 30, 3)
    vms.add_volunteer("Bob", 25, 1)
    vms.add_volunteer("Charlie", 35, 2)

    print("Unsorted Volunteers:")
    vms.list_volunteers()

    vms.selection_sort_by_priority()

    print("\nSorted Volunteers by Priority:")
    vms.list_volunteers()
