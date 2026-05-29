import pandas as pd

df = pd.read_csv('vgsales.csv')
original_shape = df.shape

print("Missing Values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# Fill missing Year with median
if df['Year'].isnull().sum() > 0:
    median_year = df['Year'].median()
    df['Year'] = df['Year'].fillna(median_year)
    print(f"\nFilled missing Year values with median: {median_year}")

# Fill missing Publisher with 'Unknown'
if df['Publisher'].isnull().sum() > 0:
    df['Publisher'] = df['Publisher'].fillna('Unknown')
    print("Filled missing Publisher values with {'Unknown'}")

# Remove duplicates
duplicates = df.duplicated().sum()
if duplicates > 0:
    df = df.drop_duplicates()
    print(f"Removed {duplicates} duplicate records")

# Convert Year to integer safely
# Use 'Int64' (nullable integer type) to handle any remaining NaN
df['Year'] = df['Year'].astype('Int64')

print(f"\nOriginal shape: {original_shape}")
print(f"Cleaned shape:  {df.shape}")
print(f"Records removed: {original_shape[0] - df.shape[0]}")

# Save cleaned data for use in later sections
df.to_csv('vgsales_cleaned.csv', index=False)
print("\nCleaned data saved as vgsales_cleaned.csv")
