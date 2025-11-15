import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load Data
df = pd.read_csv('../data/forts.csv')

# Step 2: Data Cleaning / Processing
# Ensure numeric columns are numeric
df['Height (m)'] = pd.to_numeric(df['Height (m)'], errors='coerce')
df['Visitors per Year'] = pd.to_numeric(df['Visitors per Year'], errors='coerce')
df['Year Built'] = pd.to_numeric(df['Year Built'], errors='coerce')

# Step 3: Add Age of Fort
current_year = 2025
df['Age (years)'] = current_year - df['Year Built']

# Step 4: Basic Analysis using NumPy
print("Oldest Fort:", df.loc[df['Age (years)'].idxmax()]['Fort Name'])
print("Tallest Fort:", df.loc[df['Height (m)'].idxmax()]['Fort Name'])
print("Average Visitors per Fort:", np.mean(df['Visitors per Year']))

# Step 5: Visualizations

# 5a: Bar chart of Fort Heights
plt.figure(figsize=(10,6))
plt.bar(df['Fort Name'], df['Height (m)'], color='skyblue')
plt.xlabel('Fort Name')
plt.ylabel('Height (m)')
plt.title('Heights of Famous Forts')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5b: Timeline of Forts Built
plt.figure(figsize=(10,6))
plt.scatter(df['Year Built'], df['Fort Name'], color='green', s=100)
for i, txt in enumerate(df['Fort Name']):
    plt.annotate(txt, (df['Year Built'][i], df['Fort Name'][i]))
plt.xlabel('Year Built')
plt.ylabel('Fort Name')
plt.title('Timeline of Forts')
plt.tight_layout()
plt.show()

# 5c: Scatter Plot of Fort Locations (Map-like)
plt.figure(figsize=(10,6))
plt.scatter(df['Longitude'], df['Latitude'], s=df['Visitors per Year']/1000, c='red', alpha=0.6)
for i, txt in enumerate(df['Fort Name']):
    plt.annotate(txt, (df['Longitude'][i]+0.02, df['Latitude'][i]+0.02))
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Fort Locations and Popularity (Size ~ Visitors)')
plt.tight_layout()
plt.show()

# 5d: Pie Chart of Forts per Region
region_counts = df['Region'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Forts by Region')
plt.show()
