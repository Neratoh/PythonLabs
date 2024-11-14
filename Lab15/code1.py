import pandas as pd

data = {
    "Country1": {"population": 10, "area": 100},
    "Country2": {"population": 20, "area": 150},
    "Country3": {"population": 30, "area": 200},
    "Country4": {"population": 40, "area": 250},
    "Country5": {"population": 50, "area": 300},
    "Country6": {"population": 60, "area": 350},
    "Country7": {"population": 70, "area": 400},
    "Country8": {"population": 80, "area": 450},
    "Country9": {"population": 90, "area": 500},
    "Country10": {"population": 100, "area": 550}
}

df = pd.DataFrame(data).T

df["density"] = df["population"] / df["area"]

print("DataFrame:")
print(df)
