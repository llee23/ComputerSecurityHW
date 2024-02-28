cipher = "1100101011101101101000100110010101011111101101110011100001110011"
key = "0100110001001111010101100100010101000011010100110100111001000100"

pc1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]

pc2 = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]

num_shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

pBox = [
        16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2, 8, 24, 14,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25,
    ]

         
IPTable = [58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7]

eBitTable = [32, 1, 2, 3, 4, 5,
               4, 5, 6, 7, 8, 9,
               8, 9, 10, 11, 12, 13,
               12, 13, 14, 15, 16, 17,
               16, 17, 18, 19, 20, 21,
               20, 21, 22, 23, 24, 25,
               24, 25, 26, 27, 28, 29,
               28, 29, 30, 31, 32, 1]
               
# s boxes
S = [
        #S1
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],

        #S2
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],

        #S3
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],

        #S4
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
        ],

        #S5
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        ],

        #S6
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
        ],

        #S7
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
        ],

        #S8
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
        ]
    ]
    
inverseIP = [
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
]

def generateRoundKeys(key):
    # permute using pc-1
    key_plus = ""
    for i in range(len(pc1)):
        key_plus += key[pc1[i]-1]

    #split the key in half
    C = key_plus[:int(len(key_plus)/2)]
    D = key_plus[int(len(key_plus)/2):]

    #generate 16 round keys
    roundKeys = []
    for i in range(16):
        #perform left shifts
        C = leftShift(C, num_shifts[i])
        D = leftShift(D, num_shifts[i])
        
        join = C + D
        tempKey = ""
        # permute according to pc2 table
        for i in range(len(pc2)):
            tempKey += join[pc2[i]-1]
        roundKeys.append(tempKey)
        
    return roundKeys
        
def leftShift(string, n):
    shift = string
    for i in range(n):
        temp = shift
        shift = temp[1:] + temp[0]
    return shift

def fFunction(R, K):
    #run r through E bit table
    ER = ""
    for i in range(len(eBitTable)):
        ER += R[eBitTable[i]-1]

    #XOR ER and K
    KER = int(K, 2)^int(ER,2)
    KER = bin(KER)[2:].zfill(len(ER)) # expand to 48 bits

    # run through s boxes to get 32 bit output
    postSBox = ""
    start=0
    for i in range(8):
        end = start + 6
        temp = KER[start:end]
        row = int(temp[0] + temp[-1], 2)
        col = int(temp[1:-1],2)
        #get 4 bit output from s table
        postSBox += bin(S[i][row][col])[2:].zfill(4)
        start=end

    # run post S box through P box
    result = ""
    for i in range(len(pBox)):
        result += postSBox[pBox[i]-1]
    
    return result
        


### Driver 

## generate and print round keys
K = generateRoundKeys(key)
print("Round Keys:")
for i in range(len(K)):
    print("K" + str(i+1) + ": " + K[i])
    


## decrypt ciphertext
# run ciphertext through the IP table
IP = ""
for i in range(len(IPTable)):
    IP += cipher[IPTable[i]-1]

# split into L0 and R0
L = [IP[:int(len(IP)/2)]]
R = [IP[int(len(IP)/2):]]

#calculate R and L arrays
print("\n\nEncryption round results:")

for i in range(1,17):
    print("\nRound " + str(i) + ": ")
    
    fResult = fFunction(R[i-1], K[16-i])
    
    print("F: " + fResult)
    L.append(R[i-1]) # L[i+1] = R[i]
    temp = int(L[i-1], 2)^int(fResult,2)
    R.append(bin(temp)[2:].zfill(32))
    print("L" + str(i) + ": "+ L[i])
    print("R" + str(i) + ": "+ R[i])
    print()

    

preIP =  R[16] + L[16]

#run through inverse IP table
output = ""
for i in range(len(inverseIP)):
    output += preIP[inverseIP[i]-1]
decoded = ""
start = 0
for i in range(8):
    end = start + 8
    bits = output[start:end]
    decoded += chr(int(bits, 2))
    start=end

print("Decoded message:")
print(decoded)