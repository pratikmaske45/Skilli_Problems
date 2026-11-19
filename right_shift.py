# Right Shift Array by N Positions
from typing import List

def rightShift(arr: List[int], K: int) -> List[int]:
    n = len(arr)
    if K >= n:
        return [0] * n
    if K <= 0:
        return list(arr)
    return [0] * K + arr[:n - K]  
