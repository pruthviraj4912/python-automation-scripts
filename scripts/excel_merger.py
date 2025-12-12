# excel_merger.py
import pandas as pd
import glob

files = glob.glob("./excels/*.xlsx")
dfs = [pd.read_excel(f) for f in files]

merged = pd.concat(dfs)
merged.to_excel("merged.xlsx", index=False)
