
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

