import pandas as pd
print("DATA FRAME:")
data = {
    "Name":["sahil","ali","kamran",None,"danyal","jamshed","hamza","kashif",None,"gulzar","hasan"],
    "age":[34,54,23,54,None,54,56,45,34,None,45],
    "gpa":[3,None,4,2.7,3.2,1,2,3,4,3,2],
    "department":["ai","cs","ai","cs","english","medical","english","medical","ai","medical","cs"]
}
df = pd.DataFrame(data)

result1 = df.groupby("department")["gpa"].mean()  #AVERAGE GPA OF EACH DEPARTMENT
print(result1[result1>2])
# result2 = df.groupby("department")["gpa"].sum()  #total GPA OF EACH DEPARTMENT
# result3 = df.groupby("department")["Name"].count()    #TOTAL STUDENT OF EACH DEPARTMENT
# result4 = df.groupby("department")["gpa"].max()  #maximum gpa OF EACH DEPARTMENT
# result5 = df.groupby("department")["gpa"].agg(["mean","min","max"])   #MULTIPLE AGGREGATION FUNCTIONS
# print(result4)
# result4.sort_values(ascending=False)
# print(result4)

