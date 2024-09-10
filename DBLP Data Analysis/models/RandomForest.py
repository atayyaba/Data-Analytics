import pandas as pd
import numpy as np
import pandas as pd2
from sklearn import metrics, linear_model
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot as plt

import pyodbc
from array import array
from sklearn import preprocessing
#from sklearn import train_test_split
county=[]
lab1=[]
cnxn = pyodbc.connect("Driver={ODBC Driver 11 for SQL Server};Server=DESKTOP-V6708T2\MSSQLSERVER01;Database=DblpXml;Trusted_Connection=yes;")
dataset = pd.read_sql_query("Select * from [DblpXml].[dbo].[Bibfinal]", cnxn)
print(dataset.shape)
features = pd.get_dummies(dataset)

# Labels are the values we want to predict
labels = np.array(features['count'])
# Remove the labels from the features
# axis 1 refers to the columns
features= features.drop('count', axis = 1)

feature_list = list(features.columns)
# Convert to numpy array
features = np.array(features)
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)
print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)
#baseline_preds = test_features[:, feature_list.index('average')]
# Baseline errors, and display average baseline error
#baseline_errors = abs(baseline_preds - test_labels)
#print('Average baseline error: ', round(np.mean(baseline_errors), 2))

from sklearn.ensemble import RandomForestRegressor
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(train_features, train_labels)
# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
#print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')

importances = list(rf.feature_importances_)
# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
# Print out the feature and importances
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances]
# Import matplotlib for plotting and use magic command for Jupyter Notebooks


# Set the style
plt.style.use('fivethirtyeight')
# list of x locations for plotting
x_values = list(range(len(importances)))
# Make a bar chart
plt.bar(x_values, importances, orientation = 'vertical')
# Tick labels for x axis
plt.xticks(x_values, feature_list, rotation='vertical')
# Axis labels and title
plt.ylabel('Predicted'); plt.xlabel('Variable'); plt.title('Co-authors Biblography Prediction')
plt.show()
