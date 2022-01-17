from random import randint
import os
from time import time

os.system("cls")
count = 10
word = "hello my name is andrey"
word_massive=word.split(" ")
symb = "is"





def interSearch(word_massive, check):
    dict_words = []
    val_massive = []

    for word in word_massive:
        dict_words.append({})
        dict_words[len(dict_words)-1]["word"] = word
        dict_words[len(dict_words)-1]["val"] = 0
        count = 0
        for symb in word:
            count += 1
            dict_words[len(dict_words)-1]["val"]+= ord(symb) + ord(symb) * count
        val_massive.append(dict_words[len(dict_words)-1]["val"])

    count = 0
    val = 0
    for symb in check:
        count += 1
        val += ord(symb) + ord(symb) * count


    val_massive = sorted(val_massive)

    beg = 0
    end = (len(dict_words) - 1)

    while beg <= end and val >= val_massive[beg] and val <= val_massive[end]:
        middle = beg + int((float((end - beg) / ( val_massive[end] - val_massive[beg])) * ( val - val_massive[beg])))
        if val_massive[middle] == val:
            for node in range(len(dict_words)):
                if dict_words[node]["val"] == val:
                    return node
        if val_massive[middle] < val:
            beg = middle + 1;
        else:
            end = middle - 1;

def lineSearch(word_massive,word):

    for i in range(len(word_massive)):
        if word_massive[i] == word:
            return i

def binSearch(word_massive,check):
    dict_words = []
    val_massive = []

    for word in word_massive:
        dict_words.append({})
        dict_words[len(dict_words)-1]["word"] = word
        dict_words[len(dict_words)-1]["val"] = 0
        count = 0
        for symb in word:
            count += 1
            dict_words[len(dict_words)-1]["val"]+= ord(symb) + ord(symb) * count
        val_massive.append(dict_words[len(dict_words)-1]["val"])

    count = 0
    val = 0
    for symb in check:
        count += 1
        val += ord(symb) + ord(symb) * count

    val_massive = sorted(val_massive)

    mid = len(val_massive) // 2
    low = 0
    high = len(val_massive) - 1

    while val_massive[mid] != val and low <= high:

        if val > val_massive[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low <= high:
        for node in range(len(dict_words)):
            if dict_words[node]["val"] == val:
                return node



print(word_massive)
print(symb)

start_time = time()
index = interSearch(word_massive,symb)
end_time = time()
print("interSearch -- > {} for {} sec".format(index,end_time-start_time))


start_time = time()
index = lineSearch(word_massive,symb)
end_time = time()
print("lineSearch -- > {} for {} sec".format(index,end_time-start_time))


start_time = time()
index = binSearch(word_massive,symb)
end_time = time()
print("binSearch -- > {} for {} sec".format(index,end_time-start_time))

