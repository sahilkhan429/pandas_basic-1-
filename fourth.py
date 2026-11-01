import pandas as pd
print("DATA FRAME:")
data = {
    "Name":["sahil","ali","kamran","ahmad","danyal","jamshed","hamza","kashif","misbah,","gulzar","hasan"],
    "age":[34,54,23,54,34,54,56,45,34,65,45],
    "gpa":[3,4.5,4,2.7,3.2,1,2,3,4,3,2]
}
df = pd.DataFrame(data)
print(df)
print(df["age"])   #SELECTING AGE COLUMN FROM DATASET IT RETURNS A SERIES
print(df[["Name","age"]])    #SELECTING MULTIPLE COLUMNS IT RETURNS A DATAFRAME
print(df.loc[2])            #SELECTING ROW NUMBER @ USING LOC METHOD
print(df.loc[2:5])          #SLICING 2 TO 5 F WILL BE INCLUDED
print(df.loc[[1,3,5]])       #SELECTING SEPECIFIC ROWS
print(df.loc[2:5,["Name","age"]])   #ROWS AND COLUMNS

print(df.iloc[0])  #SELECTING FIRST ROW USING ILOC METHOD
print(df.iloc[0:5])  #SELECTING FIRST to 5 ROWs USING ILOC METHOD last row excluded


print(df.iloc[0:5,1:4])    #SLICING ROWS AND COLUMNS REMEMEBER ENDING POINT WILL BE EXCULDED


