"""
=============================================================
 PANDAS BASICS - DATA ANALYSIS FOR AI/ML
=============================================================
 Repository: ai-ml-learning
 GitHub: https://github.com/haroongetscoding/ai-ml-learning
 
 Pandas is the most important library for data manipulation
 and analysis in AI/ML.
=============================================================
"""

import pandas as pd
import numpy as np

print("=" * 60)
print(" PANDAS BASICS - DATA ANALYSIS")
print("=" * 60)


# ============================================================
# SECTION 1: SERIES - 1D DATA
# ============================================================

print("\n--- SECTION 1: SERIES ---\n")

# Creating Series
s1 = pd.Series([10, 20, 30, 40, 50])
print(f"Basic Series:\n{s1}\n")

# With custom index
s2 = pd.Series([100, 200, 300], index=["a", "b", "c"])
print(f"Custom Index:\n{s2}\n")

# From dictionary
s3 = pd.Series({"Haroon": 3.85, "Ali": 3.72, "Sara": 3.95})
print(f"From Dict:\n{s3}\n")

# Accessing elements
print(f"Index 0: {s1[0]}")
print(f"Index 'a': {s2['a']}")
print(f"Slice [0:3]:\n{s1[0:3]}")


# ============================================================
# SECTION 2: DATAFRAME - 2D DATA
# ============================================================

print("\n--- SECTION 2: DATAFRAME ---\n")

# Creating DataFrame from dictionary
data = {
    "Name": ["Haroon", "Ali", "Sara", "Ahmed", "Fatima"],
    "Age": [25, 23, 22, 28, 24],
    "CGPA": [3.85, 3.72, 3.95, 3.60, 3.88],
    "City": ["Karachi", "Lahore", "Islamabad", "Karachi", "Lahore"]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print(f"\nShape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Data Types:\n{df.dtypes}")


# ============================================================
# SECTION 3: READING & WRITING DATA
# ============================================================

print("\n--- SECTION 3: FILE OPERATIONS ---\n")

# Save to CSV
df.to_csv("students.csv", index=False)
print("Saved to students.csv")

# Read from CSV
df_read = pd.read_csv("students.csv")
print(f"\nRead from CSV:\n{df_read}")

# Save to Excel (requires openpyxl)
# df.to_excel("students.xlsx", index=False)

# Save to JSON
df.to_json("students.json", orient="records")
print("\nSaved to students.json")


# ============================================================
# SECTION 4: VIEWING DATA
# ============================================================

print("\n--- SECTION 4: VIEWING DATA ---\n")

print("First 3 rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nRandom sample:")
print(df.sample(2))

print("\nInfo:")
print(df.info())

print("\nDescribe (statistics):")
print(df.describe())

print("\nColumn values:")
print(f"Names: {list(df['Name'])}")
print(f"Ages: {list(df['Age'])}")


# ============================================================
# SECTION 5: SELECTING DATA
# ============================================================

print("\n--- SECTION 5: SELECTING DATA ---\n")

# Select column
print("Single column:")
print(df["Name"])

# Select multiple columns
print("\nMultiple columns:")
print(df[["Name", "CGPA"]])

# Select row by index
print("\nRow at index 0:")
print(df.iloc[0])

# Select rows by condition
print("\nStudents with CGPA > 3.8:")
print(df[df["CGPA"] > 3.8])

# Multiple conditions
print("\nStudents from Karachi with CGPA > 3.7:")
print(df[(df["City"] == "Karachi") & (df["CGPA"] > 3.7)])

# Select by position
print("\nFirst 3 rows, first 2 columns:")
print(df.iloc[:3, :2])


# ============================================================
# SECTION 6: ADDING & REMOVING COLUMNS
# ============================================================

print("\n--- SECTION 6: ADDING & REMOVING ---\n")

# Add new column
df["Grade"] = ["A", "B+", "A+", "B", "A"]
print("Added Grade column:")
print(df)

# Add computed column
df["CGPA x 10"] = df["CGPA"] * 10
print("\nAdded computed column:")
print(df)

# Remove column
df_dropped = df.drop(columns=["CGPA x 10"])
print("\nRemoved 'CGPA x 10':")
print(df_dropped)

# Add row
new_row = pd.DataFrame({
    "Name": ["Zara"],
    "Age": [21],
    "CGPA": [3.92],
    "City": ["Islamabad"],
    "Grade": ["A+"]
})
df = pd.concat([df, new_row], ignore_index=True)
print("\nAdded new row:")
print(df)


# ============================================================
# SECTION 7: HANDLING MISSING DATA
# ============================================================

print("\n--- SECTION 7: MISSING DATA ---\n")

# Create DataFrame with missing values
df_missing = pd.DataFrame({
    "A": [1, 2, np.nan, 4, 5],
    "B": [np.nan, 2, 3, np.nan, 5],
    "C": [1, 2, 3, 4, np.nan]
})

print("DataFrame with missing values:")
print(df_missing)

print(f"\nMissing values per column:\n{df_missing.isnull().sum()}")

print(f"\nTotal missing: {df_missing.isnull().sum().sum()}")

# Fill missing values
df_filled = df_missing.fillna(0)
print("\nFilled with 0:")
print(df_filled)

# Fill with mean
df_mean = df_missing.fillna(df_missing.mean())
print("\nFilled with mean:")
print(df_mean)

# Drop missing values
df_dropped = df_missing.dropna()
print("\nDropped missing:")
print(df_dropped)


# ============================================================
# SECTION 8: GROUPING & AGGREGATION
# ============================================================

print("\n--- SECTION 8: GROUPING ---\n")

# Create sales data
sales_data = {
    "Product": ["A", "B", "A", "B", "A", "B"],
    "Region": ["North", "North", "South", "South", "North", "South"],
    "Sales": [100, 150, 200, 180, 120, 160],
    "Units": [10, 15, 20, 18, 12, 16]
}

df_sales = pd.DataFrame(sales_data)
print("Sales Data:")
print(df_sales)

# Group by single column
print("\nTotal Sales by Product:")
print(df_sales.groupby("Product")["Sales"].sum())

# Group by multiple columns
print("\nTotal Sales by Product and Region:")
print(df_sales.groupby(["Product", "Region"])["Sales"].sum())

# Multiple aggregations
print("\nStatistics by Product:")
print(df_sales.groupby("Product").agg({
    "Sales": ["sum", "mean", "max"],
    "Units": ["sum", "mean"]
}))


# ============================================================
# SECTION 9: MERGING & JOINING
# ============================================================

print("\n--- SECTION 9: MERGING & JOINING ---\n")

# Create two DataFrames
df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Haroon", "Ali", "Sara", "Ahmed"]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3, 5],
    "Score": [85, 90, 78, 92]
})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Inner join
inner = pd.merge(df1, df2, on="ID", how="inner")
print("\nInner Join:")
print(inner)

# Left join
left = pd.merge(df1, df2, on="ID", how="left")
print("\nLeft Join:")
print(left)

# Right join
right = pd.merge(df1, df2, on="ID", how="right")
print("\nRight Join:")
print(right)

# Outer join
outer = pd.merge(df1, df2, on="ID", how="outer")
print("\nOuter Join:")
print(outer)


# ============================================================
# SECTION 10: DATA TRANSFORMATION
# ============================================================

print("\n--- SECTION 10: TRANSFORMATION ---\n")

# Apply function
df["Grade_Point"] = df["CGPA"].apply(lambda x: x * 25)
print("Applied lambda function:")
print(df)

# Map values
city_map = {"Karachi": "KHI", "Lahore": "LHR", "Islamabad": "ISB"}
df["City_Code"] = df["City"].map(city_map)
print("\nMapped city codes:")
print(df)

# Rename columns
df_renamed = df.rename(columns={"Name": "Student_Name", "Age": "Student_Age"})
print("\nRenamed columns:")
print(df_renamed.head())

# Sort
print("\nSorted by CGPA (descending):")
print(df.sort_values("CGPA", ascending=False))


# ============================================================
# SECTION 11: PRACTICAL EXAMPLE - DATA ANALYSIS
# ============================================================

print("\n--- SECTION 11: PRACTICAL ANALYSIS ---\n")

# Create realistic dataset
np.random.seed(42)
n = 100

dataset = pd.DataFrame({
    "Student_ID": range(1, n + 1),
    "Name": [f"Student_{i}" for i in range(1, n + 1)],
    "Age": np.random.randint(18, 30, n),
    "CGPA": np.round(np.random.uniform(2.0, 4.0, n), 2),
    "Department": np.random.choice(["CS", "AI", "Data Science", "SE"], n),
    "City": np.random.choice(["Karachi", "Lahore", "Islamabad", "Peshawar"], n)
})

print("Dataset (first 10 rows):")
print(dataset.head(10))
print(f"\nTotal students: {len(dataset)}")

# Analysis
print("\n--- ANALYSIS ---")
print(f"\nAverage CGPA: {dataset['CGPA'].mean():.2f}")
print(f"Highest CGPA: {dataset['CGPA'].max():.2f}")
print(f"Lowest CGPA: {dataset['CGPA'].min():.2f}")
print(f"Average Age: {dataset['Age'].mean():.1f}")

# Department-wise stats
print("\nDepartment Statistics:")
dept_stats = dataset.groupby("Department").agg({
    "CGPA": ["mean", "max", "count"],
    "Age": "mean"
})
print(dept_stats)

# Top students
print("\nTop 5 Students by CGPA:")
top_students = dataset.nlargest(5, "CGPA")
print(top_students[["Name", "CGPA", "Department"]])

# City distribution
print("\nStudents per City:")
print(dataset["City"].value_counts())


# ============================================================
# CLEANUP FILES
# ============================================================

import os
for file in ["students.csv", "students.json"]:
    if os.path.exists(file):
        os.remove(file)


# ============================================================
# SUMMARY
# ============================================================

print("\n" + "=" * 60)
print(" PANDAS COMPLETE!")
print("=" * 60)
print("\n Key Takeaways:")
print("  1. DataFrames are 2D labeled arrays")
print("  2. Easy file I/O (CSV, Excel, JSON)")
print("  3. Powerful filtering with boolean conditions")
print("  4. GroupBy for aggregation")
print("  5. Merge/Join for combining datasets")
print("\n Next: Matplotlib for Visualization")
print("=" * 60)
