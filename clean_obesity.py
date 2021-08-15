import pandas as pd

df = pd.read_csv("obesity.csv")
df['county'] = df['County'] + ', ' + df['State']
df['obesity'] = df['Male obesity  prevalence, 2011* (%)']/2 + df['Female obesity prevalence, 2011* (%)']/2
df = df[['county','obesity']].dropna()
df.to_csv("obesity_cleaned.csv",index=False)
print(df.columns)
print(df.head())
