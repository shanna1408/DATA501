import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

combined_df = pd.read_csv('datasets/rank_econ.csv')

""" Understand whether academic quality actually has an effect on employability. """
df3 = combined_df[["Country", "score scaled", "Unemployment (%)"]]
df3['score scaled'] = pd.to_numeric(df3['score scaled'], errors='coerce')
df3 = df3.dropna()
df3 = df3.groupby(["Country"]).mean()
print(df3)
plot3 = sns.regplot(x="score scaled", y="Unemployment (%)", data=df3)
plot3.set(xlabel='score scaled', ylabel='Unemployment (%)')
plot3.set_title('Academic quality vs Unemployment')

plt.show()