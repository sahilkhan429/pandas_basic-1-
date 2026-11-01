from pathlib import Path
import pandas as pd
import json

path = Path("data/csv")
if path.exists():
    print("found")
else:                   #LOOKING IF FILE EXISTS OR NOT
    print("not")

#loading csv file using relative path
df = pd.read_csv("data/csv")
#loading csv file using absolute path
df = pd.read_csv("user/desktop/si_project/data/csv")

#LOADING JSON WITH PANDAS
df = pd.read_json("data/student.json")

#LOADING JSON WITH PYTHON

with open("data/studenys.json") as file:
    data = json.load(file)
print(data)

