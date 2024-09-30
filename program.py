import requests
import datetime
 
# Function to download the file
def downloadFile():
    # API URL
    apiUrl = "https://eeadmz1-downloads-api-dev-appservice.azurewebsites.net/"  
    endpoint = "ParquetFile/urls"

    # Path to download the file
    downloadPath = ".\\"

    # Get the current date and time
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File name
    fileName = "download_data-"+now +".zip" 
 
    # Request body  
    request_body = { 
         "countries": ["RO"], 
         "cities": ["string"], 
         "pollutants": ["PM10", "PM25"], 
         "dataset": 2, 
         "dateTimeStart": "2014-06-05T07:19:00Z", 
         "dateTimeEnd": "2015-06-06T12:07:19.000Z", 
         "aggregationType": "day" 
    } 
 
    # A get request to the API 
    print(requests.post(apiUrl+endpoint, json=request_body).status_code)
    downloadFile = requests.post(apiUrl+endpoint, json=request_body).content
 
    # Download the file
    output = open(downloadPath+fileName, 'wb')  
    output.write(downloadFile) 

# Main
if __name__ == "__main__":
    downloadFile()