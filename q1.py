def euclidean_distance(vector1, vector2):
    # Check if the lengths of the vectors are equal
    if len(vector1) != len(vector2):
        print("Please provide vectors of equal lengths")
        
    # Initialize the Euclidean distance to 0
    euclidean_dist = 0
    
    # Iterate over each element of the vectors
    for i in range(len(vector1)):
        # Add the square of the difference of corresponding elements to the Euclidean distance
        euclidean_dist += (vector1[i] - vector2[i]) ** 2
        
    # Return the square root of the sum of squared differences
    return euclidean_dist ** 0.5

def manhattan_distance(vector1, vector2):
    # Check if the lengths of the vectors are equal
    if len(vector1) != len(vector2):
        print("Please provide vectors of equal lengths")
        
    # Initialize the Manhattan distance to 0
    manhattan_dist = 0
    
    # Iterate over each element of the vectors
    for i in range(len(vector1)):
        # Add the absolute difference of corresponding elements to the Manhattan distance
        manhattan_dist += abs(vector1[i] - vector2[i])
        
    # Return the sum of absolute differences
    return manhattan_dist

# Example vectors
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

# Calculate and print the Euclidean distance
print("The Euclidean distance between the given vectors is:", euclidean_distance(vector1, vector2))

# Calculate and print the Manhattan distance
print("The Manhattan distance between the given vectors is:", manhattan_distance(vector1, vector2))
