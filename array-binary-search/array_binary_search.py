def BinarySearch(list,k):
         min_number = 0     
         max_number = len(list) -1     
         mid = (max_number + min_number)  //2   
         while (list[mid] != k):
                    if (min_number >= max_number ):
                                     return -1         
                    elif (list[mid] > k):
                                     max_number =mid -1

                    elif (list[mid] < k):
                                     min_number= mid + 1         
                    mid = (max_number + min_number) //2

         return mid     
         

print(BinarySearch([4, 8, 15, 16, 23, 42], 15))  
print(BinarySearch([-131, -82, 0, 27, 42, 68, 179], 42))  
print(BinarySearch([11, 22, 33, 44, 55, 66, 77], 90))  
print(BinarySearch([1, 2, 3, 5, 6, 7], 4))
