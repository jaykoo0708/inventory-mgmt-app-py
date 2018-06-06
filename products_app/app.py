import os
import csv
productArray = []
def displayMenu(name,count):
    print(
        """
-----------------------------------
INVENTORY MANAGEMENT APPLICATION
-----------------------------------
Welcome {username}!
There are {length} products in the database.
    operation | description
    --------- | ------------------
    'List'    | Display a list of product identifiers and names.
    'Show'    | Show information about a product.
    'Create'  | Add a new product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.
Please select an operation:
        """.format(username = name,length = count)
    )

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    #TODO: open the file and write a list of dictionaries. each dict should represent a product.

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)

def readFromFile(filename="products.csv"):
    filepath =  os.path.join(os.path.dirname(__file__), "db", filename) ##appending the path __file__ is the current file and it is os command
    #filepath = "products_default.csv"
    with open(filepath,"r") as csv_file:
        reader = csv.DictReader(csv_file) # it is reading the files as a dictionary object
        for obj in reader:
            productArray.append(dict(obj))

productsArray = []
headers = ["id", "name", "aisle", "department", "price"]
def product_not_found():
    print("OOPS. Couldn't find a product with that identifier. Try listing products to see which ones exist.")

def product_price_not_valid():
     print("OOPS. That product price is not valid. Expecting a price like 4.99 or 0.77. Please try again.")

def update(product):
    print("update the product")
    print(product)

def delete(product):
    del productArray[productArray.index(product)]

def create(product):
    print("product created")
    productArray.append(product)

def showProduct(product):
    print("showing product")
    print(product)

def showAllProducts():
    print("showing all the products in the database")
    for item in productArray:
        print(item["id"], item["name"])

def switch_demo(argument):
    mapper = {"List":1,"Show":2,"Create":3,"Update":4,"Destroy":5}

    return mapper.get(argument, "Invalid month")


def validFuelPrice(price):
    try:
        float(price)
        return True
    except Exception as e:
        return False

def filterProduct(productId):
    for item in productArray:
        if int(item["id"]) == int(productId):
            return item
    return None

def inputProductFromUser():
    try:
        productId = input("Enter the product id")
        product = filterProduct(productId)
        return product
    except ValueError as e: return None
    except IndexError as e: return None


def editableValues():
    array = []
    for item in headers:
        if item == "id":
            continue;
        else:
            array.append(item)
    return array

def idAssigned():
#     maximu  = -1
#     if len(productArray) == 0:
#         return 1
#     else:
#         for item in productArray:
#             if maximu > int(item["id"]):
#                 maximu = int(item["id"]
#         return maximu
    if len(productArray) == 0:
        return 1
    else:
        product_ids = [int(p["id"]) for p in productArray]
        return max(product_ids) + 1

def setUp():
    readFromFile("products.csv")
    operation = input(displayMenu("abc",len(productArray)))
    operation = operation.title()
    option  = switch_demo(operation)

    if option == 1:
        showAllProducts()

    elif option == 2:
        product = inputProductFromUser()
        if product == None: product_not_found()
        showProduct(product)
    elif option == 3:
        newProduct = {}
        newProduct["id"] = idAssigned()
        editableValuesArray = editableValues();
        for item in editableValuesArray:
            val = input(f"OK. Please input the product's '{item}': ")
            if item == "price" and validFuelPrice(val) == False:
                product_price_not_valid()
                return
            newProduct[item] = val
        create(newProduct)


    elif option == 4:
        product = inputProductFromUser()
        if product == None: product_not_found()
        editableValuesArray = editableValues();
        for item in editableValuesArray:
            val =  input("enter the value of the new value for item {} ".format(item))
            if item == "price" and validFuelPrice(val) == False:
                return
            product[item] = val
        update(product)
    elif option == 5:
        product = inputProductFromUser()
        if product == None: product_not_found()
        delete(product)




def statartup():
    setUp()

if __name__ == "__main__":
    statartup()
