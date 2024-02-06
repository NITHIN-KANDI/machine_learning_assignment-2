import math

def euclidean_distance(vector1,vector2):
    if len(vector1)!=len(vector2): #checking if there are any dimensionality errors in the vectors
        raise ValueError("Vectors must have the same dimensionality")
    
    squared_distance=sum((x - y)**2 for x,y in zip(vector1,vector2))
    return math.sqrt(squared_distance)#returning the euclidean distance value

def manhattan_distance(vector1, vector2):
    if len(vector1)!=len(vector2):#checking if there are any dimensionality errors in the vectors
        raise ValueError("Vectors must have the same dimensionality")
    
    return sum(abs(x - y) for x, y in zip(vector1,vector2))#returning the manhattan distance
if __name__=="__main__":
    
    
    #Examples
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]
    print("Euclidean distance for the vectors :",euclidean_distance(vector1,vector2))
    print("Manhattan distance for the vectors:",manhattan_distance(vector1,vector2))
   



