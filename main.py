
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Global Terrorism Index 2023.csv')


print(df.info())

df.dropna(inplace=True)

summary_stats = df.describe()
print(summary_stats)


df['year'] = df['Year']
df['Incidents'] = df.groupby('year')['Incidents'].size()

# Plotting a time series of terrorist incidents
plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y=df.groupby('year')['Incidents'].sum(), data=df, marker='o')
plt.title('Terrorism Incidents Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Incidents')
plt.show()




correlation_matrix = df[['Score', 'Rank', 'Incidents']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()


