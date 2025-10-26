#Function that prints all the exercise requirements
def PrintData(lstAbsCap, lstAbsOcp, countLines, lstOcp, lstCap, sumOccupancy, sumCapacity):
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
            countLines += 1  # Checks the number of occurrences
            lstCap.append(int(row['Capacity']))  # Creates a list with items from the Capacity column
            lstOcp.append(int(row['Occupancy']))  # Creates a list with items from the Occupancy column
            lstAbsOcp.append(abs(int(row['Occupancy'])))  # Creates a list with absolute values from the Occupancy column
            lstAbsCap.append(abs(int(row['Capacity'])))  # Creates a list with absolute values from the Capacity column
    
    PrintData(lstAbsCap, lstAbsOcp, countLines, lstOcp, lstCap, sumOccupancy, sumCapacity)
if __name__ == "__main__":
    LargeDtb()
    