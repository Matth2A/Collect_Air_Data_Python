from downloadFile import downloadFile

from Packages.CreateFolder import createFolder

if __name__ == "__main__":

    file = downloadFile()

    createFolder("data")
    createFolder("data\\linkList")
    createFolder("data\\parquet")
    createFolder("data\\csv")

    file.downloadFile("2013", "2014", ["PM10", "PM25"])