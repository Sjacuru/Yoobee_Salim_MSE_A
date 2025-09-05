j=3
y=1
for i in range(j):                  #Coluna 1
    print(0, end=' ')
    for x in range(y):              #Coluna 2
        print(x, end=' ')
        for x in range(y):          #Coluna 3
            print(x)

print('-----------------------------------------')

col = 2
row = 3
iteractions = col*row

matrix = [col*[0], row*[0]]

matrix[0][0] = 'a'
matrix[0][1] = 'b'
matrix[1][0] = 'c'
matrix[1][1] = 'd'
matrix[1][2] = 'e'
#matrix[1][1] = 'f'
print(matrix)

#for i in range(iteractions):
#    print(matrix)
print('-----------------------------------------')

# A matrix need to have columns and rows determinated before the program starts to execute
col = 3
row = 2

# Now we need to set these two numbers as the dimensions of the matrix. Let`s do it creating 
# the list matrix column and rows first

#rows = [0] * row
#cols = [0] * col

rows = []
cols = []

print("----Creating the matrix----")
# A matrix, for example, of three columns and two rows can be presented as a list like 
# matrix = [0,0,0], [0,0,0]. To do so, an inner loop will be created and stored in a new_row 
# list variable created inside the outer loop. After the inner loop iterate the number 
# of steps indicated on the variabl col, 3 in this example, new_row will store a list of three 
# elements and before enter in the next outer loop interation, matrix list variable will 
# be appended with new_row list. The variable new_row will be set to empty before enter the 
# outer loop again and this will be repeated the number of times set for the col variable.   


r = c = 0
matrix = []
for r in range(row):
    new_row = []
    for c in range(col):
        new_row.append(0)
    matrix.append(new_row)

for m in range(len(matrix)):
    print(matrix[m])

print("----Creating a matrix for binary counting----")

# I need a matrix that perform a binary counting to represent a Qubit interaction.
# In this case one Qubit is represented as a unitary number that flips from 0 to 1.
# 2 Qubits would be a matrix 2 x 2, or 2 to the power of 2. 3 Qubits would be 2 to 
# the power of 3 equals to amatrix 2 x 3 with 8 elements and so on.

Qubit = 4

QubitSize = 2**Qubit

matrix = []

for r in range(QubitSize):
    new_row = []
    for c in range(Qubit):
        new_row.append(0)
    matrix.append(new_row)
print(matrix)

for p in range(len(matrix)):
    print(f"{matrix[p]}  {p+1}")

print('---------Counting in binary 1st try--------------------')

# Now I need to create a pattern to count on binary

binar = 3
rows = 2**binar
sum = 0
result = []
for r in range(rows):
    new_row = []
    for b in range(binar):
        new_row.append(0)
    result.append(new_row)

print(result)

count=0

for l in range(rows):
    
    for c in range(binar):
        count += 1
        if l == 0:

            if l == c:
                result[l][c] = l
            else:
                result[l][c] = l
            print ("l", + l, "c", + c, "Result", + result[l][c])
        elif l%2 == 0:

            if c == 0:
                result[l][c] = 2
            else:
                result[l][c] = 2
            
            print ("l", + l, "c", + c, "Result", + result[l][c])
        elif l%2 != 0:

            if c == 0:
                if l == int(count/2):
                    result[int((count/rows))][c] = 0
                result[l][c] = 1
                
            else:
                result[l][c] = 3
            
            print ("l", + l, "c", + c, "Result", + result[l][c])
        
            
print(count)
for r in range(len(result)):
    print(result[r])


# Now with a more intense AI help

binar = 4
rows = 2**binar
sum = 0
result = []
for r in range(rows):
    new_row = []
    for b in range(binar):
        new_row.append(0)
    result.append(new_row)

print(result)

for l in range(rows):
    for c in range(binar):
        bit_position = (binar - 1) - c
        result[l][c] = ( l >> bit_position) & 1
        print ("l:", + l, "c:", + c, "bit_position: ", + bit_position, "Value", + result[l][c])         

for l in range(len(result)):
        print(result[l])

#--------now the circuit----------


binar = 2
rows = 2**binar
sum = 0
result = []
for r in range(rows):
    new_row = []
    for b in range(binar):
        new_row.append(0)
    result.append(new_row)

print(result)

for l in range(rows):
    for c in range(binar):
        bit_position = (binar - 1) - c
        result[l][c] = ( l >> bit_position) & 1
        print ("l:", + l, "c:", + c, "bit_position: ", + bit_position, "Value", + result[l][c])         

for l in range(len(result)):
        print(result[l])


for l in range(rows):
    for c in range(binar):
        bit_position = (binar - 1) - c
        if result[l][0] == 1:
            result[l][1] = 3
        print ("l:", + l, "c:", + c, "bit_position: ", + bit_position, "Value", + result[l][c])         

for r in range(len(result)):
        print(result[r])