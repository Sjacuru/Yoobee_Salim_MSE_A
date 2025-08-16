"""
Develop a Python project using an object-oriented (OO) approach to convert large 
datasets into Parquet format. Then, compute the maximum, minimum, average, and 
absolute values for each column in the dataset. (see link to download a big numerical 
data in csv format from link: https://archive.ics.uci.edu/datasets)
Finally, share the GitHub repository link along with a screenshot of the results.
"""

#SystemCodeNumber,Capacity,Occupancy LastUpdated
import csv
def LargeDtb():

    inputFile = "dataset.csv"
    fileData = []

    with open(inputFile, mode = "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, fieldnames=None)
        lstCap = []
        lstOcp = []
        lstAbsOcp = []
        lstAbsCap = []
        countLines = 0
        sumCapacity = 0
        sumOccupancy = 0
        for row in reader:
            fileData.append(row) 
            sumCapacity += int(row['Capacity'])
            sumOccupancy += int(row['Occupancy']) 
            countLines += 1 #Check the quantity of occurrencies
            lstCap.append(int(row['Capacity'])) #Create a list with itens in columm Capacity
            lstOcp.append(int(row['Occupancy'])) #Create a list with itens in columm Occupancy
            lstAbsOcp.append(abs(int(row['Occupancy']))) #Create a list with absolute values in columm Occupancy
            lstAbsCap.append(abs(int(row['Capacity']))) #Create a list with absolute values in columm Capacity

    print ("First 10 numbers from occupancy absolute list", lstAbsCap[1:10])
    print ("First 10 numbers from capacity absolute list", lstAbsOcp[1:10])
    print ("number of lines - countLines", countLines)
    print ("number of lines - len", len(lstOcp))
    print ("Max Occupancy", max(lstOcp))
    print ("Max Capacity", max(lstCap))
    print ("Min Occupancy", min(lstOcp))
    print ("Min Capacity", min(lstCap))
    print ("Occupancy average for the period is: ", round(sumOccupancy/countLines,2))
    print ("Capacity average for the period is: ", round(sumCapacity/countLines,2))

if __name__ == "__main__":
    LargeDtb()
    