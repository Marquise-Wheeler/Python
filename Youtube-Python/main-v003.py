class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):
    # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

    # Assign self object
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price =  self.price * self.pay_rate

item1 = Item("Phone", 1000, 5)

item2 = Item("Laptop", 1000, 3)
item2.has_numpad = False

item3 = Item("Monitor",300, 3)

print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.calculate_total_price())

print(item2.name)
print(item2.price)
print(item2.quantity)
print(item2.calculate_total_price())

print(item3.name)
print(item3.price)
print(item3.quantity)
print(item3.calculate_total_price())

# Convert attribures to a Dictionary
print(Item.__dict__) # All the attributes for the Class level
print(item1.__dict__) # All the attributes for the Instance level
print(item2.__dict__) # All the attributes for the Instance level
print(item3.__dict__) # All the attributes for the Instance level

# Test function apply_discount
item1 = Item("Phone", 1000, 5)
item1.apply_discount()
print(item1.price)


item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)


