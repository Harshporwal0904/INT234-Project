import pandas as pd

# Load the dataset
df = pd.read_csv('dataset.csv')

# Remove unnecessary columns
cols_to_drop = ["Timestamp", "Email Address", "Column 14"]
clean_df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

output_path = "clean_dataset.csv"
clean_df.to_csv(output_path, index=False)

output_path