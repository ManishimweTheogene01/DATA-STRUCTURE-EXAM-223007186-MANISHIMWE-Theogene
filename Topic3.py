#Topic3: Implement Array for volunteer management system for ngos processing.
class Volunteer:
    def __init__(self, name, age, contact, skills):
        self.name = name
        self.age = age
        self.contact = contact
        self.skills = skills

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Contact: {self.contact}, Skills: {', '.join(self.skills)}"

class VolunteerArrayManagement:
    def __init__(self, max_volunteers):
        self.volunteers = [None] * max_volunteers  
        self.max_volunteers = max_volunteers
        self.current_count = 0

    def add_volunteer(self, name, age, contact, skills):
        if self.current_count >= self.max_volunteers:
            print("Error: Cannot add more volunteers. Array is full.")
            return
        self.volunteers[self.current_count] = Volunteer(name, age, contact, skills)
        self.current_count += 1
        print(f"Volunteer {name} added successfully.")

    def remove_volunteer(self, name):
        for i in range(self.current_count):
            if self.volunteers[i] and self.volunteers[i].name == name:
                print(f"Volunteer {name} removed successfully.")
                self.volunteers[i] = None  
                self._compact_array()  
                self.current_count -= 1
                return
        print(f"Error: Volunteer {name} not found.")

    def _compact_array(self):
        new_array = [None] * self.max_volunteers
        new_index = 0
        for i in range(self.max_volunteers):
            if self.volunteers[i] is not None:
                new_array[new_index] = self.volunteers[i]
                new_index += 1
        self.volunteers = new_array

    def list_volunteers(self):
        if self.current_count == 0:
            print("No volunteers found.")
        else:
            print("Listing all volunteers:")
            for i in range(self.current_count):
                print(self.volunteers[i])

    def find_volunteer(self, name):
        for i in range(self.current_count):
            if self.volunteers[i] and self.volunteers[i].name == name:
                print("Volunteer found:")
                print(self.volunteers[i])
                return
        print(f"Error: Volunteer {name} not found.")

# Example usage
if __name__ == "__main__":
    vams = VolunteerArrayManagement(max_volunteers=5)  


    vams.add_volunteer("Alice", 30, "alice@gmail.com", ["Teaching", "Fundraising"])
    vams.add_volunteer("Bob", 25, "bob@gmail.com", ["Cooking", "Event Management"])

    vams.list_volunteers()

    vams.find_volunteer("Alice")

    vams.remove_volunteer("Alice")

    vams.list_volunteers()

    vams.add_volunteer("Charlie", 22, "charlie@gmail.com", ["Logistics"])
    vams.add_volunteer("Daisy", 29, "daisy@gmail.com", ["First Aid"])
    vams.add_volunteer("Edward", 34, "edward@gmail.com", ["Technical Support"])
    vams.add_volunteer("Frank", 40, "frank@gmail.com", ["Driving"])
    vams.add_volunteer("Grace", 28, "grace@gmail.com", ["Coordination"])

    vams.list_volunteers()