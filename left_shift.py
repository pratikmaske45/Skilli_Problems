# Left Shift Array by N Positions
def leftShift(arr: List[int], K: int) -> List[int]:

    # Write your solution here
    n = len(arr)
    if K >= n:
        return [0]*n 
    for i in range(n-K):
        arr[i]= arr[i+K]
    for i in range(n-K,n):
        arr[i]=0 
    return arr 
arr = [10,20,30,40,50]
K=2 
print(leftShift(arr,K))