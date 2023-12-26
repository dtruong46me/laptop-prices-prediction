import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILENAME = "raw_bhphotovideo.csv"
PARENT_DIR = os.path.join(os.path.dirname(__file__), "..")
DATA_PATH = os.path.abspath(os.path.join(PARENT_DIR, "data", "Processed", DATA_FILENAME))

df = pd.read_csv(DATA_PATH)

print(df.head())