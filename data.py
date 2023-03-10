import pandas as pd
  
# reading two csv files
ranking = pd.read_csv('datasets/world_rankings.csv')
econ  = pd.read_csv('datasets/economic_freedom.csv',encoding_errors='ignore')

# data cleaning
ranking.rename(columns={"location": "Country"}, inplace = True)
ranking.replace("China (Mainland)", "China", inplace = True)
ranking.drop(columns=['location code'], inplace = True)
econ.replace("Korea, South", "South Korea", inplace = True)
econ.drop(columns=['Country Name', 'CountryID', 'WEBNAME'], inplace = True)

print("------------------------Rankings------------------------\n")
print(ranking)
print("------------------------Econ------------------------\n")
print(econ)
# using merge function by setting how='inner'
dataset = pd.merge(ranking, econ, 
                   on='Country', 
                   how='inner')
dataset.sort_values('Country', ascending=True, inplace = True)
# displaying result
print(dataset)
dataset.to_csv('datasets/rank_econ.csv')