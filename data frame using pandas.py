import pandas as pd
import numpy as np

exam_data = {'name': ['james', 'emily', 'harry', 'micheal', 'sarah', 'luara', 'kevin']
             , 'score': [12.5,15.5,9 ,np.nan,17.5, np.nan, 8.0]
             , 'attempts': [1, 3, 2, 3, 2, 3, 1]
             , 'qualify': ['yes', 'yes', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
df = pd.DataFrame(exam_data, index=labels)
print("THE BASIC SUMMARY OF DATA FRAMES AND ITS DATA:")
print(df.info())