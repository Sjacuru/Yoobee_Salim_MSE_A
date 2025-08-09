def Class_():
    class StringManipulator:
        #def __init__(self, text):
        #    self.text = text

        def var_input(text):  #New. I created
            return text

        #def find_character(self, char):
        #    return self.text.find(char)
        def find_character(char): #self parameter removed. 
            return char.find()

        def print_upper(self, char):
            return char.upper()
        
        def print_lower(self, text):
            return text.lower()
        
        def print_length(self, text):
            return len(text)


    #name = StringManipulator("example")
    name = StringManipulator.var_input("example")

    result = name.find_character("x")

    print("Find character index", name.find_character("x"))
    print("Print lower", name.print_lower("x"))
    print("Print upper", name.print_upper("x"))
    print("Print length", name.print_length("example"))
    print(result)


if __name__ == "__main__":
    ans = Class_()