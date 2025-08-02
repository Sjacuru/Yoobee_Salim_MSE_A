def factorial():
    number = input("Inut a number: ")
    fn = int(number)
    i = 1
    for i in range(fn):
        if i == 0:
            fn = 1
        else:
            fn = fn * (i + 1) 
    print(fn)

if __name__ == "__main__":
    ans = factorial()