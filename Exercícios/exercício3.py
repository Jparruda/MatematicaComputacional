import math
def serieDeTaylor(n : int, x : float) -> float:
    k = 0
    for i in range(k, n + 1):
       serie = (x**i)/math.factorial(i)
    return serie


