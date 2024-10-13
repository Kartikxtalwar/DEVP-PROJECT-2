import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the Streamlit App
st.title("Trade Data Visualization Dashboard")

# Load dataset (ensure to replace the file path with your actual data file path)
data = pd.read_csv("Imports_Exports_Dataset.csv")


# 1. Scatter Plot: Quantity vs. Value
st.header("Scatter Plot: Quantity vs. Value")
plt.figure(figsize=(8, 6))
plt.scatter(df['Quantity'], df['Value'], color='blue', alpha=0.5)
plt.title('Scatter Plot of Quantity vs. Value')
plt.xlabel('Quantity')
plt.ylabel('Value')
plt.grid(True)
st.pyplot(plt)
plt.clf()  # Clear the plot

# 2. Line Plot: Quantity Over Time (Date vs Quantity)
st.header("Line Plot: Quantity Over Time")
st.subheader("Ensure that your dataset has a 'Date' column")

# Check if 'Date' is in the dataset and adjust if needed
if 'Date' not in df.columns and 'Date' in df.index.names:
    df.reset_index(inplace=True)
    st.write("'Date' was in the index. Resetting the index.")

# Rename any column that might be named like 'Date'
if 'Date' not in df.columns:
    for col in df.columns:
        if 'date' in col.lower():
            df.rename(columns={col: 'Date'}, inplace=True)
            st.write(f"Renaming column '{col}' to 'Date'.")

# Plot only if 'Date' column is found
if 'Date' in df.columns:
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Quantity'], color='green', linestyle='-', marker='o')
    plt.title('Line Plot of Quantity Over Time')
    plt.xlabel('Date')
    plt.ylabel('Quantity')
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()
else:
    st.write("The 'Date' column still does not exist. Please check your dataset.")

# 3. Bar Chart: Top 10 Countries by Trade Quantity and Value
st.header("Bar Charts: Top 10 Countries by Trade Quantity and Value")

top_countries = df.groupby('Country').agg({
    'Quantity': 'sum',
    'Value': 'sum'
}).sort_values(by='Value', ascending=False).head(10)

# Bar Chart for Quantity
st.subheader("Top 10 Countries by Trade Quantity")
plt.figure(figsize=(10, 6))
top_countries['Quantity'].plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries by Trade Quantity')
plt.xlabel('Country')
plt.ylabel('Total Trade Quantity')
plt.xticks(rotation=45)
st.pyplot(plt)
plt.clf()

# Bar Chart for Value
st.subheader("Top 10 Countries by Trade Value")
plt.figure(figsize=(10, 6))
top_countries['Value'].plot(kind='bar', color='lightgreen')
plt.title('Top 10 Countries by Trade Value')
plt.xlabel('Country')
plt.ylabel('Total Trade Value')
plt.xticks(rotation=45)
st.pyplot(plt)
plt.clf()

# 4. Scatter Plot: Trade Value vs. Quantity by Shipping Method
st.header("Scatter Plot: Trade Value vs. Quantity by Shipping Method")
plt.figure(figsize=(10, 6))

# Subset data by Shipping Method
shipping_methods = df['Shipping_Method'].unique()

for method in shipping_methods:
    subset = df[df['Shipping_Method'] == method]
    plt.scatter(subset['Quantity'], subset['Value'], label=method, alpha=0.6)

plt.title('Trade Value vs. Quantity by Shipping Method')
plt.xlabel('Trade Quantity')
plt.ylabel('Trade Value')
plt.legend(title="Shipping Method")
st.pyplot(plt)
plt.clf()

# 5. Box Plot: Quantity by Import/Export
st.header("Box Plot: Quantity by Import/Export")
plt.figure(figsize=(8, 6))
sns.boxplot(x='Import_Export', y='Quantity', data=df)
plt.title('Box-Whisker Plot of Quantity by Import/Export')
plt.xlabel('Import/Export')
plt.ylabel('Quantity')
st.pyplot(plt)
plt.clf()

# 6. Pie Chart: Distribution of Trade Value by Product Category
st.header("Pie Chart: Distribution of Trade Value by Product Category")
product_categories = df.groupby('Category').agg({
    'Value': 'sum'
}).sort_values(by='Value', ascending=False)

plt.figure(figsize=(8, 8))
plt.pie(product_categories['Value'], labels=product_categories.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Trade Value by Product Category')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
st.pyplot(plt)
plt.clf()

# 7. Histogram: Distribution of Trade Value
st.header("Histogram: Distribution of Trade Value")
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Value', bins=30, kde=True)
plt.title('Distribution of Trade Value')
st.pyplot(plt)
plt.clf()

# 8. Pie Chart: Proportion of Import vs. Export
st.header("Pie Chart: Proportion of Import vs. Export")
import_export_counts = df['Import_Export'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(import_export_counts, labels=import_export_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen'])
plt.title('Proportion of Import vs Export')
st.pyplot(plt)
plt.clf()
