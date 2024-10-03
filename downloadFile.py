import requests, os, pandas as pd

from apiData import apiData

class downloadFile:

    # Constructor
    def __init__(self):
        self.apiUrl = "https://eeadmz1-downloads-api-appservice.azurewebsites.net/"
        self.endpoint = "ParquetFile/urls"
        self.downloadPath = ".\\"
        self.listName = ""
        self.request_body = {}
        self.apiconnection = apiData(self.apiUrl, self.endpoint, self.request_body)


    # Set the request body
    def setRequestBody(self, countries, cities, pollutants, dataset, dateTimeStart, dateTimeEnd, aggregationType):
        self.request_body = {
            "countries": countries,
            "cities": cities,
            "pollutants": pollutants,
            "dataset": dataset,
            "dateTimeStart": dateTimeStart+"-06-05T07:19:00Z",
            "dateTimeEnd": dateTimeEnd+"-06-05T07:19:00Z",
            "aggregationType": aggregationType
        }
        self.listName = "download_data-"+dateTimeStart+"-"+dateTimeEnd+".zip"


    # Function to download the file
    def downloadFile(self, startYear, endYear):
        # Set the request body
        self.setRequestBody(["RO"], ["string"], ["PM10", "PM25"], 2, startYear, endYear, "day")
        self.apiconnection.setRequestBody(self.request_body)

        # Get the file
        downloadFile = self.apiconnection.getApiDataPost()

        # Download the file
        output = open(self.downloadPath+"data\\linkList\\"+self.listName, 'wb')
        output.write(downloadFile.content)

        # Print the contents of the downloaded file
        with open(self.downloadPath+"data\\linkList\\"+self.listName, 'rb') as file:
            # Skip the first line wich is the title
            next(file)

            # Open the first link in the file
            link = file.readline().decode('utf-8').strip()
            document = requests.get(link)

            # Save the file
            with open(self.downloadPath + "data\\parquet\\" + "parquet_data" + startYear + "-" + endYear + ".parquet", 'wb') as doc:
                doc.write(document.content)

        # Convert the parquet file to a csv file
        self.parquetToCsv(startYear, endYear)


    # Function to create a folder
    def createFolder(self, folderPath):
        # Check if the folder exists, if not create it
        if not os.path.exists(self.downloadPath + folderPath):
            os.makedirs(self.downloadPath + folderPath)


    # Function to convert the parquet file to a csv file
    def parquetToCsv(self, startYear, endYear):
        df = pd.read_parquet(self.downloadPath + "data\\parquet\\" + "parquet_data" + startYear + "-" + endYear + ".parquet")
        # Convert the parquet file to a csv file
        df.to_csv(self.downloadPath + "data\\csv\\" + "csv" + startYear + "-" + endYear + ".csv", index=False)