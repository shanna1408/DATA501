import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

combined_df = pd.read_csv('../datasets/rank_econ.csv')

""" Understand the connection between economic success of a country and quality of education. """
df4 = combined_df[["Country", "score scaled", "2019 Score"]]
df4['score scaled'] = pd.to_numeric(df4['score scaled'], errors='coerce')
df4 = df4.dropna()
df4 = df4.groupby(["Country"]).mean()
print(df4)
plot4 = sns.regplot(x="2019 Score", y="score scaled", data=df4)
plot4.set(xlabel='Economy 2019 score', ylabel='Education score scaled')
plot4.set_title('Economic success vs Quality of education')

plt.show()