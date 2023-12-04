from shoplist import FoodOrder

def create_order_list():
    order_list = []
    while True:
        try:
            num_items = int(input("How many items will you order today? "))
            if num_items >= 1:
                break
            else:
                print("Number of items must be at least 1.")
        except ValueError:
            print("Please enter a valid number.")

    for i in range(num_items):
        print(f"Item #{i + 1} - ")
        food_name = input("Enter food: ")
        while True:
            try:
                amount = float(input("Enter amount of pounds: "))
                if amount > 0:
                    break
                else:
                    print("Amount of pounds must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")

        food_order = FoodOrder(food_name, amount)
        order_list.append(food_order)

    return order_list

def display_order_list(order_list):
    for item in order_list:
        print(item)
        print()

def calculate_total_cost(order_list):
    total_cost = sum(item.get_calculated_price() for item in order_list)
    return total_cost

def main():
    orders = create_order_list()
    print("\nHere's a summary of the items purchased:")
    display_order_list(orders)
    total_cost = calculate_total_cost(orders)
    print(f"Total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
