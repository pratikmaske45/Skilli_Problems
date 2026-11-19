# Insert Element at a Given Position
def  insertAtPosition(arr: List[int], X: int, P: int) -> List[int]:
    # Write your solution here
    n=len(arr)
    for i in range(n-1,P,-1):
        arr[i]=arr[i-1]
    arr[P] = X
    return arr
arr = [10,20,30,40,50]
X= 99
P = 2 
print(insertAtPosition(arr,X,P))