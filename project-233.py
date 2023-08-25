import pandas as pd
data=pd.read_csv('projectc233_studentData.csv')
data['Total_marks_obtained']=df.iloc[:,[2,3,4]].sum(axis=1)
data.loc[data['Total_marks_obtained']>250,'grade']='very good student'
data.loc[data['Total_marks_obtained']<250,'grade']='needs to work hard'
data['Percentage']=(data['Total_marks_obtained']/data['Overall_Total'])*100
print(data)