class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category = self.categorize_product()

    def categorize_product(self):
        if self.price >= 1000:
            return "Expensive"
        else:
            return "Affordable"

    def display_details(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Price: ₹", self.price)
        print("Category:", self.category)
        print("------------------------")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        print("\nProduct Inventory")
        print("========================")

        for product in self.products:
            product.display_details()


inventory = Inventory()


product1 = Product(101, "Laptop", 55000)
product2 = Product(102, "Keyboard", 800)
product3 = Product(103, "Mobile Phone", 25000)
product4 = Product(104, "Mouse", 500)


inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)
inventory.add_product(product4)


inventory.display_all_products()


#OUTPUT
#Product Inventory
#========================
#Product ID: 101
#Product Name: Laptop
#Price: ₹ 55000
#Category: Expensive
#------------------------
#Product ID: 102
#Product Name: Keyboard
#Price: ₹ 800
#Category: Affordable
#------------------------
#Product ID: 103
#Product Name: Mobile Phone
#Price: ₹ 25000
#Category: Expensive
#------------------------
#Product ID: 104
#Product Name: Mouse
#Price: ₹ 500
#Category: Affordable
#------------------------


