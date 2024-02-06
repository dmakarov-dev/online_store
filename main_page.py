class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("Available Products:")
        for index, product in enumerate(self.products, start=1):
            print(f"{index}. {product.name} - ${product.price} ({product.quantity} available)")

    def buy_product(self, index, quantity):
        selected_product = self.products[index - 1]

        if selected_product.quantity >= quantity:
            total_cost = selected_product.price * quantity
            print(f"Total cost: ${total_cost}")
            selected_product.quantity -= quantity
            print(f"You have successfully purchased {quantity} {selected_product.name}(s)!")
        else:
            print("Sorry, the selected quantity is not available.")

# Sample usage
if __name__ == "__main__":
    store = Store()

    product1 = Product("Laptop", 800, 10)
    product2 = Product("Headphones", 50, 20)
    product3 = Product("Mouse", 20, 30)

    store.add_product(product1)
    store.add_product(product2)
    store.add_product(product3)

    while True:
        print("\nWelcome to the Simple Store!")
        store.display_products()

        try:
            choice = int(input("Enter the product number you want to buy (0 to exit): "))
            if choice == 0:
                break
            elif 0 < choice <= len(store.products):
                quantity = int(input("Enter the quantity you want to buy: "))
                store.buy_product(choice, quantity)
            else:
                print("Invalid product number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Thank you for shopping with us!")
