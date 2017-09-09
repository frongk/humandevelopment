import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

def pir(df):
     # inserts row of null values every other row into input dataframe
     nans = np.where(np.empty_like(df.values), np.nan, np.nan)
     data = np.hstack([nans, df.values]).reshape(-1, df.shape[1])
     return pd.DataFrame(data, columns=df.columns)

def generatedf(filename):
    df = pd.read_csv(filename)
    df.Age = pd.to_numeric(df.Age.apply(lambda x: x.split(' ')[0]))
    df.Age.iloc[24:] = df.Age.iloc[24:]*12
    df.Age = df.Age/12
    df.Weight = pd.to_numeric(df.Weight.apply(lambda x: x.split(' ')[0]))
    df.Length = pd.to_numeric(df.Length.apply(lambda x: x.split(' ')[0].strip('\"')))
    
    for _ in range(2):
        df = pir(df)
    
    df.Age = df.Age.interpolate('linear')
    df.Weight = df.Weight.interpolate('linear')
    df.Length = df.Length.interpolate('linear')
    return df 

def plotdf(df):
    plt.plot(df.Age,df.Weight)
    plt.plot(df.Age,df.Length)
    plt.show()

if __name__=="__main__":
    dfgirl = generatedf('girl_height.csv')
    dfboy = generatedf('boy_height.csv')

    plotdf(dfgirl)
    plotdf(dfboy)

