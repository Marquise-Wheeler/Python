class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self, x, y):
        return x * y

item1 = Item("Phone", 1000, 5)
item2 = Item("Laptop",1000, 3)
item3 = Item("Monitor",300, 3)

print(item1.name)
print(item1.price)
print(item1.quantity)

print(item2.name)
print(item2.price)
print(item2.quantity)

print(item3.name)
print(item3.price)
print(item3.quantity)

#print(type(item1))          # item
#print(type(item1.name))     # str
#print(type(item1.price))    # int
#print(type(item1.quantity)) # int
