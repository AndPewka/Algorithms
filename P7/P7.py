from test import *
from time import time

def vertical(fileName):
    with open(fileName,"r") as file:
        text = file.read()

    text = text.replace(" ","\n")
    with open(fileName,"w") as file:
        file.write(text)

def fileAppend(fileName,value):
    with open(fileName,"r") as file:
        text = file.read()
    if text:
        value = " " + value

    with open(fileName,"a") as file:
        file.write(value)

def fileClear(fileName):
    with open(fileName,"w") as file:
        file.write("")

# with open("A.txt","w") as file:
#     file.write("8 2 23 27 5 3 65 68 44 42 33 40 1 0 6 10 2")
# fileClear("B.txt")
# fileClear("C.txt")

def merge(left, right):
    # Если первый массив пуст, то ничего не нужно
    # для объединения, и вы можете вернуть второй массив в качестве результата
    if len(left) == 0:
        right = str(right).replace("[","")
        right = str(right).replace("]","")

        return "[" + str(right).replace(" ","") + "]"

    # Если второй массив пуст, то ничего не нужно
    # для объединения, и вы можете вернуть первый массив как результат
    if len(right) == 0:
        left = str(left).replace("[","")
        left = str(left).replace("]","")
        return "[" + str(left).replace(" ","") + "]"

    result = []
    index_left = index_right = 0
    text = ""

    # Теперь перебираем оба массива, пока все элементы
    # превратить его в результирующий массив
    while len(result) < len(left) + len(right):
        # Элементы необходимо отсортировать, чтобы добавить их в
        # результирующий массив, поэтому вам нужно решить, получать ли
        # следующий элемент из первого или второго массива
        if left[index_left] <= right[index_right]:
            text = text + str(left[index_left]) + ", "
            # result.append(left[index_left])
            index_left += 1
        else:
            text = text + str(right[index_right]) + ", "
            # result.append(right[index_right])
            index_right += 1

        # Если вы дойдете до конца любого массива, вы можете
        # добавляем оставшиеся элементы из другого массива в
        # результат и разорвать цикл
        if index_right == len(right):
            for i in left[index_left:]:
                text = text + str(i) + ", "
            # result += left[index_left:]
            break

        if index_left == len(left):
            for i in right[index_right:]:
                text = text + str(i) + ", "
            # result += right[index_right:]
            break
    text = "[" + text.replace(" ","")[:-1] + "]"
    return text

def transResult():
    with open("A.txt","r") as file:
        text = file.read()
        
        text = text.replace(","," ")
        text = text.replace("[","")
        text = text.replace("]","")

    with open("A.txt","w") as file:
        file.write(text)

def scatterValues():
    vertical("A.txt")
    with open("A.txt","r") as file:
        line = "123"
        count = 0
        while line:
            line = file.readline().replace("\n","")
            if not line:
                continue
            count += 1

            if count%2==1:
                fileAppend("B.txt",line)
            else:
                fileAppend("C.txt",line)
        fileClear("A.txt")

def getCountEl(fileName):
    vertical(fileName)
    with open(fileName,"r") as file:
        line = "123"
        count = 0
        while line:
            line = file.readline().replace("\n","")
            if not line:
                continue
            count += 1
    
    return count

    
def sorterBC():
    fileB = open("B.txt", "r")
    fileC = open("C.txt", "r")
    vertical("B.txt")
    vertical("C.txt")
    while True:
        flag = False
        multy = False

        lineB = fileB.readline().replace("\n","")
        lineC = fileC.readline().replace("\n","")
        if "[" in lineB:
            multy = True
        
        if not lineB or not lineC:
            flag = True

        if not lineB and not lineC:
            break

        if multy==False:
            # print("{} - {}".format(lineB,lineC))
            if lineB > lineC:
                text = "[" + lineC + "," + lineB + "]"
            else:
                text = "[" + lineB + "," + lineC + "]"
            
            if flag:
                text = text.replace(",","")
            
            fileAppend("A.txt",text)
            

        else:
            it = 0
            lineB = eval(lineB)
            if lineC:
                lineC = eval(lineC)
            else:
                lineC = []
            
            if isinstance(lineB,int): #если множество заданий
                lineB = [lineB]
            
            if isinstance(lineC,int): #если множество заданий
                lineC = [lineC]

            text = "["

            print("lineB -->{}".format(lineB))
            print("lineC -->{}".format(lineC))

            text = merge(sorted(lineB),sorted(lineC))
            print(text)

            print(" ")

            # sorting = sorting.replace("[","(")
            # sorting = sorting.replace("]",")")
            fileAppend("A.txt",text)

        
    fileClear("B.txt")
    fileClear("C.txt")
    fileB.close()
    fileC.close()
    
flag = False
start_time = time()

while True:
    scatterValues()
    nB = getCountEl("B.txt")
    if nB == 1:
        flag = True

    sorterBC()

    if flag == True:
        transResult()
        break


with open("A.txt","r") as file:
    save = file.read()

end_time = time()
print("\nlist delete for {} sec".format(end_time - start_time))

number = 3
vertical("A.txt")
line="123"
with open("A.txt","r") as file:
    number+= 1
    while line and number>0:
        number-=1
        line = file.readline()

with open("A.txt","w") as file:
    file.write(save)

print(line)
print("file was sorted")








