import pandas as pd

df = pd.read_csv(
    "data/student_data.csv",
    sep=";"
)

print(df.head())
print(df.columns)
print(df.shape)

# Remove exact duplicate rows
df = df.drop_duplicates()

# Drop rows where all values are missing
df = df.dropna(how="all")

# Fill missing numeric values with column median
numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Fill missing categorical values with column mode
categorical_cols = df.select_dtypes(include="object").columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Strip extra whitespace from string columns
for col in categorical_cols:
    df[col] = df[col].astype(str).str.strip()

print("Cleaned Dataset Shape:", df.shape)

# Save cleaned dataset
df.to_csv(
    "data/cleaned_student_data.csv",
    sep=";",
    index=False
)

print("cleaned_student_data.csv saved successfully")