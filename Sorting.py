
# returns a sorted array of the first k elements
def sortArrays(arr1, arr2, k):
    arr1.extend(arr2) # combine both arrays
    arr1.sort() # sort combined array
    return arr1[:k] # return sorted array of first k elements


