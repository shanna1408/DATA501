import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../datasets/world_rankings.csv')

""" Understand the connection between academic reputation and employability. """
plot1 = sns.regplot(x="ar score", y="er score", data=df)
plot1.set(xlabel='Academic Reputation Score', ylabel='Employer Reputation Score')
plot1.set_title('Academic Reputation Score vs Employer Reputation Score')

plt.show()