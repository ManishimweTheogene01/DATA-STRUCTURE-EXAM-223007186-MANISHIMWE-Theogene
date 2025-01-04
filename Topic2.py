#Topic2:Implement Queue and Circular Linked List to manage data in the volunteer management system for ngos.
#Queue
class VolunteerQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, volunteer):
        """Add a volunteer to the queue."""
        self.queue.append(volunteer)

    def dequeue(self):
        """Remove and return the volunteer at the front of the queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty!"

    def peek(self):
        """Return the volunteer at the front without removing them."""
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty!"

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def display(self):
        """Display all volunteers in the queue."""
        if self.is_empty():
            return "Queue is empty!"
        return " -> ".join(self.queue)


# Example Usage
queue = VolunteerQueue()
queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Charlie")

print("Current Queue:", queue.display())  
print("Processing:", queue.dequeue())   
print("Updated Queue:", queue.display())

#Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def add_event(self, event):
        """Add an event to the circular linked list."""
        new_node = Node(event)
        if not self.tail:
            self.tail = new_node
            self.tail.next = new_node  
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def display_events(self, count=10):
        """Display the events in the circular linked list."""
        if not self.tail:
            return "No events scheduled!"
        events = []
        current = self.tail.next
        for _ in range(count):  
            events.append(current.data)
            current = current.next
            if current == self.tail.next:
                break
        return " -> ".join(events)

    def next_event(self):
        """Move to the next event."""
        if not self.tail:
            return "No events scheduled!"
        self.tail = self.tail.next
        return self.tail.data

# Example Usage
event_schedule = CircularLinkedList()
event_schedule.add_event("Cleanup Drive")
event_schedule.add_event("Tree Plantation")
event_schedule.add_event("Food Distribution")

print("Scheduled Events:", event_schedule.display_events())  
print("Next Event:", event_schedule.next_event())            
print("Next Event:", event_schedule.next_event())            
print("Next Event:", event_schedule.next_event())          





    

   
    