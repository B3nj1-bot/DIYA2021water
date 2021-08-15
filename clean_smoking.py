import pandas as pd

def remove_county(x):
    try:
        if 'county' in x.lower():
            return x[:-7]
        else:
            return x
    except:
        print(x)

df = pd.read_csv("smoking.csv")
df = df[df['sex'] == "Both"]
df = df.dropna(subset=['county'])
df['county'] = df['county'].apply(remove_county)
df['county'] = df['county'] + ', ' + df['state']
df['smoking'] = df['total_mean']
df = df[['county','smoking']]
df = df.groupby('county').mean()
df = df.reset_index()
df.to_csv("smoking_cleaned.csv",index=False)
print(df.head())
