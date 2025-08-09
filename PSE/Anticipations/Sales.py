import csv
def rwfile():

    inputFile = "Sales.csv"
    fileData = []
    outputFile = "Result.csv"

    with open(inputFile, mode = "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, fieldnames=None)
        total = 0
        for row in reader:
            fileData.append(row) 
            product = row[' Product']
            revenue = int(row[' Revenue'])
            total += revenue 
            print(product, revenue, total)

    print("Data loaded in fileData as dict")
    print(fileData[1:2])
    print(",".join(fileData[1]))
    print("Total revenue: ", total)

    with open(outputFile, mode = 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', ' Product', ' Revenue'])
        writer.writerow([' Product', ' revenue'])

if __name__ == "__main__":
    ans = rwfile()
    