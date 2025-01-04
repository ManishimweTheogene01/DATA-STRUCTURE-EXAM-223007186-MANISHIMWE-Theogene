#Topic4: Create Deque to manage a fixed number of orders in the volunteer management system for ngos.

from collections import deque
class Order:
    def __init__(self, order_id, description):
        self.order_id = order_id
        self.description = description

    def __str__(self):
        return f"Order ID: {self.order_id}, Description: {self.description}"

class OrderManagement:
    def __init__(self, max_orders):
        self.orders = deque(maxlen=max_orders) 

    def add_order(self, order_id, description):
        if len(self.orders) == self.orders.maxlen:
            print("Deque is full. The oldest order will be replaced.")
        self.orders.append(Order(order_id, description))
        print(f"Order {order_id} added successfully.")

    def list_orders(self):
        if not self.orders:
            print("No orders available.")
        else:
            print("Listing all orders:")
            for order in self.orders:
                print(order)

    def remove_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                self.orders.remove(order)
                print(f"Order {order_id} removed successfully.")
                return
        print(f"Order {order_id} not found.")

# Example usage
if __name__ == "__main__":
    oms = OrderManagement(max_orders=5)  

    oms.add_order(1, "Order for event supplies")
    oms.add_order(2, "Order for catering services")
    oms.add_order(3, "Order for transport arrangements")
    oms.add_order(4, "Order for medical kits")
    oms.add_order(5, "Order for teaching materials")

    oms.list_orders()

    oms.add_order(6, "Order for promotional materials")

    oms.list_orders()

    oms.remove_order(2)

    oms.list_orders()