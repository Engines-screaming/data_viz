import pandas as pd
import numpy as np

df = pd.read_csv(r"../data/baseball_data.csv")

# Group by handedness and show median for all columns
grouped = df.groupby("handedness").median().reset_index()

grouped.to_csv(r"../data/parsed_baseball_data.csv")