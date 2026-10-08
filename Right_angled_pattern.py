# Right Triangle Pattern
# Right Triangle Pattern
# Given an integer n, generate a right-angled triangle pattern of asterisks (*) of height n.

# Return the result as a list of strings, where each string corresponds to one row of the triangle.

# Row 1: "*"
# Row 2: "**"
# Row i: "*" * i
def rightTrianglePattern(n: int) -> list[str]:
    result =[]
    for i in range(1,n+1):
        row = "*" * i
        result.append(row)
    return(result)    
print(rightTrianglePattern(4))