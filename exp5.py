import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load the dataset (as in the previous example)
def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found at {file_path}. Please check the path.")
        return None

# Function to perform EDA on the dataset
def exploratory_data_analysis(df):
    if df is not None:
        # Display basic information about the dataset
        print("\nBasic Information:")
        print(df.info())

        # Summary statistics
        print("\nSummary Statistics:")
        print(df.describe())

        # Display column names and data types
        print("\nColumn Names and Data Types:")
        print(df.dtypes)

        # Checking for missing values
        print("\nMissing Values in Each Column:")
        print(df.isnull().sum())

        # Correlation matrix
        print("\nCorrelation Matrix:")
        correlation_matrix = df.corr(numeric_only=True)
        print(correlation_matrix)
        
        # Plotting heatmap of the correlation matrix
        plt.figure(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title("Correlation Matrix Heatmap")
        plt.show()

        # Plotting distributions for numerical columns
        numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
        for column in numerical_columns:
            plt.figure(figsize=(6, 4))
            sns.histplot(df[column].dropna(), kde=True)
            plt.title(f'Distribution of {column}')
            plt.show()

        # Boxplot for detecting outliers in numerical columns
        for column in numerical_columns:
            plt.figure(figsize=(6, 4))
            sns.boxplot(x=df[column].dropna())
            plt.title(f'Boxplot of {column} (Outlier Detection)')
            plt.show()

        # Pairplot to explore pairwise relationships between numerical columns
        sns.pairplot(df[numerical_columns])
        plt.title('Pairplot of Numerical Columns')
        plt.show()

        # Countplot for categorical columns (if applicable)
        categorical_columns = df.select_dtypes(include=['object']).columns
        for column in categorical_columns:
            plt.figure(figsize=(6, 4))
            sns.countplot(y=df[column])
            plt.title(f'Count of {column}')
            plt.show()

    else:
        print("No dataset to analyze.")

# Function to export the dataset (same as above)
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
    
    # Perform EDA
    exploratory_data_analysis(df)
    
    # Export dataset to a new CSV file
    export_dataset(df, output_path)
