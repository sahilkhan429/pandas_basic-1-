import pandas as pd
print("DATA FRAME:")
data = {
    "Name":["sahil","ali","kamran","ahmad","danyal","jamshed","hamza","kashif","misbah,","gulzar","hasan"],
    "age":[34,54,23,54,34,54,56,45,34,65,45],
    "gpa":[3,4.5,4,2.7,3.2,1,2,3,4,3,2]
}
df = pd.DataFrame(data)
print(df[df["age"]>40])    #IT IS BOOLEAN FILTERING PRINTING the rows WHOSE AGE IS > 40
print(df[df["gpa"]>2])     #SELECTING ROWS WHOSE GPA IS > 2 USING BOOLEAN FILTERING

print(df[(df["age"]>40)&(df["gpa"]>2)])   #MULTIPLE CONDITIONS OF BOOLEAN FILTERING EACH CONDITION WILL BE INSIDE THIS BRACKET

print(df[df["Name"].isin(["sahil","kamran","ali"])])  #THIS RETURN WHETHER VALUES BELONG TO A LIST OR NOT IT IS BETTER THAM USING MULTIPLE CONDITIONS AT A TIME
print(df[df["age"].between(20,50)])    #FILTERING ROWS WHOSE AGE IS BETWEEN 20 AND 50
print(df.query("age>40"))  #THIS METHOD PROVIDE LIKE ENGLISH QUERY WE CAN ENTER AS ENGLISH QUERY
print(df.query("age>40 and gpa >3")) #MULTIPLE CONDITIONS USING QUERY METHOD


