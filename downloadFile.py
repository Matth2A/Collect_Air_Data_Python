import requests, os, pandas as pd

from apiData import apiData

class downloadFile:

    # Constructor
    def __init__(self):
        # API Data
        self.apiUrl = "https://eeadmz1-downloads-api-appservice.azurewebsites.net/"
        self.endpoint = "ParquetFile/urls"
        self.request_body = {}
        self.apiconnection = apiData(self.apiUrl, self.endpoint, self.request_body)

        # Files data
        self.downloadPath = ".\\"
        self.listName = ""


    # Set the request body
    def setRequestBody(self, countries, cities, pollutants, dataset, dateTimeStart, dateTimeEnd, aggregationType):
        self.request_body = {
            "countries": countries,
            "cities": cities,
            "pollutants": pollutants,
            "dataset": dataset,
            "dateTimeStart": dateTimeStart + "-06-05T07:19:00Z",
            "dateTimeEnd": dateTimeEnd +"-06-05T07:19:00Z",
            "aggregationType": aggregationType
        }
        self.listName = "download_data-" + dateTimeStart + "-" + dateTimeEnd + "-" + pollutants[0] + ".zip"


    # Function to create a folder
    def createFolder(self, folderPath):
        # Check if the folder exists, if not create it
        if not os.path.exists(self.downloadPath + folderPath):
            os.makedirs(self.downloadPath + folderPath)


    # Function to convert the parquet file to a csv file
    def parquetToCsv(self, startYear, endYear, po):
        df = pd.read_parquet(self.downloadPath + "data\\parquet\\" + "parquet_data" + startYear + "-" + endYear + "-" + po + ".parquet")
        # Convert the parquet file to a csv file
        df.to_csv(self.downloadPath + "data\\csv\\" + "csv" + startYear + "-" + endYear + "-" + po + ".csv", index=False)


    # Function to download the file
    def downloadFile(self, startYear, endYear, pollutant):
        for i in pollutant:

            # Set the request body
            self.setRequestBody(["RO"], ["string"], [i], 2, startYear, endYear, "hour")
            self.apiconnection.setRequestBody(self.request_body)
            print("Set request body: " + i)

            # Get the file
            downloadFile = self.apiconnection.getApiDataPost()

            # Download the file
            output = open(self.downloadPath + "data\\linkList\\" + self.listName, 'wb')
            output.write(downloadFile.content)
            print("Downloaded link list: " + i)

            # Print the contents of the downloaded file
            with open(self.downloadPath + "data\\linkList\\" + self.listName, 'rb') as file:
                # Skip the first line wich is the title
                next(file)

                # Open the first link in the file
                link = file.readline().decode('utf-8').strip()
                print("Link: " + link)
                document = requests.get(link)

                # Save the file
                with open(self.downloadPath + "data\\parquet\\" + "parquet_data" + startYear + "-" + endYear + "-" + i + ".parquet", 'wb') as doc:
                    doc.write(document.content)
                    print("Downloaded parquet file: " + i)

            # Convert the parquet file to a csv file
            self.parquetToCsv(startYear, endYear, i)
            print("Downloaded csv file: " + i)