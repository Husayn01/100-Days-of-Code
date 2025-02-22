testList = [1, -4, 8, -9]
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def minusOne(a):
    return a + 1
applyToEach(testList, minusOne)
#  [2, -3, 9, -8]

def square(a):
    return a * a
applyToEach(testList, square)
# [1, 16, 64, 81]