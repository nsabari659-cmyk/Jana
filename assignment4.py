#assignment4 billing machine

# class Product:
#     def __init__(self, name, price, quantity):
#         self.__name = name
#         self.__price = price
#         self.__quantity = quantity

#     def get_name(self):
#         return self.__name

#     def get_price(self):
#         return self.__price

#     def get_quantity(self):
#         return self.__quantity

#     def apply_discount(self):
#         return 0

#     def get_category(self):
#         return "General"


# class GroceryProduct(Product):
#     def apply_discount(self):
#         return self.get_price() * self.get_quantity() * 0.05

#     def get_category(self):
#         return "Grocery"


# class ElectronicsProduct(Product):
#     def apply_discount(self):
#         return self.get_price() * self.get_quantity() * 0.10

#     def get_category(self):
#         return "Electronics"


# class ClothingProduct(Product):
#     def apply_discount(self):
#         return self.get_price() * self.get_quantity() * 0.15

#     def get_category(self):
#         return "Clothing"


# class LoyaltyTier:
#     def __init__(self, name, discount):
#         self.name = name
#         self.discount = discount

#     def apply_discount(self, amount):
#         return amount * self.discount / 100


# class Regular(LoyaltyTier):
#     def __init__(self):
#         super().__init__("Regular", 0)


# class Silver(LoyaltyTier):
#     def __init__(self):
#         super().__init__("Silver", 5)


# class Gold(LoyaltyTier):
#     def __init__(self):
#         super().__init__("Gold", 10)


# class BillingEngine:
#     def __init__(self, cart, loyalty):
#         self.cart = cart
#         self.loyalty = loyalty

#     def generate_bill(self):
#         subtotal = 0
#         product_discount = 0

#         print("\n========== RETAIL STORE BILL ==========")

#         for product in self.cart:
#             amount = product.get_price() * product.get_quantity()
#             discount = product.apply_discount()
#             final_amount = amount - discount

#             subtotal += amount
#             product_discount += discount

#             print("\nProduct:", product.get_name())
#             print("Category:", product.get_category())
#             print("Price: Rs.", product.get_price())
#             print("Quantity:", product.get_quantity())
#             print("Amount: Rs.", round(amount, 2))
#             print("Discount: Rs.", round(discount, 2))
#             print("Final Amount: Rs.", round(final_amount, 2))

#         amount_after_discount = subtotal - product_discount
#         loyalty_discount = self.loyalty.apply_discount(
#             amount_after_discount
#         )
#         grand_total = amount_after_discount - loyalty_discount

#         print("\n---------------------------------------")
#         print("Subtotal: Rs.", round(subtotal, 2))
#         print("Product Discount: Rs.", round(product_discount, 2))
#         print("Loyalty Tier:", self.loyalty.name)
#         print("Loyalty Discount: Rs.", round(loyalty_discount, 2))
#         print("Grand Total: Rs.", round(grand_total, 2))
#         print("=======================================")


# cart = []

# number_of_products = int(input("Enter number of products: "))

# for i in range(number_of_products):
#     print("\nProduct", i + 1)
#     name = input("Enter product name: ")
#     price = float(input("Enter product price: "))
#     quantity = int(input("Enter quantity: "))

#     print("Select category:")
#     print("1. Grocery")
#     print("2. Electronics")
#     print("3. Clothing")

#     category = input("Enter category choice(Grocery,Electronics,clothing): ")

#     if category == "1":
#         product = GroceryProduct(name, price, quantity)

#     elif category == "2":
#         product = ElectronicsProduct(name, price, quantity)

#     elif category == "3":
#         product = ClothingProduct(name, price, quantity)

#     else:
#         print("Invalid category. Product added as General.")
#         product = Product(name, price, quantity)

#     cart.append(product)



# print("\nSelect Loyalty Tier")
# print("1. Regular - 0% discount")
# print("2. Silver - 5% discount")
# print("3. Gold - 10% discount")

# tier = input("Enter loyalty tier: ")

# if tier == "2":
#     loyalty = Silver()

# elif tier == "3":
#     loyalty = Gold()

# else:
#     loyalty = Regular()



# billing = BillingEngine(cart, loyalty)
# billing.generate_bill()