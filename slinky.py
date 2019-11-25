#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #principal librería para el análisis de datos
import numpy as np #librería para trabajar con matrices, vectores y cálculos
import matplotlib.pyplot as plt #librería para realizar gráficas
import seaborn as sns #librería para realizar gráficas
import numpy


# In[2]:


data1 = pd.read_csv("datosCm.csv", sep= ";")


# In[4]:


data1


# In[5]:


data2= pd.read_csv("DatosSlinky1.csv", sep=";")


# In[8]:


data2


# In[29]:


data3 = pd.read_csv("datos.csv", sep=";")


# In[30]:


plt.plot(data1.t, data1.y, "r-", data2.t, data2.y, "g--", data3.t, data3.y)
plt.ylabel('Desplazamiento en y (m)')
plt.xlabel('Tiempo (s)')
plt.show()


# In[13]:


data3


# In[46]:


dx= data2.y.diff()


# In[47]:


plt.plot(data2.t,dx)
plt.ylabel('Desplazamiento en y (m)')
plt.xlabel('Tiempo (s)')
plt.show()


# In[50]:


data4= pd.read_csv("velocidad.csv", sep=";" )


# In[51]:


data4


# In[53]:





# In[ ]:




