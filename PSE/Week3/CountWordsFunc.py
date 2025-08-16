
def countOne(infile):
    count = 0
    for line in infile:
        words = line.split()
        for word in words:
            count += 1
    return print (count)

def countwo(infile):
    wordLen = 0
    for line in infile:
        words = line.split()
        wordLen += len(words)
    print(wordLen)    

def CountWords():

    infile = open("demo.txt", "r")
    countOne(infile)
    infile.close()


    # Alternative  
    infile = open("demo.txt", "r")
    countwo(infile)
    infile.close()

if __name__ == "__main__":
    CountWords()
