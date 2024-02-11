"""
PROJECT RECIEPT 
AUTHOR SAMPSON NGOBI 

I exceeded requirement by give a 10% discount every Teusday and Thursday
"""
#imports the csv lib
import csv

#imports the datetime lib
from datetime import datetime
 
#This function reads a csv file called products.csv and stores its content in a dictionary and returns same.
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    #used to catch errors 
    try:
        #open the products.csv file as product_file
        with open("products.csv", "rt") as products_file:

            #creats a csv reader for the products_file
            reader = csv.reader(products_file)

            #skips the header row
            next(reader)

            #loops through the file and adds it's content in a dictionary
            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]

                    dictionary[key] = row_list

                    
            
            return dictionary

    # these block handles any missing file, permission and exception errors
    except FileNotFoundError:
         print(f"Error: File '{filename}' not found.")
         return{}
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")
        return {}
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return {}



# This function calls the read_dictionary function 
# opens a request file and checks if the requested products are the product file and print the requested items
# calculates prints the number of requested items
#sums up and prints the prices of the requested products 
#computes the sales tax value and adds it to the subtotal 
# gives a 10% discount on Tuesdays and Thursdays 
# prints the total Due
# it also prints the date and time 
# prints the stores name and appreciation message

def main():

    try:

        PRODUCT_INDEX = 0
        PRODUCT_NAME = 1
        PRICE = 2
        

        ordered_items = []
        

        print()  
        product_dict = read_dictionary("products.csv", PRODUCT_INDEX)

        print(f"SAMPSON & SON STORES")
        print()

        price_list = []

        with open("request.csv", "rt") as request_file:

            reader = csv.reader(request_file)

            next(reader)

            product_no_index = 0
            quantity_index = 1

            for row_list in reader:


                product = row_list[product_no_index]
                quantity = row_list[quantity_index]
                ordered_items.append(product)


                for product_id in product_dict:
                    if product == product_id:
                        name = product_dict[product][PRODUCT_NAME]
                        price = float(product_dict[product][PRICE])
                        
                        
                        print(f"{name:<20} {quantity:<2} @ {price:<3}")

                        
                        price_list.append(price)
                            

            number_of_ordered_items = len(ordered_items)
            print()
            print(f"No of items: {number_of_ordered_items}")   

            subtotal_due = sum(price_list)
            print(f"Subtotal: {subtotal_due:.2f}")

            tax_amount = subtotal_due * 6 / 100
            print(f"Sales Tax: {tax_amount:.2f}")

            total_amount_due = tax_amount + subtotal_due
            print(f"Total: {total_amount_due:.2f}")

            print()
            print("Thank you for your petronage")

            current_date_and_time = datetime.now()
            formatted_date = current_date_and_time.strftime("%a %b  %d %H:%M:%S %Y")
            print(formatted_date)

            if current_date_and_time.weekday() == 1 or current_date_and_time.weekday() == 3:
                total_amount_due = (tax_amount + subtotal_due )* 10 / 100
                print(f"Total (less 10% discount: {total_amount_due:.2f})")
        
    except FileNotFoundError:
        print("Error: File 'request.csv' not found.")
    except PermissionError:
        print("Error: Permission denied for file 'request.csv'.")
    except KeyError as e:
        print(f"Error: {e} not found in the products dictionary.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")



                        
    print()
if __name__ == "__main__":
    main()
  
        
