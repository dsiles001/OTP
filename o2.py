import random

message = input()

alpha = ['dummy','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def randomKey(message):
    binaryKey = []
    for _ in range(len(message)):
        ind = random.randrange(1,26,1)
        char = alpha[ind]
        binaryKey.append(format(ord(char), '08b'))
    return binaryKey

def encrypt(message, binaries):
    messagebinaries = []
    binaryNums = []
    for i in range(len(message)):
        temp = ''
        binaryChar = format(ord(message[i]),'08b')
        messagebinaries.append(binaryChar)
        for j in range(len(binaryChar)):
            if binaryChar[j] == '1' and binaries[i][j] == '1':
                temp+='0'
            elif binaryChar[j] == '1' or binaries[i][j] == '1':
                temp+='1'
            else:
                temp+='0'
        binaryNums.append(temp)
    
    return binaryNums, messagebinaries

def decrypt(enrypted, binaries):
    for i in range(len(encrypted)):
        temp = ''
        decryptBinary =[]
        # messagebinaries.append(binaryChar)
        for j in range(len(encrypted[i])):
            if encrypted[i][j] == '1' and binaries[i][j] == '1':
                temp+='0'
            elif encrypted[i][j] == '1' or binaries[i][j] == '1':
                temp+='1'
            else:
                temp+='0'


        decryptBinary.append(temp)

    print(decryptBinary)


def BinaryToText(encrypted):
    finalString = ''
    for binary in encrypted:

        binary_int = int(binary, 2)
        ascii_char = chr(binary_int)
        finalString += ascii_char

    return finalString
        


binaries = randomKey(message)
encrypted, messagebin = encrypt(message, binaries)
justwork = BinaryToText(encrypted)


print(messagebin)
print(binaries)
print(encrypted)
print(f"Final encrypted message (it is there): {justwork}")
decrypt(encrypted, binaries)

