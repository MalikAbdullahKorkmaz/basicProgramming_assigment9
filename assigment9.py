class Product:
    def __init__(self, name, id):
        self.name = name
        self.id = id

def show_products(product_list):
    print("List of products:")
    for i, product in enumerate(product_list):
        print("{}: {} (id: {})".format(i, product.name, product.id))

product_list = []

while True:
    print("\nProduct Menu:")
    print("1. Add product")
    print("2. Delete product")
    print("3. Delete product by id/index")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter product name: ")
        id = len(product_list) + 1
        product = Product(name, id)
        product_list.append(product)
        print("Product added!")

    elif choice == 2:
        show_products(product_list)
        delete_id = int(input("Enter the id of the product to delete: "))
        for product in product_list:
            if product.id == delete_id:
                product_list.remove(product)
                print("Product deleted!")
                break
        else:
            print("Product not found!")

    elif choice == 3:
        show_products(product_list)
        delete_index = int(input("Enter the index of the product to delete: "))
        if 0 <= delete_index < len(product_list):
            del product_list[delete_index]
            print("Product deleted!")
        else:
            print("Invalid index!")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")