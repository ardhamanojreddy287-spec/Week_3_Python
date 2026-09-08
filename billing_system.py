class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        return sum(product.get_total() for product in self.products)

    def calculate_tax(self, tax_rate=18):
        subtotal = self.calculate_subtotal()
        return subtotal * tax_rate / 100

    def calculate_total(self, tax_rate=18):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(tax_rate)
        return subtotal + tax

    def display_bill(self, tax_rate=18):
        print("\n" + "=" * 65)
        print("                       BILL")
        print("=" * 65)

        print(f"{'Product':<25}{'Price':>12}{'Qty':>8}{'Total':>15}")
        print("-" * 65)

        for product in self.products:
            total = product.get_total()
            print(
                f"{product.name:<25}"
                f"₹{product.price:>10.2f}"
                f"{product.quantity:>8}"
                f"₹{total:>13.2f}"
            )

        print("-" * 65)

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(tax_rate)
        grand_total = self.calculate_total(tax_rate)

        print(f"{'Subtotal':<45}₹{subtotal:>13.2f}")
        print(f"{'GST (' + str(tax_rate) + '%)':<45}₹{tax:>13.2f}")
        print(f"{'Grand Total':<45}₹{grand_total:>13.2f}")

        print("=" * 65)


bill = Bill()

product1 = Product("Laptop", 50000, 1)
product2 = Product("Mouse", 800, 2)
product3 = Product("Keyboard", 1500, 1)

bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)

bill.display_bill()