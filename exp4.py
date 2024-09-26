import pandas as pd

# Function to load the dataset (CSV format for this example)
def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found at {file_path}. Please check the path.")
        return None

# Function to display details of the dataset
def display_dataset_details(df):
    if df is not None:
        # Display number of rows and columns
        print(f"Number of rows: {df.shape[0]}")
        print(f"Number of columns: {df.shape[1]}")
        
        # Display first five rows
        print("\nFirst five rows:")
        print(df.head())
        
        # Display dataset size
        print(f"\nDataset size (rows * columns): {df.size}")
        
        # Display missing values in each column
        print("\nMissing values in each column:")
        print(df.isnull().sum())
        
        # Summary statistics for numerical columns
        print("\nStatistical Summary of Numerical Columns:")
        print(df.describe())
        
        # Sum, Average, Min, Max for numerical columns
        print("\nSum of numerical columns:")
        print(df.sum(numeric_only=True))
        
        print("\nAverage of numerical columns:")
        print(df.mean(numeric_only=True))
        
        print("\nMinimum values in numerical columns:")
        print(df.min(numeric_only=True))
        
        print("\nMaximum values in numerical columns:")
        print(df.max(numeric_only=True))
    else:
        print("No dataset to display.")

# Function to export the dataset
def export_dataset(df, output_path):
    if df is not None:
        df.to_csv(output_path, index=False)
        print(f"Dataset exported successfully to {output_path}")
    else:
        print("No dataset to export.")

# Example usage
if __name__ == "__main__":
    file_path = "your_dataset.csv"  # Replace with the actual file path
    output_path = "exported_dataset.csv"  # Replace with the desired output path
    
    # Load dataset
    df = load_dataset(file_path)
    
    # Display dataset details
    display_dataset_details(df)
    
    # Export dataset to a new CSV file
    export_dataset(df, output_path)
