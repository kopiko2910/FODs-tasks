import pandas as pd
import matplotlib.pyplot as plt


try:
    df = pd.read_csv('weight_height.csv')
    print("Data loaded successfully:")
    print(df.head())
except FileNotFoundError:
    print("Error: File 'weight_height.csv' not found. Please ensure the file exists.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    exit()


plt.figure(figsize=(15, 10))


plt.subplot(2, 3, 1)
plt.scatter(df['Height'], df['Weight'], alpha=0.5)
plt.title('Weight vs Height')
plt.xlabel('Height')
plt.ylabel('Weight')


plt.subplot(2, 3, 2)
plt.scatter(df['Age'], df['Weight'], alpha=0.5)
plt.title('Age vs Weight')
plt.xlabel('Age')
plt.ylabel('Weight')

plt.subplot(2, 3, 3)
plt.scatter(df['Age'], df['Height'], alpha=0.5)
plt.title('Height vs Age')
plt.xlabel('Age')
plt.ylabel('Height')

plt.subplot(2, 3, 4)
for gender in df['Gender'].unique():
    subset = df[df['Gender'] == gender]
    plt.scatter(subset['Gender'], subset['Height'], alpha=0.5, label=gender)
plt.title('Gender vs Height')
plt.xlabel('Gender')
plt.ylabel('Height')
plt.legend()


plt.subplot(2, 3, 5)
for gender in df['Gender'].unique():
    subset = df[df['Gender'] == gender]
    plt.scatter(subset['Gender'], subset['Weight'], alpha=0.5, label=gender)
plt.title('Gender vs Weight')
plt.xlabel('Gender')
plt.ylabel('Weight')
plt.legend()


plt.tight_layout()
plt.show()