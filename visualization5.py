import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

combined_df = pd.read_csv('datasets/rank_econ.csv')

""" Understand the connection between economic success of a country and employability of institutions. """
df5 = combined_df[["Country", "er score", "2019 Score"]]
df5 = df5.dropna()
df5 = df5.groupby(["Country"]).mean()
print(df5)
plot5 = sns.regplot(x="2019 Score", y="er score", data=df5)
plot5.set(xlabel='Economy 2019 score', ylabel='Employer Reputation Score')
plot5.set_title('Economic success vs Employability of institutions')

plt.show()
