import numpy as np
#%matplotlib qt
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

def kNearestNeighbors(k): 
    rand = np.random.RandomState(42)
    X = rand.rand(10,2)
    print("X-Array is:\n", X)

    plt.scatter(X[:, 0], X[:, 1], s=100)
    # plt.show(block=True)

    # Difference between each pair of points
    differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
    print("Distances between each points:\n", differences)
    print("Shape: ", differences.shape)

    # Quare the coordinate differences
    sq_differences = differences ** 2
    print("Squared Differences:\n", sq_differences)
    print("Shape: ", sq_differences.shape )

    # Sum it up from last to first
    dist_sq = sq_differences.sum(axis = -1)
    print("Summed up : \n", dist_sq)

    # Sort to nearest neighbor
    nearest = np.argsort(dist_sq, axis=1)
    print("Nearest Neighbor:\n", nearest)

    nearest_partition = np.argpartition(dist_sq, k+1, axis=1)
    print("Just the nearest k neighbors indices\n", nearest_partition )

    nearest_partition_data = np.partition(dist_sq, k+1, axis=1)
    print("Data of nearest partition:\n", nearest_partition_data)

    # Print all k nearest neighbors like:
    # point 1: nearest point 3
    # Why isn't the nearest point the point itself? 
    print("Print nearest neighbors:\n", nearest_partition[:, :k+1])

    # Print Plot and combine the lines

    plt.scatter(X[:, 0], X[:,1], s=100) 

    #draw lines from each point to its k nearest neighbors
    k=2
    for i in range(X.shape[0]):
        for j in nearest_partition[i, :k+1]:
                # plot a line from X[i] to X[j]
                # use some zip magic to make it happen
                plt.plot(*zip(X[j], X[i]), color="black")
    
    plt.show(block=True)