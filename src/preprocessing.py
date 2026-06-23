import pandas as pd

df = pd.read_csv(
    "data/student_data.csv",
    sep=";"
)

print(df.head())
print(df.columns)
print(df.shape)
