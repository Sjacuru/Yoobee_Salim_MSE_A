def createMatrix(rows, binar, result):
    for r in range(rows):
        new_row = []
        for c in range(binar):
            new_row.append(0)
        result.append(new_row)

    for l in range(rows):
        for c in range(binar):
            bit_position = (binar - 1) - c
            result[l][c] = ( l >> bit_position) & 1

    print ("\nINPUT\n")
    for r in range(len(result)):
        print(result[r])
    print ("\nOUTPUT\n") 
    return rows, binar, result

def twoqubits_x(rows, result):
    for lin in range(rows):
        if result[lin][0] == 1:
            result[lin][1] ^= 1
    return result

def threequbits_xy(rows, result):
    for lin in range(rows):
        if result[lin][0] == 1 and result[lin][1] == 1:
            result[lin][2] ^= 1
            print("X")
    return result

def CNOT_y(rows, result):
    for lin in range(rows):
        if result[lin][1] == 1:
            result[lin][2] ^= 1
    return result

def tofoliGate(rows, result):
    for lin in  range(rows):
        if  result[lin][0] == 1 and result[lin][1] == 1 or result[lin][0] == 1 and result[lin][1] == 1:
            result[lin][2] ^= 1
    return result

def fredkinGate(rows, result):
    for lin in  range(rows):
        if   result[lin][1] == 1 and result[lin][2] == 1:
                result[lin][1] = 1
                result[lin][2] = 1
        elif result[lin][0] == 1 and result[lin][1] == 1 or result[lin][0] == 1 and result[lin][2] == 1:
                result[lin][2] ^= 1
                result[lin][1] ^= 1
    return result

def menu():
    print("\n==== Quantum Circuits ====")
    print("1.  Circuit with 2 Qubits.\n"
          "|x, y> -> |x, y ⊕ x> The control Qubit 'x', when set to |1>, flips the target y\n\n")
    print("2.  Circuit with 3 Qubits.           [0, 0,  0]  \n" \
          "|x, y, z> -> |x, y, z ⊕ x^y>         [0, 0,  1]  \n" \
          "The control Qubit 'x^y',             [0, 1,  0]  \n" \
          "when set to |11>, flips the target z [0, 1,  1]  \n" \
          "                                     [1, 0,  0]  \n" \
          "                                     [1, 0,  1]  \n" \
          "                                     [1, 1, Flip]\n" \
          "                                     [1, 1, Flip]\n")
    print("3.  CNOT Gate.\n"
          "|x, y, z> -> |x, y, z ⊕ y> The control Qubit 'y', when set to |1>, flips the target z\n" \
                    "           x: ───────      [0, 0,  0]   \n"
                    "                           [0, 0,  1]   \n"
                    "           y: ───●───      [0, 1, Flip] \n"
                    "                 │         [0, 1, Flip] \n"
                    "           z: ───⊕──       [1, 0,  0]  \n" 
                    "                           [1, 0,  1]   \n" 
                    "                           [1, 1, Flip] \n" 
                    "                           [1, 1, Flip] \n")

    print("4.  Tofoli Gate\n"
                    "          C1:  ──●──       [0, 0,  0]   \n"
                    "                 │         [0, 0,  1]   \n"
                    "          C2:  ──●──       [0, 1,  0]   \n"
                    "                 │         [0, 1,  1]   \n"
                    "          T: ───⊕──        [1, 0,  0]  \n"
                    "                           [1, 0,  1]   \n"
                    "                           [1, 1, Flip] \n"
                    "                           [1, 1, Flip] \n")
    
    print("5.  Fredkin Gate\n" 
                    "           C: ───●────     [0,  0,   0]        \n"
                    "                 │         [0,  0,   1]        \n"
                    "           T1: ──⊕────     [0,  1,   0]       \n"
                    "                 │         [0,  1,   1]        \n"
                    "           T2: ──⊕────     [1,  0,   0]       \n" 
                    "                           [1, Flip, Flip]     \n" 
                    "                           [1, Flip, Flip]     \n" 
                    "                           [1,  1,   1]        \n")
    print("6.  Reserved")
    print("7.  Reserved")
    print("8.  Reserved")
    print("9.  Exit")

def main():

    while True:
        menu()
        choice = input("Select an option (1-5 or 9 to exit): ")
        if choice == '1':
            binar = 2
            rows = 2**binar
            result = []
            createMatrix(rows, binar, result)
            twoqubits_x(rows, result)
            for r in range(len(result)):
                print(result[r])
        
        elif choice == '2':    
            binar = 3
            rows = 2**binar
            result = []
            createMatrix(rows, binar, result)
            threequbits_xy(rows, result)
            for r in range(len(result)):
                print(result[r])

        elif choice == '3':    
            binar = 3
            rows = 2**binar
            result = []
            createMatrix(rows, binar, result)
            CNOT_y(rows, result)
            for r in range(len(result)):
                print(result[r])

        elif choice == '4':    
            binar = 3
            rows = 2**binar
            result = []
            createMatrix(rows, binar, result)
            tofoliGate(rows, result)
            for r in range(len(result)):
                print(result[r])

        elif choice == '5':    
            binar = 3
            rows = 2**binar
            result = []
            createMatrix(rows, binar, result)
            fredkinGate(rows, result)
            for r in range(len(result)):
                print(result[r])

        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

