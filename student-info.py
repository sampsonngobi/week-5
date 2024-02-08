#import the csv lib
import csv

def main():
    heading_list = ["I-number","Name"]
    
    # Create a dictionary that contains student
    # I-Numbers and names.
    students_dict = {
        # I-Number : Name
        "751766201" : "James Smith",
        "751762102" : "Esther Einboden",
        "052058203" : "Cassidy Benavidez",
        "323021604" : "Joel Hatch",
        "251041405" : "Brianna Ririe",
        "001152306" : "Stefano Hisler",
        "182706207" : "Hyeonbeom Park",
        "124712708" : "Maren Thomas",
        "212505409" : "Tyler Clark"
    }

    write_dict("student-info.csv", students_dict, heading_list, 0)

def write_dict(filename, dictionary, heading_list=None, key_column_index=None):

    """Write the contents of a dictionary into a CSV file.

    Parameters
        filename: the name of the CSV file to write
        dictionary: the dictionary to write to the CSV file
        heading_list: a list that contains the column headings.
            If heading_list is None, this function will not
            write headings to the CSV File.
        key_column_index: the index of the column in the CSV
            file where this function should write the keys.
            If key_column_index is None, this function will
            not write the keys to the CSV file.
    Return: nothing
    """

    # Open the text file for writing and store a reference
    # to the opened file in a variable named csv_file.
    with open("student-info.csv", "wt")as student_file:

         # Use the csv module to create a writer object
        # that will write to the opened CSV file.
        writer = csv.writer(student_file)

        # Write the heading_list to the CSV file.
        if heading_list is not None:
            writer.writerow(heading_list)

        # Get each key value pair from the dictionary
        # and write each pair on a separate row in thee
        # CSV file.
        for key, value in dictionary.items():
            # If a value stored in the dictionary is a
            # list, make a temporary copy of that value.
            # Otherwise, create a list that contains the
            # value.
            if isinstance(value, list):
                row_list = value.copy()
            else:
                row_list = [value]

            # If key_column_index is an integer, insert
            # the key into the row_list so that this
            # function will write the key to the CSV file.
            if key_column_index is not None:
                row_list.insert(key_column_index, key)

            # Write a row to the CSV file.
            writer.writerow(row_list)


if __file__ == "__main__":
    main()