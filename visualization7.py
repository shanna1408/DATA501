import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('datasets/world_rankings.csv')
combined_df = pd.read_csv('datasets/rank_econ.csv')

""" Compare data between various countries and Canada. """

# - USA
# - Hong Kong
# - North Korea

combined_df = combined_df[(combined_df['Country'] == 'Hong Kong') | (combined_df['Country'] == 'Canada') | (combined_df['Country'] == 'North Korea') | (combined_df['Country'] == 'United States')]

plt.show()