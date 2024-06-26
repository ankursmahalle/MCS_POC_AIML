import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression(solver='lbfgs', max_iter=10000000)
import pickle
import joblib

logreg=LogisticRegression()

data=pd.read_csv("C:\\Users\\MCS\\Downloads\\cancer.csv")
data.drop(["Unnamed: 32"],axis="columns",inplace=True)
data.drop(["id"],axis="columns",inplace=True)
a=pd.get_dummies(data["diagnosis"])
cancer=pd.concat([data,a],axis="columns")
cancer.drop(["diagnosis","B"],axis="columns",inplace=True)
cancer.rename(columns={"M":"Malignant/Benign"},inplace=True)
y=cancer[["Malignant/Benign"]]
X=cancer.drop(["Malignant/Benign"],axis="columns")
print(X.shape[1])

X=np.array(X)
y=np.array(y)

logreg.fit(X,y.reshape(-1,))

joblib.dump(logreg,"model")

