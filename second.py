import pandas as pd
print("DATA FRAME:")
data = {
    "Name":["sahil","ali","kamran","ahmad","danyal","jamshed","hamza","kashif","misbah,","gulzar","hasan"],
    "age":[34,54,23,54,34,54,56,45,34,65,45],
    "gpa":[3,4.5,4,2.7,3.2,1,2,3,4,3,2]
}
df = pd.DataFrame(data)  #COVERTINF DATA INTO PANDAS DATAFRAME
print(df.head())         #PRINT FIRST 5 ROWS
print(df.head(3))        #PRINT FIRST 3 ROWS
print(df.tail(3))        #PRINT LAST 3 ROWS
print(df.tail())         #LAST 5 ROWS
print(df.shape)          #SHAPE OF DATA FRAME
print(df.columns)        #COLUMNS NAMES
print(df.columns.tolist()) #COLUMNS NAMES INTO A LIST

print(df.info())          #COMPLETE INFORMATION OF DATASET
print(df.describe())       #COMPLETE NUMERICAL ?STATISTICAL INFO OF DATASETS



