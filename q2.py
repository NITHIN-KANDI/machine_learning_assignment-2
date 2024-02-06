import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

def k_nearest_neighbors(X_train, y_train, x_test, k):
    distances = []
    for i in range(len(X_train)):
        dist = euclidean_distance(X_train[i], x_test)
        distances.append((dist, y_train[i]))
    
    distances = sorted(distances)[:k]
    
    neighbor_labels = [label for (_, label) in distances]
    most_common = Counter(neighbor_labels).most_common(1)
    
    return most_common[0][0]
if __name__=="__main__":
    X_train = np.array([[1, 2], [2, 3], [3, 4], [5, 6]])
    y_train = np.array([0, 0, 1, 1])
    x_test = np.array([4, 5])
    k = 3
    predicted_class = k_nearest_neighbors(X_train, y_train, x_test, k)
    print("Predicted class:", predicted_class)
