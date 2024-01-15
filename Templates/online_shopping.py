def main():
    # Create product instances
    product1 = Product(product_id=1, name="Laptop", price=800)
    product2 = Product(product_id=2, name="Headphones", price=50)
    product3 = Product(product_id=3, name="Mouse", price=20)

    # Create customer instances
    customer1 = Customer(customer_id=101, name="Alice")
    customer2 = Customer(customer_id=102, name="Bob")

    # Display product and customer information
    product1.display_info()
    product2.display_info()
    product3.display_info()

    customer1.display_info()
    customer2.display_info()

    # Customers add products to the cart
    customer1.cart.add_to_cart(product1, quantity=2)
    customer1.cart.add_to_cart(product2)

    customer2.cart.add_to_cart(product3, quantity=3)

    # Display the contents of the shopping carts
    customer1.cart.display_cart()
    customer2.cart.display_cart()


if __name__ == "__main__":
    main()
