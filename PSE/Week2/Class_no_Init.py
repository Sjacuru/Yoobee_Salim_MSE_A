class StringManipulator:
    #def __init__(self, text):
    #    self.text = text

    def var_input(text):  #New. I created
        return text

    def find_character(text, char):
        return text.find(char)
    
    def print_upper(text):
        return text.upper()
    
    def print_lower(text):
        return text.lower()

    def print_length(text):
        return len(text)


def Main():

    name = StringManipulator.var_input("example") #Create instante and assign "example" to name variable (object) 

    position = StringManipulator.find_character(name, "x") #Call find method 

    upp = StringManipulator.print_upper(name) #Call upper method 
    
    low = StringManipulator.print_lower(name) #Call lower method

    leng = StringManipulator.print_length(name) #call length method

    #Testing ----------
    print(name)
    print(position)
    print(upp)
    print(low)
    print(leng)
    #Testing ----------

if __name__ == "__main__":
    ans = Main()