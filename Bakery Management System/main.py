from bms import BakeryManagementSystem 
from customers import Customer
def main():
    bakery_system = BakeryManagementSystem()
    while True:
        print("\nBakery Management System")
        print("1. Add Customer")
        print("2. Place Order")
        print("3. Display Orders")
        print("4. Modify Order")
        print("5. Display Customers")
        print("6. Save to Excel")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            customer_id = input("Enter Customer ID: ")
            name = input("Enter Customer Name: ")
            email = input("Enter Customer Email: ")
            phone = input("Enter Customer Phone: ")

            new_customer = Customer(customer_id, name, email, phone)
            bakery_system.add_customers(new_customer)

        elif choice == "2":
            customer_id = input("Enter Customer ID: ")
            product = input("Enter Product: ")
            try:
                quantity = int(input("Enter Quantity: "))
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")
                continue

            customer = next((c for c in bakery_system.customers if c.id == customer_id), None)
            if customer:
                customer.place_order(product, quantity)
            else:
                print("Customer not found.")

        elif choice == "3":
            customer_id = input("Enter Customer ID: ")
            customer = next((c for c in bakery_system.customers if c.id == customer_id), None)
            if customer:
                customer.display_order()
            else:
                print("Customer not found.")

        elif choice == "4":
            customer_id = input("Enter Customer ID: ")
            try:
                order_index = int(input("Enter Order Index to Modify: "))
                new_quantity = int(input("Enter New Quantity: "))
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")
                continue

            customer = next((c for c in bakery_system.customers if c.id == customer_id), None)
            if customer:
                customer.modify_order(order_index, new_quantity)
            else:
                print("Customer not found.")

        elif choice == "5":
            bakery_system.display_customers()

        elif choice == "6":
            bakery_system.save_to_excel()

        elif choice == "7":
            print("Exiting Bakery Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
