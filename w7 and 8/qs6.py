import pandas as pd


try:
    df = pd.read_csv('weight_height.csv')
    print("Original Data:")
    print(df.head())
except FileNotFoundError:
    print("Error: File 'weight_height.csv' not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()


df['BMI'] = df['Weight'] / (df['Height']/100)**2 


def get_risk(bmi):
    if bmi < 18.5:
        return 'Nutrient deficient'
    elif 18.5 <= bmi < 25:
        return 'Lower risk'
    elif 25 <= bmi < 30:
        return 'Heart disease risk'
    elif 30 <= bmi < 40:
        return 'Higher risk of diabetes, heart disease'
    else:
        return 'Serious health condition risk'

df['Risk'] = df['BMI'].apply(get_risk)


print("\nData with BMI and Risk columns:")
print(df.head())


try:
    df.to_csv('weight_height_with_bmi.csv', index=False)
    print("\nUpdated data saved to 'weight_height_with_bmi.csv'")
except Exception as e:
    print(f"Error saving file: {e}")