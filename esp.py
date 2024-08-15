import pandas as pd
import matplotlib.pyplot as plt
s = pd.Series(data=[10,5,15,20,10],index = [1,2,3,4,5])
s.plot()
plt.show()
#df = pd.read_csv("GoogleApps.csv")
#print(pd.isnull(df['Rating']).head()) #шукає порожнє значення у перших 5
#df.fillna({'Rating':-1},inplace=True)
#print(df['Rating'][0])
#print(df['Rating'].value_counts().index[1])
#df.info()
#df.dropna()#видалити значення
#df.info()
#print(df.head())
#print(df.head(1))
#print(df.describe())
#print(df["Category"].tail(1))
#print(df.tail())
#print(df['Size'].mean())[]
#print(df['Installs'].median())
#print(df["Installs"].mean(0))
#print(df["Installs"].mean(), df["Installs"].median())
#print(df[df["Category"]=="ART_AND_DESIGN"]['Installs'].median())
