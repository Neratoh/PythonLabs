import pandas as pd

df = pd.read_csv('data.csv')

print("Перші кілька рядків даних:")
print(df.head())

if 'date' not in df.columns:
    print("Стовпець 'date' відсутній у даних.")
else:

    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month

    monthly_usage = df.groupby('month').size()

    most_popular_month = monthly_usage.idxmax()
    most_popular_count = monthly_usage.max()

    print("\nМісяць з найбільшою популярністю серед велосипедистів:")
    print(f"Місяць: {most_popular_month}, Кількість поїздок: {most_popular_count}")

    
