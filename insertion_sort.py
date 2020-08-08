def insertionSort(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      # Move elements of arr[0..i-1], that are greater
      
      # to one position ahead of their current position
      j = i-1
      while j >=0 and key < arr[j] :
         arr[j+1] = arr[j]
         j -= 1
      arr[j+1] = key
# main
arr = ['12','11','55','30','90','48','39','89']
insertionSort(arr)
print ("The sorted array is:")
for i in range(len(arr)):
   print (arr[i])
