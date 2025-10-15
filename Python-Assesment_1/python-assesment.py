import datetime

inventory = {
    "Paracetamol": {"price": 20, "stock": 50},
    "Amoxicillin": {"price": 50, "stock": 30},
    "Cough Syrup": {"price": 80, "stock": 25}
}


def view_inventory():
    print("\n--- Current Medicine Inventory ---")
    print("Medicine\tPrice\tStock")
    print("-" * 30)
    for med in inventory:
        price = inventory[med]['price']
        stock = inventory[med]['stock']
        print(f"{med}\t{price}\t{stock}")
    print("-" * 30)


def update_inventory():
    med_name = input("\nEnter medicine name: ").strip().title()
    try:
        price = int(input("Enter price per unit: "))
        qty = int(input("Enter quantity to add/update: "))

  
        for name in inventory:
            if name == med_name:
                inventory[name]['stock'] += qty  
                inventory[name]['price'] = price 
                print(f"{name} stock updated successfully!")
                return 


        inventory[med_name] = {"price": price, "stock": qty}
        print(f"{med_name} added successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric values for price and quantity.")



def process_sale():
    customer = input("Enter customer name: ").title()
    med_name = input("Enter medicine name: ").strip().title()

    # found_med = None
    for name in inventory:
        if name == med_name:
            med_name = name
            break

    if med_name not in inventory:
        print("Medicine not found in inventory!")
        return
    
    try:
        qty = int(input("Enter quantity to purchase: "))
        if qty <= 0:
            print("Quantity must be positive.")
            return
        if qty > inventory[med_name]['stock']:
            print("Not enough stock available!")
            return

        price = inventory[med_name]['price']
        total = qty * price
        inventory[med_name]['stock'] -= qty
        date = datetime.date.today()

        print("\n--- Sale Bill ---")
        print(f"Customer Name : {customer}")
        print(f"Date          : {date}")
        print(f"Medicine Name : {med_name}")
        print(f"Quantity      : {qty}")
        print(f"Price/Unit    : ₹{price}")
        print(f"Total Amount  : ₹{total}")
        print("-----------------------------")
        print("Sale recorded successfully!\n")

    except ValueError:
        print("Invalid quantity entered!")


def main():
    while True:
        print("\n====== QuickMed MediTrack ======")
        print("1. View Inventory")
        print("2. Add/Update Medicine")
        print("3. Process a Sale")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_inventory()
        elif choice == '2':
            update_inventory()
        elif choice == '3':
            process_sale()
        elif choice == '4':
            print("\nThank you for using MediTrack! ")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

main()
