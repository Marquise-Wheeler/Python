class Item:
    def __init__(self, name):
        print(f"An instance created: {name}")

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item("Phone")
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))


item2 = Item("Laptop")
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

item3 = Item("Monitor")
item3.name = "Monitor"
item3.price = 300
item3.quantity = 3
print(item3.calculate_total_price(item3.price, item3.quantity))

#print(type(item1))          # item
#print(type(item1.name))     # str
#print(type(item1.price))    # int
#print(type(item1.quantity)) # int
