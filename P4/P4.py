a=23
key = 10
count = 34

####################
print("\n\n\n\n")


    
def hash(value,key):
    result=value%key
    return result

def getValue(hashTable,targetHash,key):
    listValue=[]
    for hashDict in hashTable:
        if targetHash in hashDict:
            listValue = hashDict[targetHash]
    

    if listValue:
        return listValue
    
    return -1

def delValue(hashTable,hash):
    for i in range(len(hashTable)):
        if hashTable[i]["hash"] == hash:
            del hashTable[i]
            return 1
    return -1

def putValue(hashTable,value,key):
    targetHash = hash(value,key)
    for hashDict in hashTable:
        if targetHash in hashDict:
            listValue = hashDict[targetHash]
            if value not in listValue:
                listValue.reverse()
                listValue.append(value)
                listValue.reverse()
    return hashTable

def newPutValue(hashTable,value,key):
    targetHash = hash(value,key)
    here = False
    for hashDict in hashTable:
        if targetHash in hashDict:
            listValue = hashDict[targetHash]
            if not listValue or here:
                listValue.append(value)
            else:
                here = True
        
        for i in hashDict:
            listValue = hashDict[i]
        
        if not listValue and here:
            here = False
            listValue.append(value)

    return hashTable

def newGetValue(hashTable,value,key):
    targetHash = hash(value,key)
    here = False
    listValue=[]
    for hashDict in hashTable:
        if targetHash in hashDict or here:
            here = True
            
            for i in hashDict:
                if hashDict[i] == [value]:
                    return value

    return -1

def newDelValue(hashTable,value,key):
    targetHash = hash(value,key)
    here = False
    listValue=[]
    for hashDict in hashTable:
        if targetHash in hashDict or here:
            here = True
            
            for i in hashDict:
                if hashDict[i] == [value]:
                    hashDict[i] = []
    return -1

def delValue(hashTable,value,key):
    targetHash = hash(value,key)
    for hashDict in hashTable:
        if targetHash in hashDict:
            listValue = hashDict[targetHash]
            if value in listValue:
                del listValue[listValue.index(value)]

    return hashTable





hashTable = []
for i in range(key):
    table = {}
    table[hash(i,key)] = []
    hashTable.append(table)

print("hashTable was generated")

newPutValue(hashTable,2,key)
newPutValue(hashTable,12,key)
newPutValue(hashTable,2,key)
newPutValue(hashTable,2,key)
newPutValue(hashTable,14,key)
newPutValue(hashTable,74,key)


newDelValue(hashTable,14,key)
# newDelValue(hashTable,5,key)

for i in hashTable:
    print(i)

x = newGetValue(hashTable,14,key)
print(x)



# x = getValue(hashTable,0,key)

# print(x)







