def CountWords():

    infile = open("demo.txt", "r")

    count = 0
    for line in infile:
        words = line.split()
        for word in words:
            count += 1
    print (count)

    # Alternative 
    wordLen = 0
    infile = open("demo.txt", "r")
    for line in infile:
        words = line.split()
        wordLen += len(words)
    print(wordLen)

    infile.close()

if __name__ == "__main__":
    CountWords()
