# Array
array in python is **list type**(dynamically-resized)

## Todo
- study labuladong quick sort
- then finish question 5.1 with follow-up

## Basic
```sh
# init a list
[3,5,7,11]
list(range(100)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1] + [0]*10 # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


len(x)) # length of array
x.append(1) # add 1 to end
x.remove(2) # remove 2 from list
x.insert(3, 28) # add 28 to index 3

# init 2D array
x = [[1, 2, 4], [3, 5, 7, 9], [13]]
```

look up x in array time: o(n), n is size of arr

## copy
- shallow copy
- deep copy (totally individual one)

## key function
- min(), max()
- binary search of sorted lists: 
  - bisect.bisect()
  - bisect.bisect_left()
  - bisect.bisect_right()
- reverse: 
  - inplace: A.reverse()
  - return iterator reversed(A)
- sort: 
  - in place: A.sort()
  - return a copy: sorted(A)
- delete 
  - delete the i-th element: del A[i]
  - remove the lice(start from index i, end before index j): A[i:j]

## quick sort
[study quick sort](https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247496139&idx=1&sn=b0aca0f2b98e23495c9bd13bb4d90e40&chksm=9bd40fc3aca386d5687dc10ddb1034b71df7584add74c4eb5ab95bbcc2da58cf8402507fad24&scene=178&cur_album_id=1318883740306948097#rd)
快速排序是先将一个元素排好序，然后再将剩下的元素排好序。