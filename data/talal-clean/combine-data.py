import os
import pickle
import pandas as pd

def load_and_concatenate_data(folder):
    dataframes = []
    
    # Iterate through all the .pkl files in the specified folder
    for filename in os.listdir(folder):
        if filename.endswith('.pkl'):
            file_path = os.path.join(folder, filename)
            # Unpickle the data
            with open(file_path, 'rb') as f:
                data = pickle.load(f)
                
                # Convert to DataFrame
                df = pd.DataFrame(data)
                
                # Add the 'd_class' column
                df['d_class'] = "talal-" + filename[:-4].lower()
                
                # Append DataFrame to the list
                dataframes.append(df)
    
    # Concatenate all DataFrames in the list
    return pd.concat(dataframes, ignore_index=True)

directories = ['test', 'train', 'valid']

# Store concatenated DataFrames
all_data = {}

# Loop through each directory and concatenate data
for directory in directories:
    all_data[directory] = load_and_concatenate_data(directory)

# Optionally, save the concatenated DataFrames to new .pkl files
for directory, dataframe in all_data.items():
    output_file = f"{directory}.pkl"
    dataframe.to_pickle(output_file)

print("Data concatenation completed. Concatenated files are saved as .pkl.")
