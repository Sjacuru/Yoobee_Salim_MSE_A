def creatingClass():
    class bankAcc:                                              #class definition
        
        def __init__(self,  accountNumber,                      # Constructor - called when 
                            balance,                            #   create instances
                            ownerName):                         
            
            self.accountNumber = accountNumber                  # Instance self . parameter 1
            self.balance = balance                              # Instance self . parameter 2
            self.ownerName = ownerName                          # Instance self . parameter 3

        def __str__(self):
            return      f"Account: {newAccount.accountNumber},\
                        Balance: {newAccount.balance},\
                        Name: {newAccount.ownerName}, \n"
        
        def client (self):                                      # Method that belong to the 
                                                                #   class
            print("(Def client)list",   self.accountNumber, 
                                        self.balance, 
                                        self.ownerName)
        def account (self):
            print("(Def account)Your account is ", self.accountNumber,"\n")
        
        def deposit(self):
            if amount > 0:
                self.balance += amount
                print("Deposited: ", amount, ", new balance", self.balance, "\n")
            else:
                print("Deposit invalid")

        def withdraw (self):
            if 0 < amount <= self.balance:
                self.balance -= amount
                print("Withdraw amount: ", amount, "remaining balance: ", self.balance)
            else:
                print("Invalid withdraw amount")

        
    newAccount = bankAcc(1234, 5678, "Salim")                   # Create an object
    print (newAccount.accountNumber,                            
           newAccount.balance, 
           newAccount.ownerName, "\n")                          # Use object attributes 
    print("Print class bankAcc", bankAcc, "\n")
    print("Print variable newAccount", newAccount, "\n")                                           
    print("-------")   
    newAccount.client()
    print("-------")                                            # Use method
    newAccount.account()                                        # Use method
    
    
    transaction = int(input("For deposit enter 1, for withdram enter 2: "))
    if transaction == 1:
        amount = int(input("Enter the deposit value: "))
        newAccount.deposit()
    
    elif transaction == 2:
        amount = int(input("Enter amount to withdraw: "))
        newAccount.withdraw()
    
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    ans = creatingClass()