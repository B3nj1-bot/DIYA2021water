import pandas as pd

df = pd.read_csv("physical_activity.csv")
df['county'] = df['County'] + ', ' + df['State']
df['physical_activity'] = df['Male sufficient physical activity  prevalence, 2011* (%)']/2 + df['Female sufficient physical activity  prevalence, 2011* (%)']/2
df = df[['county','physical_activity']].dropna()
df.to_csv("physical_activity_cleaned.csv",index=False)
print(df.columns)
print(df.head())
