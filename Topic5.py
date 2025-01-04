#Topic 5: Use Array to track data dynamically in volunteer management system for ngos.

class Volunteer:
    def __init__(self, name, age, contact, skills):
        self.name = name
        self.age = age
        self.contact = contact
        self.skills = skills

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Contact: {self.contact}, Skills: {', '.join(self.skills)}"

class DynamicVolunteerManagement:
    def __init__(self):
        self.volunteers = [] 

    def add_volunteer(self, name, age, contact, skills):
        volunteer = Volunteer(name, age, contact, skills)
        self.volunteers.append(volunteer)
        print(f"Volunteer {name} added successfully.")

    def remove_volunteer(self, name):
        for volunteer in self.volunteers:
            if volunteer.name == name:
                self.volunteers.remove(volunteer)
                print(f"Volunteer {name} removed successfully.")
                return
        print(f"Volunteer {name} not found.")

    def list_volunteers(self):
        if not self.volunteers:
            print("No volunteers found.")
        else:
            print("Listing all volunteers:")
            for volunteer in self.volunteers:
                print(volunteer)

    def find_volunteer(self, name):
        for volunteer in self.volunteers:
            if volunteer.name == name:
                print("Volunteer found:")
                print(volunteer)
                return
        print(f"Volunteer {name} not found.")

    def update_volunteer(self, name, age=None, contact=None, skills=None):
        for volunteer in self.volunteers:
            if volunteer.name == name:
                if age:
                    volunteer.age = age
                if contact:
                    volunteer.contact = contact
                if skills:
                    volunteer.skills = skills
                print(f"Volunteer {name} updated successfully.")
                return
        print(f"Volunteer {name} not found.")

# Example usage
if __name__ == "__main__":
    dvms = DynamicVolunteerManagement()

    dvms.add_volunteer("Alice", 30, "alice@gmail.com", ["Teaching", "Fundraising"])
    dvms.add_volunteer("Bob", 25, "bob@gmail.com", ["Cooking", "Event Management"])

    dvms.list_volunteers()

    dvms.find_volunteer("Alice")

    dvms.update_volunteer("Alice", age=31, contact="alice_new@gmail.com", skills=["Teaching"])

    dvms.list_volunteers()

    dvms.remove_volunteer("Bob")

    dvms.list_volunteers()