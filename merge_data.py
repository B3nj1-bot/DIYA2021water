#merges data into one set with county as index. code has not been updated to include later additions to the data like lifestyle data and other types of cancer, but the approach is identical.
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


final = pd.merge(bladder_incidence,cancer_incidence,how='outer',on='county')

for filename in os.listdir(directory):
    if not filename.startswith('.'):
        print(filename)
        adding = pd.read_csv(os.path.join(directory,filename),index_col=[0])
        final = pd.merge(final,adding,how='outer',on='county')
final.to_csv('six_year_data.csv',index=False)
