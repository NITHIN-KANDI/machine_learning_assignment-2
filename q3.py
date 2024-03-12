def categorical_to_numerical(categories):
    # Dictionary to store the encoding of each category
    encoding_dict = {}
    # Counter to keep track of the numerical encoding
    numerical_value = 0
    
    # Iterate through each category
    for category in categories:
        # Check if the category is not already encoded
        if category not in encoding_dict:
            # Assign a numerical value to the category and increment the counter
            encoding_dict[category] = numerical_value
            numerical_value += 1
    
    # Return a list of numerical values corresponding to the input categories
    return [encoding_dict[category] for category in categories]

# Example categories
categories = ['One', 'Two', 'One', 'Three', 'Three', 'One', 'Two']

# Convert categorical values to numerical representations
encoded_values = categorical_to_numerical(categories)

# Print the encoded values
print("Encoded values:", encoded_values)
