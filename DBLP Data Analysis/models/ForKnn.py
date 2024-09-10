import pandas as pd
import numpy as np
import pandas as pd2
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pyodbc
from array import array
from sklearn import preprocessing
from matplotlib import pyplot as plt
county=[]
lab1=[]
cnxn = pyodbc.connect("Driver={ODBC Driver 11 for SQL Server};Server=DESKTOP-V6708T2\SQLSERVER;Database=DBLP;Trusted_Connection=yes;")
dataset = pd.read_sql_query("SELECT TOP (1000) [ID] ,[year],[count] FROM [DBLP].[dbo].[ForFinal]", cnxn)
for index, row in dataset.iterrows():
    if row['count']<=66 and row['count']>=100:
        lab1.append('A')
    elif row['count']>=101 and row['count']<=300:
        lab1.append('B')
    elif row['count']>=301 and row['count']<=500:
        lab1.append('C')
    else:
        lab1.append('D')
#print(dataset)
#pd2 = dataset.groupby('Year').count()
le = preprocessing.LabelEncoder()
#label = le.fit_transform(dataset.groupby('Year').count())
####label=dataset.groupby('Year').count()
###print(label)
label=dataset['count']
print(label.max())
print(label.min())
lab=le.fit_transform(lab1)
id=dataset['ID']
year=dataset['year']
l = preprocessing.LabelEncoder()
y=l.fit_transform(year)
i=l.fit_transform(id)
X = np.array(list(zip(i, y)))


"""from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_encoder = LabelEncoder()
ohe = OneHotEncoder(id)
label_encoded_data = label_encoder.fit_transform(id)
i=ohe.fit_transform(label_encoded_data.reshape(-1,1))
ohe = OneHotEncoder(year)
label_encoded_data = label_encoder.fit_transform(year)
y=ohe.fit_transform(label_encoded_data.reshape(-1,1))"""

#features=zip(i,y)
#print(X)
####print(X.shape)
#X = np.arange(100)
#X = X[:26]
#X = X.reshape(2,50)
#X = X.transpose()
####print(len(X))


##print(label.shape)
##print(len(label))
#label = np.arange(100)
#label = label.reshape(2,50)
##label = label.transpose()
##3print(label.shape)
#print(len(label))
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,lab)
predicted= model.predict([[0,5]]) # 0:Overcast, 2:Mild
print(predicted)
cn = pyodbc.connect("Driver={ODBC Driver 11 for SQL Server};Server=DESKTOP-V6708T2\SQLSERVER;Database=DBLP;Trusted_Connection=yes;")
a = pd.read_sql_query("SELECT TOP (1000) [ID] ,[year],[count] FROM [DBLP].[dbo].[ForFinal] Where year<=2000", cn)
#a=int(dataset[dataset.year <= 2000].groupby('year'))
#a=dataset.query('year<=1952')
print(len(a))
# Split dataset into training set and test set
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, lab, test_size=0.2) # 70% training and 30% test
from sklearn.neighbors import KNeighborsClassifier

#Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=3)

#Train the model using the training sets
knn.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = knn.predict(X_test)
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

#model.fit(dataset.items, dataset.items)

#expected = dataset.target
#predicted = model.predict(dataset.data)

#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))