'''插入排序，线性查找，二进制相加'''
def insertSort(array):
    for i in range(1,len(array)):
        right = array[i]
        leftPointer = i - 1
        while(leftPointer >= 0 and right < array[leftPointer]):
            array[leftPointer + 1] = array[leftPointer]
            leftPointer -= 1
        array[leftPointer + 1] = right
    return array
def findLine(v,A):
    for i in range(len(A)):
        if (A[i] == v):
            return i
    return None
def binaryAdd(A,B):
    C = [0] * (len(A) + 1)
    carry = 0#进位
    for i in range(len(A) - 1, -1, -1):
        temp = A[i] + B[i] + carry
        C[i + 1] = temp % 2
        if (temp >= 2):
            carry = 1
        else:
            carry = 0
    C[0] = carry
    return C
def selectionSort(A):
    for i in range(0, len(A) - 1):
        minIndex = i
        for j in range(i + 1, len(A)):
            if (A[j] < A[minIndex]):
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]
    return A
