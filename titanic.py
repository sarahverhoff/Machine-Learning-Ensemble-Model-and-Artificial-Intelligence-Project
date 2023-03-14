#!/usr/bin/env python
#titanic problem for predicting if a passenger has survived or died(binary classification)
import numpy as np #linear algebra
import pandas as pd # data processing as data = pd.read_csv("/content/salaries_POINTCLICK_upload.csv")
#for dirname, _, filenames in os.walk('/Documents/Liotta_lab_rotation/titanic_practice_probleme'):
    #for filename in filenames:
        #print(os.path.join(dirname, filename))
# Any results you write to the current directory are saved as output.
 #installing packages: py -3 -m  pip install numpy
train_data = pd.read_csv("train.csv")
train_data.head()


test_data = pd.read_csv("test.csv")
test_data.head()
#output the beginning data of the test data set
women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived:", rate_women) 
# % of women who survived: 0.7420382165605095

men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)

print("% of men who survived:", rate_men)
#% of men who survived: 0.18890814558058924
 #First machine learning model: Random Forest Classifier
 
from sklearn.ensemble import RandomForestClassifier

y = train_data["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")
#Your submission was successfully saved!
