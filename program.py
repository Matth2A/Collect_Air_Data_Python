import requests, os, webbrowser
 
# Function to download the file
def downloadFile():
    # API URL
    apiUrl = "https://eeadmz1-downloads-api-dev-appservice.azurewebsites.net/"  
    endpoint = "ParquetFile/urls"

    # Path to download the file
    downloadPath = ".\\"

    # Ensure the download path exists
    while True:
        yearStart = input("Enter the year start: ")
        yearEnd = input("Enter the year end: ")
        if(yearStart < yearEnd):
            break

    # File name
    fileName = "download_data-"+yearStart+"-"+yearEnd+".zip" 
 
    # Request body  
    request_body = { 
         "countries": ["RO"], 
         "cities": ["string"], 
         "pollutants": ["PM10", "PM25"], 
         "dataset": 2, 
         "dateTimeStart": yearStart+"-06-05T07:19:00Z", 
         "dateTimeEnd": yearEnd+"-06-06T12:07:19.000Z", 
         "aggregationType": "day" 
    } 
 
    # A get request to the API 
    print(requests.post(apiUrl+endpoint, json=request_body).status_code)
    downloadFile = requests.post(apiUrl+endpoint, json=request_body).content
 
    # Download the file
    output = open(downloadPath+fileName, 'wb')  
    output.write(downloadFile)

    # Print the contents of the downloaded file
    with open(downloadPath+fileName, 'rb') as file:
        next(file)  # Skip the first line

        # Open the first link in the file
        link = file.readline().decode('utf-8').strip()        
        document = requests.get(link)

        # Save the file
        with open(downloadPath+"data\\"+"download_data"+yearStart+"-"+yearEnd+".parquet", 'wb') as file:
            file.write(document.content)

        # For each line in the file
        # for line in file:
        #     link = line.decode('utf-8').strip()
        #     webbrowser.open(link)
        #     break


# Main
if __name__ == "__main__":
    downloadFile()