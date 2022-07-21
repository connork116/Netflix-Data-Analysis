"""
Author: Connor King
Early stages of dataset cleaning 
Cleaning credits.csv
"""
import pandas as pd
import numpy as np

df = pd.read_csv('datasets/titles.csv')

# Drpos NaNs for imdb_score column
df = df.dropna(subset = ['imdb_score'])