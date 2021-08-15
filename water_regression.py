
import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
import graphviz
from sklearn import tree
from sklearn.metrics import r2_score

six_year = pd.read_csv("six_year_all_cancers_obesity_alcohol_smoking.csv")

type_cancer = 'liver cancer rate (per 100K)'#'PCTPOVALL_2019'
feature_dict = {
    'kidney cancer rate (per 100K)': ['chlorite','fluoride', 'total_organic_carbon', 'dichloroacetic_acid', 'TTHM', 'monochloroacetic_acid','obesity','physical_activity','smoking'],
    'liver cancer rate (per 100K)':  ['heptachlor','dibromoacetic_acid','nitrate','monobromoacetic_acid','alpha_particles','dinoseb','uranium_combined','chromium','di(2-ethylhexyl)_phthalate','cyanide','physical_activity'],
    'bladder cancer rate (per 100K)': ['chlorite','trichloroacetic_acid','pH','dichloroacetic_acid','chloroform','arsenic','2,3,7,8-TCDD (dioxin)','HAA5','heavy_alcohol'],
    'stomach cancer rate (per 100K)': ['heptachlor','nitrate','monobromoacetic_acid','pentachlorophenol','di(2-ethylhexyl)_phthalate','chlorite','obesity','physical_activity'],
    'cancer rate (per 100K)' : ['chlorite','2,3,7,8-TCDD (dioxin)','HAA5','heptachlor','trichloroacetic_acid','chlorine'],
    'PCTPOVALL_2019': ['chlorite','monobromoacetic_acid','monochloroacetic_acid','HAA5','dichloroacetic_acid','TTHM','trichloroacetic_acid'],
    'lung cancer rate (per 100K)' : ['smoking','obesity','PCTPOVALL_2019','HAA5','TTHM']
}
nonwater_feature_dict = {
    'kidney cancer rate (per 100K)': ['physical_activity','smoking'],
    'liver cancer rate (per 100K)':  ['physical_activity'],
    'bladder cancer rate (per 100K)': ['heavy_alcohol'],
    'stomach cancer rate (per 100K)': ['obesity','physical_activity'],
    'cancer rate (per 100K)' : ['obesity','physical_activity','smoking','PCTPOVALL_2019'],
    'lung cancer rate (per 100K)' : ['smoking','obesity','PCTPOVALL_2019']
}
to_use_dict = feature_dict


dt = six_year.iloc[: , 2:]
results = []
predicting = type_cancer
for i in dt:
  if i == predicting:
    continue
  bi_table = six_year[[predicting, i]]
  bi_table = bi_table.dropna()
  #sns.lmplot(x = 'cancer rate (per 100K)', y = i, data = poop)
  if math.isnan(bi_table[predicting].corr(bi_table[i])):
    continue
  else:
    results.append((bi_table[predicting].corr(bi_table[i]), i))
results.sort(key = lambda x: x[0], reverse=True)
for f in [x for x in results if abs(x[0]) > 0.1]:
  print(f)

r2_scores = []
rmse_scores = []
mae_scores = []
for rand_state in range(0,100):
    x_vars = to_use_dict.get(type_cancer)
    y_var = [type_cancer]

    df = six_year[x_vars + y_var]
    df = df.dropna(subset = [type_cancer])
    #df = df[(df[type_cancer] < df[type_cancer].quantile(0.95)) & (df[type_cancer] > df[type_cancer].quantile(0.05))]
    df = df.fillna(0)
    print(df[type_cancer].describe())
    for col in df:
      print(col, len(df[col].dropna()))

    X = df[x_vars]
    #split
    X_train, X_test, y_train, y_test = train_test_split(X, df[y_var[0]], test_size=0.30, random_state=rand_state)
    #train
    regressor = DecisionTreeRegressor(random_state=rand_state,max_depth=6)
    regressor.fit(X_train, y_train)
    #predict
    y_pred = regressor.predict(X_test)
    y_naive = [df[y_var[0]].mean()] * len(y_test)
    #evaluate
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mse_naive = mean_squared_error(y_test, y_naive)
    rmse_naive = np.sqrt(mse_naive)
    print('mean squared error:',mse)
    print('root mean squared error:',rmse)
    print('naive mean squared error:',mse_naive)
    print('naive root mean squared error:',rmse_naive)
    print('R2 score:',r2_score(y_test,y_pred))
    print('mean absolute error:',mean_absolute_error(y_test,y_pred))
    r2_scores.append(r2_score(y_test,y_pred))
    rmse_scores.append(rmse)
    mae_scores.append(mean_absolute_error(y_test,y_pred))
plt.boxplot(r2_scores)
plt.show()
plt.boxplot(rmse_scores)
plt.show()
plt.boxplot(mae_scores)
plt.show()
