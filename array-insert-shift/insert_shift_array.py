def insertShiftArray(list, num):
    if len(list) % 2 == 0:
        position = int(len(list)/2)
        list.insert(position, num)
        return list
    else :
        position1 = int (len(list)/2)+1
        list.insert(position1, num)
        return list
    
result = insertShiftArray([1,2,3], 4)
print(result)