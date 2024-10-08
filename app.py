{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b486b1f-65c0-4ce8-97f9-3a4c26ea660b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Load the CSV file\n",
    "file_path = r'C:\\Users\\Dell\\Downloads\\Imports_Exports_Dataset.csv'\n",
    "df = pd.read_csv(file_path) \n",
    "# Title of the Streamlit App\n",
    "st.title(\"Trade Data Visualization Dashboard\")\n",
    "\n",
    "# 1. Scatter Plot: Quantity vs. Value\n",
    "st.header(\"Scatter Plot: Quantity vs. Value\")\n",
    "plt.figure(figsize=(8, 6))\n",
    "plt.scatter(df['Quantity'], df['Value'], color='blue', alpha=0.5)\n",
    "plt.title('Scatter Plot of Quantity vs. Value')\n",
    "plt.xlabel('Quantity')\n",
    "plt.ylabel('Value')\n",
    "plt.grid(True)\n",
    "st.pyplot(plt)\n",
    "\n",
    "# 2. Line Plot: Quantity Over Time (Date vs Quantity)\n",
    "st.header(\"Line Plot: Quantity Over Time\")\n",
    "st.subheader(\"Ensure that your dataset has a 'Date' column\")\n",
    "\n",
    "# Check if 'Date' is in the dataset and adjust if needed\n",
    "if 'Date' not in df.columns and 'Date' in df.index.names:\n",
    "    df.reset_index(inplace=True)\n",
    "    st.write(\"'Date' was in the index. Resetting the index.\")\n",
    "\n",
    "# Rename any column that might be named like 'Date'\n",
    "if 'Date' not in df.columns:\n",
    "    for col in df.columns:\n",
    "        if 'date' in col.lower():\n",
    "            df.rename(columns={col: 'Date'}, inplace=True)\n",
    "            st.write(f\"Renaming column '{col}' to 'Date'.\")\n",
    "\n",
    "# Plot only if 'Date' column is found\n",
    "if 'Date' in df.columns:\n",
    "    plt.figure(figsize=(10, 6))\n",
    "    plt.plot(df['Date'], df['Quantity'], color='green', linestyle='-', marker='o')\n",
    "    plt.title('Line Plot of Quantity Over Time')\n",
    "    plt.xlabel('Date')\n",
    "    plt.ylabel('Quantity')\n",
    "    plt.xticks(rotation=45)\n",
    "    plt.grid(True)\n",
    "    st.pyplot(plt)\n",
    "else:\n",
    "    st.write(\"The 'Date' column still does not exist. Please check your dataset.\")\n",
    "\n",
    "# 3. Bar Chart: Top 10 Countries by Trade Quantity and Value\n",
    "st.header(\"Bar Charts: Top 10 Countries by Trade Quantity and Value\")\n",
    "\n",
    "top_countries = df.groupby('Country').agg({\n",
    "    'Quantity': 'sum',\n",
    "    'Value': 'sum'\n",
    "}).sort_values(by='Value', ascending=False).head(10)\n",
    "\n",
    "# Bar Chart for Quantity\n",
    "st.subheader(\"Top 10 Countries by Trade Quantity\")\n",
    "plt.figure(figsize=(10, 6))\n",
    "top_countries['Quantity'].plot(kind='bar', color='skyblue')\n",
    "plt.title('Top 10 Countries by Trade Quantity')\n",
    "plt.xlabel('Country')\n",
    "plt.ylabel('Total Trade Quantity')\n",
    "plt.xticks(rotation=45)\n",
    "st.pyplot(plt)\n",
    "\n",
    "# Bar Chart for Value\n",
    "st.subheader(\"Top 10 Countries by Trade Value\")\n",
    "plt.figure(figsize=(10, 6))\n",
    "top_countries['Value'].plot(kind='bar', color='lightgreen')\n",
    "plt.title('Top 10 Countries by Trade Value')\n",
    "plt.xlabel('Country')\n",
    "plt.ylabel('Total Trade Value')\n",
    "plt.xticks(rotation=45)\n",
    "st.pyplot(plt)\n",
    "\n",
    "# 4. Scatter Plot: Trade Value vs. Quantity by Shipping Method\n",
    "st.header(\"Scatter Plot: Trade Value vs. Quantity by Shipping Method\")\n",
    "plt.figure(figsize=(10, 6))\n",
    "\n",
    "# Subset data by Shipping Method\n",
    "shipping_methods = df['Shipping_Method'].unique()\n",
    "\n",
    "for method in shipping_methods:\n",
    "    subset = df[df['Shipping_Method'] == method]\n",
    "    plt.scatter(subset['Quantity'], subset['Value'], label=method, alpha=0.6)\n",
    "\n",
    "plt.title('Trade Value vs. Quantity by Shipping Method')\n",
    "plt.xlabel('Trade Quantity')\n",
    "plt.ylabel('Trade Value')\n",
    "plt.legend(title=\"Shipping Method\")\n",
    "st.pyplot(plt)\n",
    "\n",
    "# 5. Box Plot: Quantity by Import/Export\n",
    "st.header(\"Box Plot: Quantity by Import/Export\")\n",
    "plt.figure(figsize=(8, 6))\n",
    "sns.boxplot(x='Import_Export', y='Quantity', data=df)\n",
    "plt.title('Box-Whisker Plot of Quantity by Import/Export')\n",
    "plt.xlabel('Import/Export')\n",
    "plt.ylabel('Quantity')\n",
    "st.pyplot(plt)\n",
    "\n",
    "# 6. Pie Chart: Distribution of Trade Value by Product Category\n",
    "st.header(\"Pie Chart: Distribution of Trade Value by Product Category\")\n",
    "product_categories = df.groupby('Category').agg({\n",
    "    'Value': 'sum'\n",
    "}).sort_values(by='Value', ascending=False)\n",
    "\n",
    "plt.figure(figsize=(8, 8))\n",
    "plt.pie(product_categories['Value'], labels=product_categories.index, autopct='%1.1f%%', startangle=140)\n",
    "plt.title('Distribution of Trade Value by Product Category')\n",
    "plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.\n",
    "st.pyplot(plt)\n",
    "\n",
    "# 7. Histogram: Distribution of Trade Value\n",
    "st.header(\"Histogram: Distribution of Trade Value\")\n",
    "plt.figure(figsize=(8, 6))\n",
    "sns.histplot(data=df, x='Value', bins=30, kde=True)\n",
    "plt.title('Distribution of Trade Value')\n",
    "st.pyplot(plt)\n",
    "\n",
    "# 8. Pie Chart: Proportion of Import vs. Export\n",
    "st.header(\"Pie Chart: Proportion of Import vs. Export\")\n",
    "import_export_counts = df['Import_Export'].value_counts()\n",
    "plt.figure(figsize=(7, 7))\n",
    "plt.pie(import_export_counts, labels=import_export_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen'])\n",
    "plt.title('Proportion of Import vs Export')\n",
    "st.pyplot(plt)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
