import numpy as np
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt
import pandas as pd


#read data
data1 = pd.read_excel('iShares S&P 500 Value ETF.xlsx')
returns = data1.values[:,1]

#make qqplot
qqplot(returns, line='s')
plt.show()
