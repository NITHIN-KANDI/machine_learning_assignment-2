def label_encode_categorical(data):
    label_mapping = {}
    label_counter = 0
    
    for category in data:
        if category not in label_mapping:
            label_mapping[category] = label_counter
            label_counter += 1
    
    return label_mapping
if __name__=="__main__":
    categorical_data = ['red', 'blue', 'green', 'red', 'yellow', 'blue']
    label_mapping = label_encode_categorical(categorical_data)
    print("Label Mapping:", label_mapping)
    encoded_data = [label_mapping[category] for category in categorical_data]
    print("Encoded Data:", encoded_data)
