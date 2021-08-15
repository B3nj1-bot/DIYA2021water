import pandas as pd
df_list = []
def remove_county(x):
    try:
        if 'County' in x:
            return x[:-7]
        else:
            return None
    except:
        print(x)
for filename in ['any_alcohol','binge_alcohol','heavy_alcohol']:
    print(filename)
    df = pd.read_csv(filename+'.csv').dropna()
    df['Location'] = df['Location'].apply(remove_county)
    df = df.dropna()
    df['county'] = df['Location'] + ', ' + df['State']
    df[filename] = df['2012 Both Sexes'] + df['2011 Both Sexes'] + df['2010 Both Sexes'] + df['2009 Both Sexes'] + df['2008 Both Sexes'] + df['2007 Both Sexes'] + df['2006 Both Sexes']
    df[filename] = df[filename] / 7
    df = df[['county',filename]].dropna()
    df.to_csv(f"{filename}_cleaned.csv",index=False)
    df_list.append(df)
    print(df.columns)
    print(df.head())
df = pd.merge(df_list[0],df_list[1],how='outer',on='county')
df = pd.merge(df,df_list[2],how='outer',on='county')
df.to_csv(f"all_alcohol_cleaned.csv",index=False)
