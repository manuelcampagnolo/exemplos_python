from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import pandas as pd
import numpy as np
np.set_printoptions(precision=4)
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder

# df is  the sample matrix (n_obs,n_variables) 
# nomeVarResposta is 'Tipo' (df.Tipo): the values are strings (they are the classes of interest)
# could be 1st column for the response variable "nomeVarResposta" and idxInicioBandas=1. Columns to use for LDA have indices [idxInicioBandas:]
# lda: linear combination of features that characterizes or separates the classes
# X_lda: matrix n*k, with k= (n° of classes - 1); each column is the component on the k-th discriminate axis
# target_names are the class names (from df.Tipo)
# target_values are the class indices [0,1,...6]
# y are the class indices of the response variable 
def comp_discrim(df,nomeVarResposta, idxInicioBandas):
  #df = df.iloc[1: , :]
  X = np.array(df.iloc[:,idxInicioBandas:])
  le = LabelEncoder()
  y = le.fit_transform(df[nomeVarResposta])
  #print(y)
  target_names=le.inverse_transform([x for x in range(min(y),max(y)+1)])
  target_values=[x for x in range(min(y),max(y)+1)]
  #print(target_names)
  #print(target_values)
  #print(np.bincount(y)) # np.bincount(x)
  lda = LinearDiscriminantAnalysis() # (n_components=1)
  lda.fit(X,y)
  X_lda = lda.transform(X)
  return X_lda, y, target_names,target_values, lda, X

# convert array into dataFrame
def convertXtoDf(X_lda,df,idxInicioBandas):
  X=X_lda.copy()
  df_lda=df.copy()
  df_lda=df_lda.iloc[:,:idxInicioBandas]
  #print(df_lda)
  df_lda.reset_index(drop=False, inplace=True)
  pd.DataFrame(data = X)
  df_lda=pd.concat([df_lda, pd.DataFrame(data = X)], axis = 1) 
  #print(df_lda)
  nomesCols=df_lda.columns.to_list()[:-X.shape[1]]+[str(i+1) for i in range(X.shape[1])]
  df_lda.columns=nomesCols
  if 'index' in df_lda.columns:
    df_lda.drop('index', inplace=True, axis=1)
  return df_lda

def ScatterPlot(X_lda, y, nomesClasses, indicesClasses, coresClasses,axis1,axis2): 
  plt.figure()
  for color, i, target_name in zip(coresClasses, indicesClasses, nomesClasses):
      plt.scatter(
          X_lda[y == i, axis1], X_lda[y == i, axis2], alpha=0.8, color=color, label=target_name
      )
  plt.legend(loc="best", shadow=False, scatterpoints=1)
  plt.title("LDA")
  plt.show()

# Output: spectral signature for each  class 
# graphic of the mean spectral signature and standard deviation 
def SpectralSignature(mydf, idxInicioBandas,nomeVarResposta, nomesClasses,coresClasses,Title):
  df=mydf.copy() # to avoid indexing mydf
  df.set_index(nomeVarResposta, inplace=True)
  for nomeClasse in nomesClasses: 
    mycolor=coresClasses[list(nomesClasses).index(nomeClasse)]
    classedf=df.loc[nomeClasse]
    X = np.array(classedf.iloc[:,(idxInicioBandas-1):])
    #if nomeClasse=='doente' : print(X)
    means=X.mean(axis=0)
    stds=X.std(axis=0)
    bandNumbers=df.columns.to_list()[(idxInicioBandas-1):]
    #if nomeClasse=='doente' :  print(bandNumbers)
    bandas=np.asarray([float(i) for i in bandNumbers])
    plt.plot(bandas, means, label= nomeClasse,color=mycolor)
    plt.fill_between(bandas, means-stds,means+stds, alpha=0.1,color=mycolor)
  if Title=='Spectral signatures': 
    plt.xlabel('Wavelenght (nm)')
    plt.ylabel('Reflectance (\u2031)')
  plt.legend()
  plt.title(Title)

# Processing
# compute LDA components
X_lda, y, nomesClasses, indicesClasses, lda, X = comp_discrim(df,nomeVarResposta, idxInicioBandas)

# create signatures using LDA components
plt.rcParams['figure.dpi'] = 100
df_lda=convertXtoDf(X_lda,df)
SpectralSignature(df_lda, idxInicioBandas,nomeVarResposta, nomesClasses,coresClasses,'LDA signatures')

# plot observations discriminant plane 
# last indices are the LDA components indices
plt.rcParams['figure.dpi'] = 100
ScatterPlot(X_lda, y, nomesClasses, indicesClasses, coresClasses,0,2)
