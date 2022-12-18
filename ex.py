import pandas as pd
import numpy as np
df=pd.read_csv("first.csv")


data = df.drop(labels=[0,1], axis=0)
print(data.columns)