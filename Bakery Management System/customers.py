from datetime import datetime, timedelta
class Customer:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.orders = []

    def place_order(self, product, quantity):
        order = {
            'product': product,
            'quantity' : quantity,
            'order_date' : datetime.now(),
            'modifiable_until' : datetime.now() + timedelta(minutes=5)
        }
        self.orders.append(order)
        print(f"Order placed successfully!\n{order}")

    def display_order(self):
        print(f"Order for {self.name}")
        for order in self.orders:
            print(f"Product: {order['product']}, Quantity: {order['quantity']}, Order Date: {order['order_date']}")

    def modify_order(self, order_index, new_quantity):
        order = self.orders[order_index]
        if datetime.now() <= order['modifiable_until']:
            order['quantity'] = new_quantity
            print(f"Order modified successfully!\n{order}")
        else:
            print(f"Order modification time expired")

