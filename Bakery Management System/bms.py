from customers import Customer
import pandas as pd
class BakeryManagementSystem:
    def __init__(self):
        self.customers = []
    
    def add_customers(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} has been added")

    def display_customers(self):
        print("List of customers:")
        for customer in self.customers:
            print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}")

    def save_to_excel(self):
        data = {'Customer_ID': [], 'Name': [], 'Email': [], 'Phone': [], 'Order': []}
        for customer in self.customers:
            data['Customer_ID'].append(customer.id)
            data['Name'].append(customer.name)
            data['Email'].append(customer.email)
            data['Phone'].append(customer.phone)
            data['Order'].append(customer.order)

        df = pd.DataFrame(data)
        df.to_excel("Bakery_Order.xlsx", index=False)
        print("Data saved to 'Bakery_Order.xlsx'.")
