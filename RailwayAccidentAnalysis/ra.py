# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read and preprocess data
file_path = '/content/Highway-Rail_Grade_Crossing_Accident_Data.csv'
df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Hour'] = df['Hour'].fillna(0).astype(int)
df['AM/PM'] = df['AM/PM'].fillna('AM')
df['Time of Day'] = df.apply(lambda row: row['Hour'] if row['AM/PM'] == 'AM' else (row['Hour'] + 12) % 24, axis=1)

# Plot 1: Accident Count by Weather Condition
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Weather Condition', palette='coolwarm', order=df['Weather Condition'].value_counts().index)
plt.title('Accident Count by Weather Condition')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Accident Count by Track Type
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Track Type', palette='viridis', order=df['Track Type'].value_counts().index)
plt.title('Accident Count by Track Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 3: Accident Count by Time of Day
plt.figure(figsize=(10, 6))
sns.histplot(df['Time of Day'], bins=24, kde=True, color='blue')
plt.title('Accident Count by Time of Day')
plt.xlabel('Hour of the Day')
plt.tight_layout()
plt.show()

# Plot 4: Accident Count by State
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='State Name', palette='plasma', order=df['State Name'].value_counts().index)
plt.title('Accident Count by State')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Plot 5: Top 15 Counties by Accident Count
plt.figure(figsize=(12, 6))
top_counties = df['County Name'].value_counts().nlargest(15).index
sns.countplot(data=df[df['County Name'].isin(top_counties)], x='County Name', palette='magma', order=top_counties)
plt.title('Top 15 Counties by Accident Count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
