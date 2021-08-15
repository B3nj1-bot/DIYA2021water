import pandas as pd
import os
import sys
from abbrev_state import states
def clean_county(x):
    print(x)
    if 'County' in x:
        return x.strip()[:-7]
    else:
        return None
directory = 'six_year_compiled'

bladder_incidence = pd.read_csv("bladder_cancer.csv")
bladder_incidence = bladder_incidence[["Incidence"]]
bladder_incidence['county'] = bladder_incidence.index
bladder_incidence = bladder_incidence.reset_index()[["county","Incidence"]].iloc[1:]
bladder_incidence["Incidence"] = pd.to_numeric(bladder_incidence["Incidence"])
bladder_incidence = bladder_incidence.rename(columns={"Incidence":f"bladder cancer rate (per 100K)"})

cancer_incidence = pd.read_csv("cancer.csv")
cancer_incidence = cancer_incidence[["Incidence"]]
cancer_incidence['county'] = cancer_incidence.index
cancer_incidence = cancer_incidence.reset_index()[["county","Incidence"]].iloc[1:]
cancer_incidence["Incidence"] = pd.to_numeric(cancer_incidence["Incidence"])
cancer_incidence = cancer_incidence.rename(columns={"Incidence":f"cancer rate (per 100K)"})

poverty_percent = pd.read_csv("PovertyEstimates.csv")
poverty_percent = poverty_percent[["Stabr","Area_name","PCTPOVALL_2019"]].iloc[1:]
poverty_percent["Stabr"] = poverty_percent["Stabr"].apply(lambda x: states.get(x))
poverty_percent["Area_name"] = poverty_percent["Area_name"].apply(clean_county)
poverty_percent.dropna(inplace=True)
poverty_percent['county'] = poverty_percent['Area_name'] + ', ' + poverty_percent['Stabr']
poverty_percent = poverty_percent[["county","PCTPOVALL_2019"]].reset_index(drop=True)
final = pd.merge(bladder_incidence,cancer_incidence,how='outer',on='county')
final = pd.merge(final,poverty_percent,how='outer',on='county')
for filename in os.listdir(directory):
    if not filename.startswith('.'):
        print(filename)
        adding = pd.read_csv(os.path.join(directory,filename),index_col=[0])
        final = pd.merge(final,adding,how='outer',on='county')
final.to_csv('six_year_data.csv',index=False)
