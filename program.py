from downloadFile import downloadFile

if __name__ == "__main__":

    file = downloadFile()

    file.createFolder("data")
    file.createFolder("data\\linkList")
    file.createFolder("data\\parquet")
    file.createFolder("data\\csv")

    file.downloadFile("2013", "2014", ["PM10", "PM25"])