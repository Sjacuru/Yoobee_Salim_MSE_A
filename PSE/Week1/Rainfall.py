import numpy as np
def rainanalysis():
    rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
    rainarray = np.array(rainfall)

    print(rainarray)

    print("The total amount of rain for the period was ",round(np.sum(rainarray),2))

    print("The average amount of rain for the period was ", round(np.mean(rainfall),2))
    
    days = 0
    for day in rainfall:
        if day == 0.0:
            days += 1
    print("There was no rain on", days, "days")

    print("There was no rain on", np.sum(rainarray == 0.0), "days") #AI alternative

if __name__ == "__main__":
    ans = rainanalysis()
