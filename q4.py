def one_hot_encode_categorical(data):
    unique_categories = list(set(data))
    unique_categories.sort()
    encoded_data = []
    for category in data:
        encoded_category = [0] * len(unique_categories)
        category_index = unique_categories.index(category)
        encoded_category[category_index] = 1
        encoded_data.append(encoded_category)
    return encoded_data

categorical_data = ['red', 'blue', 'green', 'red', 'yellow', 'blue']
encoded_data = one_hot_encode_categorical(categorical_data)
print("One-Hot Encoded Data:")
for data_point in encoded_data:
    print(data_point)
