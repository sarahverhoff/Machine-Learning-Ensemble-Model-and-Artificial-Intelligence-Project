#titanic problem for predicting if a passenger has survived or died(binary classification)
import numpy as np #linear algebra
import pandas as pd # data processing as data = pd.read_csv("/content/salaries_POINTCLICK_upload.csv")
#for dirname, _, filenames in os.walk('/Documents/Liotta_lab_rotation/titanic_practice_probleme'):
    #for filename in filenames:
        #print(os.path.join(dirname, filename))
# Any results you write to the current directory are saved as output.

train_data = pd.read_csv("/Documents/Liotta_lab_rotation/titanic_practice_problem/train.csv")
df = train_data.head()
print(df)

test_data = pd.read_csv("/Documents/Liotta_lab_rotation/titanic_practice_problem//test.csv")
test_data.head()
#output the beginning data of the test data set
women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived:", rate_women) # % of women who survived: 0.7420382165605095