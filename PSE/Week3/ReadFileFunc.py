def ReadFile(data):

    lines = data.readlines()
    for line in lines:
        print(line[0:-1])
    data.close()
    return lines
    
def WriteFile(data):
    with open("demo_file.txt", "a") as data:
        data.write("\nAppended lin 1 \n")
        data.write("Appended lin 2 \n")
    data.close()

def PrintLines(data, lines):
    for line in lines:
        print(line[0:-1])
    data.close()

def ReadWrite():

    # Opens the file in "read" mode ("r").
    data = open("demo_file.txt", "r")
    #Read the file: "r"
    ReadFile(data)
    

    #Write a sentence at the end of the file
    data = open("demo_file.txt")
    WriteFile(data)
    
    #Print the file line by line. There is a bug. The content is being printed the number of data.write is being aplied
    lines = data.readlines()
    PrintLines(data, lines)

if __name__ == "__main__":
    ReadWrite()
