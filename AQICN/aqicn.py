import requests

from Packages.CreateFolder import createFolder

if __name__ == "__main__":

    # Create the folder to store the data
    createFolder("data")

    ## TEST ##
    # Counter to stop the loop
    # i=0

    # List of links to download data
    docLink = \
        [
            "2015H1", "2016H1", "2017H1", "2018H1",
            "2019Q1", "2019Q2", "2019Q3", "2019Q4",
            "2020Q1", "2020Q2", "2020Q3", "2020Q4",
            "2021Q1", "2021Q2", "2021Q3", "2021Q4",
            "2022Q1", "2022Q2", "2022Q3", "2022Q4"
        ]

    # Loop through the list of links
    for link in docLink:
        # i+=1

        # Get the data from the link
        data = requests.get("https://aqicn.org/data-platform/covid19/report/43768-aa2d98d4/"+link).content
        output = open("data/"+link, 'wb')

        # Save the data
        with open(".//data//"+link, "wb") as file:
            file.write(data)

        # only one for testing
        # if i==2:
        #     print("Done")
        #     break