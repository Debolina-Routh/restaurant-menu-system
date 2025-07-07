
  
menu = {  
    "Indian": {  
        "Butter Chicken": 250,  
        "Paneer Tikka": 200,  
        "Biryani": 180,  
        "Garlic Naan": 40  
    },  
    "Chinese": {  
        "Hakka Noodles": 150,  
        "Manchurian": 160,  
        "Spring Rolls": 120,  
        "Fried Rice": 140  
    },  
    "Italian": {  
        "Margherita Pizza": 300,  
        "Pasta Alfredo": 280,  
        "Lasagna": 320,  
        "Garlic Bread": 100  
    },  
    "Mexican": {  
        "Tacos": 180,  
        "Burrito": 220,  
        "Nachos with Cheese": 160,  
        "Quesadilla": 200  
    },  
    "Beverages": {  
        "Cold Coffee": 80,  
        "Lemonade": 60,  
        "Masala Chai": 40,  
        "Iced Tea": 70  
    }  
}  
  
DELIVERY_CHARGE = 50  
GST_RATE = 0.18  
  
# Function to display the menu  
def display_menu():
    print("\nWelcome to !! SYMPHONY OF TASTES !! online Restaurant\n")
    for cuisine in menu:
        print(f"-----{cuisine}-----")
        for dish, price in menu[cuisine].items():
            print(f"   - {dish} ... ₹{price}")
        print()
  
# Function to take order from user  
def take_order():  
    order = {}  
    print("\nEnter your order (type 'done' to finish odering):")  
    while True:  
        item = input("Enter dish name: ").strip()  
        if item.lower() == 'done':  
            break  
        found = False  
        for cuisine in menu.values():  
            if item in cuisine:  
                try:  
                    qty = int(input(f"Enter quantity of '{item}': "))  
                    if qty <= 0:  
                        print("Quantity must be greater than 0.")  
                        break  
                    if item in order:  
                        order[item]["quantity"] += qty  
                    else:  
                        order[item] = {"price": cuisine[item], "quantity": qty}  
                    found = True  
                    break  
                except ValueError:  
                    print("Please enter a valid number.")  
                    found = True  
                    break  
        if not found:  
            print("Item not found in menu. Please try again.")  
    return order  
  
# Function to calculate and print bill  
def generate_bill(order):  
    print("\n-------- BILL --------")  
    subtotal = 0  
    for item, details in order.items():  
        price = details["price"]  
        qty = details["quantity"]  
        total = price * qty  
        subtotal += total  
        print(f"{item} x{qty} = ₹{total}")  
      
    gst = subtotal * GST_RATE  
    grand_total = subtotal + gst + DELIVERY_CHARGE  
      
    print(f"\nSubtotal: ₹{subtotal:.2f}")  
    print(f"GST (18%): ₹{gst:.2f}")  
    print(f"Delivery Charges: ₹{DELIVERY_CHARGE}")  
    print(f"Grand Total: ₹{grand_total:.2f}")  
    print("\nThank you for ordering with us ❤!")  
  
# Main function  
if __name__ == "__main__":  
    display_menu()  
    order = take_order()  
    if order:  
        generate_bill(order)  
    else:  
        print("No items ordered.")  