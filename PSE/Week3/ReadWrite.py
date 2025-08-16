
def ReadWrite():

    data = open("demo_file.txt", "r")
    lines = data.readlines()
    for line in lines:
        print(line[0:-1])
    data.close()

    with open("demo_file.txt", "a") as data:
        data.write("\nAppended lin 1 \n")
        data.write("Appended lin 2 \n")
    data.close()

    data = open("demo_file.txt")
    for line in lines:
        print(line[0:-1])
    data.close()



if __name__ == "__main__":
    ReadWrite()
