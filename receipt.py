# Import the datatime module so that
# it can be used in this program.
from datetime import datetime
import csv

# Define index constant for clarity.
PRODUCT_NUM_INDEX = 0

def main():
    # Print store name
    STORE_NAME = "Inkom Emporium"
    print(STORE_NAME)
    print()

    # Call the read_products function and stores the products dictionary in a variable named products.
    products = read_products()

    # Call the process_request function.
    quantity, subtotal = process_request(products)

    # Calculate and print out the item quantity and total prices.
    TAX_RATE = 0.06
    sales_tax = subtotal * TAX_RATE
    total = subtotal + sales_tax
    print(f"Number of Items: {quantity:.0f}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    print()
    
    # Print out concluding thank you message and current time.
    print(f"Thank you for shopping at {STORE_NAME}!")

    # Call the now() method to get the current date and
    # time as a datetime object from the computer's clock.
    current_date_and_time = datetime.now()

    # Format and print the current date and time to include
    # only the day of the week, the hour, and the minute.
    print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

def read_products():
    products = {}

    # try excepy block in case the file is not found or permission is denied.
    try:
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
    except FileNotFoundError as e:
        print(type(e).__name__, e, sep=": ")
        print(f"The file products.csv doesn't exist.")
        print("Ensure products.csv exists in the current directoy and run the program again.")
        exit()
    except PermissionError as e:
        print(type(e).__name__, e, sep=": ")
        print(f"You don't have permission to read products.csv.")
        print("Ensure products.csv grants reading permissions and run the program again.")
        exit()
    except Exception as e:
        print(type(e).__name__, e, sep=": ")
        exit()

    # Return the dictionary.
    return products

def process_request(products):
    try:
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

            # Process the file one row at a time. Keep tabs on the number 
            # of items and the subtotal.
            num_items = 0
            subtotal = 0
            for row in reader:

                # Retrieve request information.
                product_num = row[PRODUCT_NUM_INDEX]
                product_quantity = int(row[QUANTITY_INDEX])
                num_items += product_quantity

                # Use the requested product number to find the corresponding item in products dictionary.
                product = products[product_num]

                # Retrieve product information.
                product_name = product[NAME_INDEX]
                product_price = float(product[PRICE_INDEX])
                subtotal += product_price * product_quantity

                # Print the product name, requested quantity, and product price.
                print(f"{product_name}: {product_quantity} @ {product_price}")
            print()
    except FileNotFoundError as e:
        print(type(e).__name__, e, sep=": ")
        print(f"The file request.csv doesn't exist.")
        print("Ensure request.csv exists in the current directoy and run the program again.")
        exit()
    except PermissionError as e:
        print(type(e).__name__, e, sep=": ")
        print(f"You don't have permission to read request.csv.")
        print("Ensure request.csv grants reading permissions and run the program again.")
        exit()
    except KeyError as e:
        print(type(e).__name__, e, sep=": ")
        print(f"A key requested in request.csv does not exist as an item in products.csv.")
        print("Edit products.csv and request.csv files to ensure keys match exactly then run the program again.")
        exit()
    except Exception as e:
        print(type(e).__name__, e, sep=": ")
        
    return num_items, subtotal

# Call main to start this program.
if __name__ == "__main__":
    main()