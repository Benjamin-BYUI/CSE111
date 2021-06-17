import csv

I_NUMBER_INDEX = 0
NAME_INDEX = 1

def main():
    # Indexes of some of the columns
    # in the dentists.csv file.

    # Read the contents of a CSV file named dentists.csv
    # into a dictionary named dentists. Use the phone
    # numbers as the keys in the dictionary.
    students = read_dict("students.csv", I_NUMBER_INDEX)

    # Gets an I-Number from the user
    i_number = input("Insert I-number: ")

    # Remove dashes (-'s) from the i_number
    i_number = i_number.replace("-", "")

    # Check if the i_number is a valid int, otherwise throw error.
    try:
        i_number_temp = int(i_number)
    except:
        print("Invalid I-Number")
        return

    i_number = str(i_number)
    # Check if length of i_number input is valid
    if len(i_number) > 9:
        print("Invalid I-Number: too many digits")
        return
    elif len(i_number) < 9:
        print("Invalid I-Number: too few digits")
        return

    # Uses the I-Number to find the corresponding student name in the dictionary
    if i_number in students:
        student = students[i_number]

        # prints the student name.
        print(student)
    else:
        print("No such student")
    


def read_dict(filename, key_column_index):
    """Read the contens of a CSV file into a dictionary
    and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open a CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column
        # headings and not information, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in reader:

            # From the current row, retrieve
            # the column that contains the key.
            key = row[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row[NAME_INDEX]

    # Return the dictionary.
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()