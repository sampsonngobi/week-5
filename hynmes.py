import csv

def main():

    #creat a heading list 
    heading_list= ["Title", "Author", "Composer"]

    #creat a hymns list 
    hymns_list =[
        ["O Holy Night", "John Dwight", "Adolphe Adam"],
        ["Oh, Come, All Ye Faithful", "John Wade", "John Wade"],
        ["Joy to the World", "Isaac Watts", "George Handel"],
        ["With Wondering Awe", "Anonymous", "Anonymous"]
    ]

    #call the write compound function 
    write_compound_list("hymmes.csv", hymns_list, heading_list)

def write_compound_list(filename,compound_list, heading_list = None):
        """Write the contents of a compound list into a CSV file.

        Parameters
            filename: the name of the CSV file to write
            compound_list: the list to write to the CSV file
            heading_list: a list that contains the column headings.
                If heading_list is None, this function will not
                write headings to the CSV File.
        Return: nothing
        
        """

        # Open the text file for writing and store a reference
        # to the opened file in a variable named csv_file.
        with open("hynmes.csv", "wt", newline="")as hymmes_file:
              

              # Use the csv module to create a writer object
              # that will write to the opened CSV file.
              writer = csv.writer (hymmes_file) 

              # Write the heading_list to the CSV file.
              if heading_list is not None:
                    writer.writerow(heading_list)

                # Write the contents of the list into
                # the CSV file, one row at a time.
              for rowlist in compound_list:
                    writer.writerow(rowlist)

# Call main to start this program.
if __name__ == "__main__":
    main()
              

