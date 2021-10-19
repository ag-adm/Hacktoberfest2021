#Given an array of N integers. The task is to print the elements from the array which are greater than their immediate previous and next elements.

def printElements(arr, n):
     
    # Traverse array from index 1 to n-2
    # and check for the given condition
    for i in range(1, n - 1, 1):
        if (arr[i] > arr[i - 1] and
            arr[i] > arr[i + 1]):
            print(arr[i], end = " ")
 
# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 1, 5, 4, 9, 8, 7, 5]
    n = len(arr)
 
    printElements(arr, n)
     
