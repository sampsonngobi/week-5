"""
A program that gets a quote 
from user and writes to a file 
"""

def main():

    #ask user for a quote
    quote = input("Please enter a quote: ")


    #open the quotes.text file for appending text
    with open("quotes.txt", "at") as quotes_file:

        #print the quote into the opened file 
        print(quote, file=quotes_file)
        print()
    
if __name__ == "__main__":
    main()