import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the Streamlit App
st.title("Trade Data Analysis and Visualization Dashboard")


# Load dataset (ensure to replace the file path with your actual data file path)
df = pd.read_csv("Imports_Exports_Dataset.csv")
# Display the first few rows of the dataframe
st.write("Data Preview:")
st.write(df.head())

# Plot 1: Scatter Plot of Quantity vs. Value
st.header("Scatter Plot: Quantity vs. Value")
plt.figure(figsize=(8, 6))
plt.scatter(df['Quantity'], df['Value'], color='blue', alpha=0.5)
plt.title('Scatter Plot of Quantity vs. Value')
plt.xlabel('Quantity')
plt.ylabel('Value')
plt.grid(True)
st.pyplot(plt)
st.write("**Analysis**: This scatter plot reveals the relationship between trade quantity and value. Higher quantities often correspond to higher values, but some outliers show different patterns.")

# Plot 2: Line Plot - Quantity Over Time (if 'Date' column exists)
st.header("Line Plot: Quantity Over Time")
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])  # Ensure 'Date' is datetime
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Quantity'], color='green', linestyle='-', marker='o')
    plt.title('Line Plot of Quantity Over Time')
    plt.xlabel('Date')
    plt.ylabel('Quantity')
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(plt)
    st.write("**Analysis**: This line plot shows the changes in trade quantity over time. Peaks in the graph suggest periods of increased trade activity, possibly linked to specific events.")
else:
    st.write("The 'Date' column is not present in the dataset.")

# Plot 3: Bar Chart - Top 10 Countries by Trade Quantity
st.header("Bar Chart: Top 10 Countries by Trade Quantity")
top_countries_quantity = df.groupby('Country').agg({'Quantity': 'sum'}).sort_values(by='Quantity', ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_countries_quantity['Quantity'].plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries by Trade Quantity')
plt.xlabel('Country')
plt.ylabel('Total Trade Quantity')
plt.xticks(rotation=45)
st.pyplot(plt)
st.write("**Analysis**: The bar chart identifies the top 10 countries with the highest trade quantities. These countries are the most active in terms of total quantity traded.")

# Plot 4: Bar Chart - Top 10 Countries by Trade Value
st.header("Bar Chart: Top 10 Countries by Trade Value")
top_countries_value = df.groupby('Country').agg({'Value': 'sum'}).sort_values(by='Value', ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_countries_value['Value'].plot(kind='bar', color='lightgreen')
plt.title('Top 10 Countries by Trade Value')
plt.xlabel('Country')
plt.ylabel('Total Trade Value')
plt.xticks(rotation=45)
st.pyplot(plt)
st.write("**Analysis**: While quantity and value usually go hand in hand, this chart shows which countries contribute the most to the total trade value.")

# Plot 5: Box Plot - Trade Quantity by Import/Export
st.header("Box Plot: Trade Quantity by Import/Export")
plt.figure(figsize=(8, 6))
sns.boxplot(x='Import_Export', y='Quantity', data=df)
plt.title('Box Plot of Trade Quantity by Import/Export')
plt.xlabel('Import/Export')
plt.ylabel('Quantity')
st.pyplot(plt)
st.write("**Analysis**: This box plot compares the distribution of trade quantities for imports versus exports, highlighting key differences in quantity between the two categories.")

# Plot 6: Pie Chart - Distribution of Trade Value by Product Category
st.header("Pie Chart: Distribution of Trade Value by Product Category")
product_categories = df.groupby('Category').agg({'Value': 'sum'}).sort_values(by='Value', ascending=False)
plt.figure(figsize=(8, 8))
plt.pie(product_categories['Value'], labels=product_categories.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Trade Value by Product Category')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
st.pyplot(plt)
st.write("**Analysis**: The pie chart shows the percentage of trade value contributed by different product categories. Some categories clearly dominate trade value, indicating their significance in the market.")
