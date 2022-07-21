"""
Author: Connor King
Early stages of dataset cleaning 
Cleaning credits.csv
"""
import pandas as pd
import numpy as np

df = pd.read_csv('datasets/titles.csv')
print(len(df))

# Drpos NaNs for imdb_score column
df = df.dropna(subset = ['imdb_score'])
print(len(df))

df = df.dropna(subset=['imdb_score'])
print(len(df))