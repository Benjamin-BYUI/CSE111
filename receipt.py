import csv

# Define index constant for clarity.
PRODUCT_NUM_INDEX = 0

def main():
    # Call the read_products function and stores the products dictionary in a variable named products.
    products = read_products()

    # Print the products dictionary.
    print("Products")
    for product_num, name_and_price in products.items():
        pass
        print(f"{product_num} {name_and_price}")
    print()

    # Call the process_request function.
    process_request(products)

def read_products():
    products = {}

    # Open the products.csv file for reading.
    with open("products.csv", "rt") as products_file:

        # Use a csv.reader to read from the opened file.
        reader = csv.reader(products_file)

        # Skip the first line giving a format.
        next(reader)

        # Define index constants for clarity.
        NAME_INDEX = 1
        PRICE_INDEX = 2

        # Process the file one row at a time.
        for row in reader:

            # Retrieve product information.
            product_num = row[PRODUCT_NUM_INDEX]
            product_name = row[NAME_INDEX]
            product_price = row[PRICE_INDEX]

            # Populate a dictionary with the contents of the products.csv file.
            products[product_num] = [product_name, product_price]

    # Return the dictionary.
    return products

def process_request(products):

    # Open the request.csv file for reading. 
    with open("request.csv", "rt") as requests_file:

        # Use a csv.reader to read from the opened file.
        reader = csv.reader(requests_file)

        # Skip the first line giving a format.
        next(reader)

        # Define index constant for clarity.
        QUANTITY_INDEX = 1
        NAME_INDEX = 0
        PRICE_INDEX = 1

        # Print a title for the requested items. Process the file one row at a time.
        print("Requested Items")
        for row in reader:

            # Retrieve request information.
            product_num = row[PRODUCT_NUM_INDEX]
            product_quantity = row[QUANTITY_INDEX]

            # Use the requested product number to find the corresponding item in products dictionary.
            product = products[product_num]

            # Retrieve product information.
            product_name = product[NAME_INDEX]
            product_price = product[PRICE_INDEX]

            # Print the product name, requested quantity, and product price.
            print(f"{product_name}: {product_quantity} @ {product_price}")
        print()

# Call main to start this program.
if __name__ == "__main__":
    main()