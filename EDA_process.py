import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load dataset
df = pd.read_csv(r"C:\Documents\Intership\samsung_global_sales_dataset.csv")   # Place your dataset in the same folder

# Step 2: Descriptive statistics
print("Summary Statistics:\n", df.describe())

# Step 3: Frequency counts for categorical variables
print("Product Category Counts:\n", df['ProductCategory'].value_counts())

# Step 4: Histogram for numerical variable
plt.hist(df['Revenue'], bins=20, color='skyblue', edgecolor='black')
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

# Step 5: Bar chart for categorical variable
df['ProductCategory'].value_counts().plot(kind='bar', color='orange')
plt.title("Product Category Distribution")
plt.show()
