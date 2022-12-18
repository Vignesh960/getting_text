


import pandas as pd
import numpy as np





df = pd.read_csv("first.csv")
df





df.drop(["Unnamed: 0.1"], axis = 1, inplace = True)
df.head()





df.drop([0], axis = 0, inplace = True)
df.head()





ss = df.iloc[0]
ss





dd = df[1:]
dd.columns = ss
dd.head()





dd





dd["man_hole_id"] = 5464666





dd["Item Name"] = "Manhole"
dd





dd.drop([3], axis = 0, inplace = True)
dd





dd





dd.columns





dd = dd[["man_hole_id", "Item Name", 'Sequence', 'Question', 'Primary Answer', 'Secondary Answer', 'Answer Priority']]
dd





dd.to_csv("firsty.csv", index = False)







