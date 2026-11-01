import pandas as pd
print("DATA FRAME:")
data = {
    "Name":["sahil","ali","kamran",None,"danyal","jamshed","hamza","kashif",None,"gulzar","hasan"],
    "age":[34,54,23,54,None,54,56,45,34,None,45],
    "gpa":[3,None,4,2.7,3.2,1,2,3,4,3,2]
}
df = pd.DataFrame(data)
print(df.dtypes)  #CHECK DATA TYPES

# print(df.isna())   #IF DATASET HAS MISSING AVLUES OR NOT RETURN TRUE FALSE
# print(df.isnull())   #same like isna() 
# print(df.isnull().sum())   #RETURN TOTAL OF MISSING VALUES     
# print(df.isnull().sum(axis=1))   #RETURN TOTAL OF MISSING VALUES for each ROW 
# print(df.dropna())   #REMOVING ROWS THAT CONTAINS MISSING VALUES
# print(df.dropna(subset=["gpa"]))   #REMOVING ROWS only that missing only gpa

# df["age"] = df["age"].fillna(21)   #FILINF WITH 21 OF AFE COLUMN MISSING VALUE


# mean_age = df["age"].mean()
# df["age"] = df['age'].fillna(mean_age)    #FILLING WITH AVERAGE NUMBER OF AFE COLUMN MISSING VALUES

# median_age = df["age"].median()

# df["age"] = df['age'].fillna(median_age)    #FILLING WITH median NUMBER OF AFE COLUMN MISSING VALUES

# print(df.duplicated())   #check duplicates
# print(df.drop_duplicates())   #REMOVE DUPLICATES

# df["Name"]=  df["Name"].replace("sahil","salar")  #REPLACE NAME OF NAMES COLUMN


