import numpy as np 

def selectionSort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

def bogoSort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x

x = np.array([1,5,4,2,9,5,4,10,3])
print("Original Array:", x)
x = np.array([1,5,4,2,9,5,4,10,3])
print("Selection Sort: ", selectionSort(x))
x = np.array([1,5,4,2,9,5,4,10,3])
print("bogoSort", bogoSort(x))
x = np.array([1,5,4,2,9,5,4,10,3])
print("np.sort:", np.sort(x))
x = np.array([1,5,4,2,9,5,4,10,3])
print("indices of sorted", np.argsort(x))
x = np.array([1,5,4,2,9,5,4,10,3])


rand = np.random.RandomState(42)
X = rand.randint(0, 10, (4,6))
print(X)

x = np.array([7,2,3,1,6,5,4])

