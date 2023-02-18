import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from numpy.random import multivariate_normal
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import datetime
from matplotlib import rcParams

import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = None


fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(14,8))

fp = r".\testfile\002161.SZ.csv"
data = pd.read_csv(fp,parse_dates=["trade_date"]).fillna(0).sort_values("trade_date")
# print(data)
# exit()
'''twinx:共享x轴'''
ax1.plot(data["trade_date"],data["open"])

ax2 = ax1.twinx()

ax2.plot(data.trade_date,data.amount,c='r')

ax1.tick_params(labelrotation=45)

'''twiny:共享y轴'''

ax4.plot(data.vol,data.trade_date)
ax4.tick_params(labelrotation=45)
ax3 = ax4.twiny()
ax3.plot(data.close,data.trade_date,c='r')

plt.show(block=True)