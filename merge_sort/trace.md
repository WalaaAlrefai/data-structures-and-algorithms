# Merge Sort
- Merge Sort is an algorithm that finds the middle of the input array and splits it into two. Then, it uses recursion on both the left and right halves to sort. Finally, the two halves are merged in the merge method to return one full sorted array.
### Pseudo Code
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```
## Trace 
- #### Sample array: [8,4,23,42,16,15]

### Phase 1:
```
[8,4,23,42,16,15] -> [8,4,23]
                      |   |      
                    [8] [4,23] 
                         |  |        
                        [4] [23]    
```
1. Our sort method will divide (recursively) the array in half. 
2. The left side will be processed first, followed by the right. 
3. The halves will continue to be halved until there is a single value. 
4. Note that this visual is only meant to show the left side.* 

### Phase 2:
```
[8,4,23,42,16,15] -> [8,4,23]
                      |   |     
                    [8] [4,23]
# [4, 23] has been sorted!
[8,4,23,42,16,15] -> [4,8,23]
# Left side is all sorted!
```
- Now that we have all of these branches via recursion, it is time make our way back up with merge. 
1. Merge will evaluate values in the sub-arrays and swap positions to put each value in the correct order. 
2. With each step that we take back up, each sub-array will be properly sorted. 

### Phase 3:
```
[8,4,23,42,16,15] -> [4,8,23][42,16,15]
                               |   |
                             [42] [16,15]
                                   |
                                [16][15]
```
- Now it is time to do the right side of the array! 
1. It will go through the exact same recursive process. 
2. The right array will be split until we have single values.

### Phase 4:
```
[8,4,23,42,16,15] -> [4,8,23][42,16,15]
                               |   |
                             [42] [15,16]
# [15,16] now sorted!
[8,4,23,42,16,15] -> [4,8,23][15,16,42]
# right array fully sorted! 
```
- It is time make our way back up with merge.
1. merge will evaluate values in the right array and swap positions to put each value in the correct order. 
2. With each step that we take back up, each sub-array will be properly sorted.
                          
### Phase 5:
```
RETURN arr
Output: [4,8,15,16,23,42]
```
- Lastly 
1. merge is called to merge the two halves and do another comparison of values to put each value into the correct spot. 
2. 23 is placed after 16 while the arrays become one!                    

### Efficieny

- Time: O(nlog(n)): We will need to split the array a certain number of times. Basically, time will be proportional to the number of digits in n.
- Space: O(n): Space will be determined by the number of elements in the input array. 