def main():

    country_list = ['United States', 'Canada', 'Germany', 'Japan', 'Brazil', 'Australia', 'India', 'South Africa', 'Italy', 'Mexico']

    write_list("countries.txt", country_list)

def write_list(filename, text_list):

    with open("countries.txt", "wt") as countries_file:

        for country in text_list:
            print(country, file=countries_file )

if __name__ == "__main__":
    main()