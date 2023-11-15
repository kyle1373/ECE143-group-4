import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path_csv = '../data/data.csv'
data = pd.read_csv(file_path_csv)

data.head()

# Devices Used
plt.figure(figsize=(10, 6))
sns.countplot(x='DEVICE_TYPE_W63', data=data)
plt.title('Distribution of Devices Used')
plt.ylabel('Count')
plt.xlabel('Type of Device')
plt.xticks(ticks=[0, 1, 2], labels=['Desktop', 'Mobile Phone', 'Tablet'])
plt.show()

# Age Category
plt.figure(figsize=(10, 6))
sns.countplot(x='F_AGECAT', data=data)
plt.title('Distribution by Age')
plt.ylabel('Count')
plt.xlabel('Age Category')
plt.show()

# Education Level
plt.figure(figsize=(10, 6))
sns.countplot(x='F_EDUCCAT', data=data)
plt.title('Distribution by Level of Education')
plt.ylabel('Count')
plt.xlabel('Level of Education')
plt.show()

# Correlation Matrix
subset_columns = [
    'DEVICE_TYPE_W63',
    'LANG_W63_W63',
    'SNSUSE_W63',
    'VIDEOGAME_W63',
    'F_AGECAT',
    'F_EDUCCAT',
    'F_INCOME',
    'SMARTPHONE_W63',
    'F_SEX'
]

correlation_data = data[subset_columns]
correlation_matrix = correlation_data.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()