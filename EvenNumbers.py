def evenNumber():
    number = input("Enter a number: ")
    even = int (number)
    total = 0
    for i in range (2, even + 1, 2):
        total += i
    print ("Result ", total)
if __name__ == "__main__":
    ans = evenNumber()

