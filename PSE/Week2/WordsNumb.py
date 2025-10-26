class WordsNumber:
    def __init__(self, text):
        self.text = text
        
    def length(self):
        return len(self.text)
    
    def counting(self):
        return len(self.text.split())

    def __str__(self):
        return self.text

def main():

    sentence = input("Please input a sentence: ")
    leters = WordsNumber(sentence)
    words = WordsNumber(sentence)

    leng_l = words.length()
    leng_w = words.counting()

    print(sentence)
    print("Counting letters: ", leng_l)
    print("Counting of words: ", leng_w)


if __name__ == "__main__":
    main()