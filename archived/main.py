import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score
from sklearn.tree import export_graphviz
from sklearn.metrics import accuracy_score


filepath = "C:/Users/prana/Downloads/six_year_data.csv"
data = pd.read_csv(filepath)

new_data = data.loc[:,['asbestos','TTHM','chloroform','chlorite',
                       'combinded_radium','uranium_combined','arsenic',
                       'chlorine','nitrate','cancer rate (per 100K)']]
new_data = new_data.dropna(subset = ['cancer rate (per 100K)'])

y = new_data['cancer rate (per 100K)']
X = new_data.loc[:,['asbestos','TTHM','chloroform','chlorite',
            'combinded_radium','uranium_combined','arsenic',
            'chlorine','nitrate']]



model_X, test_X, model_y, test_y = train_test_split(X, y, random_state = 0, test_size=.1)
train_X, val_X, train_y, val_y = train_test_split(model_X, model_y, random_state = 0, test_size=.22)

my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(train_X))
imputed_X_valid = pd.DataFrame(my_imputer.transform(val_X))
imputed_X_test = pd.DataFrame(my_imputer.transform(test_X))


# Imputation removed column names; put them back
imputed_X_train.columns = train_X.columns
imputed_X_valid.columns = val_X.columns
imputed_X_test.columns = test_X.columns


train_X = imputed_X_train
val_X = imputed_X_valid
test_X = imputed_X_test


model = DecisionTreeRegressor()
model.fit(train_X, train_y)
val_predictions = model.predict(test_X)




