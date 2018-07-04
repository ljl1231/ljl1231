import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('age.csv') 
ljl = data['22']
plt.plot(ljl, '.') 
plt.ylim((1,200))  
plt.xlabel('X')  
plt.ylabel('Y')
plt.show()

