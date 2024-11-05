import os
import pickle
import pandas as pd


def load_and_concatenate_data(folder):
    dataframes = []

    # Iterate through all the .pkl files in the specified folder
    for filename in os.listdir(folder):
        if filename.endswith(".pkl"):
            file_path = os.path.join(folder, filename)
            # Unpickle the data
            with open(file_path, "rb") as f:
                data = pickle.load(f)

                # Convert to DataFrame
                df = pd.DataFrame(data)

                # Add the 'd_class' column
                df["d_class"] = "talal-" + filename[:-4].lower()

                # Append DataFrame to the list
                dataframes.append(df)

    # Concatenate all DataFrames in the list
    return pd.concat(dataframes, ignore_index=True)


pik_types = ["test", "train", "valid"]

for type in pik_types:
    talal = pickle.load(open(f"./talal-clean/{type}.pkl", "rb"))
    liam = pickle.load(open(f"./liam-clean/{type}.pkl", "rb"))
    liam["d_class"] = "liam-" + liam["d_class"]
    data = pd.concat([talal, liam])
    pickle.dump(data, open(f"./{type}.pkl", "wb"))

print("Data concatenation completed. Concatenated files are saved as .pkl.")
