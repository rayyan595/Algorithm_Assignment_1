import os  # Import the os module for working with file paths

class Product:
    def __init__(self, ID, Name, Price, Category):
        self.ID = ID
        self.Name = Name
        self.Price = Price
        self.Category = Category

def load_product_data(file_path): # loads the file from a txt file 
    products = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(', ')
            product = Product(int(data[0]), data[1], float(data[2]), data[3])
            products.append(product)
    return products

def Insert_product(products, product): #Inserts a new product into the list
    products.append(product)

def Update_product(products, ID, new_name, new_price, new_category): #Updates a product in the list
    for product in products:
        if product.ID == ID:
            product.Name = new_name
            product.Price = new_price
            product.Category = new_category

def Delete_product(products, ID): #Deletes a product from the list
    products[:] = [product for product in products if product.ID != ID]

def Search_product_by_id(products, ID): #Finds a certain product on the list by its ID
    for product in products:
        if product.ID == ID:
            return product
    return None

def search_product_by_name(products, name): #Finds a certain product on the list by its name
    matching_products = []
    for product in products:
        if name.lower() in product.Name.lower():
            matching_products.append(product)
    return matching_products

def quick_sort(arr): #Sorts the products in order by price using the quicksort algorithm
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2].Price
    left = [x for x in arr if x.Price < pivot]
    middle = [x for x in arr if x.Price == pivot]
    right = [x for x in arr if x.Price > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Main code
os.chdir('/Users/notrayyan/Downloads/')
product_data_file = "product_data.txt"
products = load_product_data(product_data_file)

while True: #Displays this in the output menu
    print("\nChoose one of the following:")
    print("1. Add a new product")
    print("2. Update a product")
    print("3. Delete a product")
    print("4. Search for a product by ID Number")
    print("5. Search for a product by its name")
    print("6. Sort products by price")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        ID = int(input("Enter the product ID: "))
        Name = input("Enter the product name: ")
        Price = float(input("Enter the product price: "))
        Category = input("Enter the product category: ")
        new_product = Product(ID, Name, Price, Category)
        Insert_product(products, new_product)
        print("Product was inserted successfully.")

    elif choice == "2":
        ID = int(input("Enter the product ID to update: "))
        new_name = input("Enter the new product name: ")
        new_price = float(input("Enter the new product price: "))
        new_category = input("Enter the new product category: ")
        Update_product(products, ID, new_name, new_price, new_category)
        print("Product was updated successfully.")

    elif choice == "3":
        ID = int(input("Enter the product ID of the product you'd like to delete': "))
        Delete_product(products, ID)
        print("Product was deleted successfully.")

    elif choice == "4":        
        ID = int(input("Enter the product ID for the product you'd like to search: "))
        found_product = Search_product_by_id(products, ID)
        if found_product:
            print("Product was found:", found_product.Name)
        else:
            print("Product was not found.")

    elif choice == "5":
        name = input("Enter the product name to search: ")
        matching_products = search_product_by_name(products, name)
        if matching_products:
            print("Matching products:")
            for product in matching_products:
                print(product.Name)
        else:
            print("No matching products found.")

    elif choice == "6":
        sorted_products = quick_sort(products)
        print("Sorted products by price:")
        for product in sorted_products:
            print(product.ID, product.Name, product.Price, product.Category)

    elif choice == "7":
        print("""Ending the program. Thank you for using""")
        break

    else:
        print("That was not a valid choice, Please enter a number between 1 and 7.")
        
        
        
        