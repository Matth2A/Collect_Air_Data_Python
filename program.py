from downloadFile import downloadFile
# Main
if __name__ == "__main__":

    #downloadFiles("2013", "2014")

    file = downloadFile()

    file.createFolder("data")
    file.createFolder("data\\linkList")
    file.createFolder("data\\parquet")
    file.createFolder("data\\csv")

    file.downloadFile("2014", "2015")