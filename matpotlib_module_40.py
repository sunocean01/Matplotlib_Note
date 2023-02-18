import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from numpy.random import multivariate_normal

'''
1.plot: 画图方法

2.labels, legend: label的设定及图例的显示
    legend()
    legend(labels)
    legend(handles, labels)
'''

#  解决中文字体显示问题
# font = {'family' : 'SimHei'};
# mpl.rc('font', **font);

import matplotlib
matplotlib.rc("font",family='DejaVu Sans')


'''测试数据'''
filep = r".\datasource\000061.csv"
data = pd.read_csv(filep,index_col=1,nrows=100,parse_dates=True)
data.sort_index(ascending=True,inplace=True)

# print(data.head())
# exit()

# 创建基图: fig = plt.figure(): 返回的是matplotlib.figure.Figure()的实例化对象(最大的artist),这个很重要,所以fig就有了Figure类的所有的属性和方法!!!!
fig = plt.figure(figsize=[12,8],dpi=100,facecolor='white',edgecolor='blue',linewidth=1,frameon=True)


'''bar:柱状图'''
x = data["low"][:10].tolist()
y = data["close"][:100].tolist()
z = data["high"][:100].tolist()
# print(x,y)

ax1 = fig.add_subplot(231)
line1, = ax1.plot("open",data=data.head(50),color='y')
ax1.tick_params(labelrotation=20)
plt.legend(         #或者ax.legend
            # handles=,      #见ax2.legend()
            labels=['ax1'],
           
            #其他参数
            loc=0,        #str or pair of floats, 具体参数见下面对照表;
            bbox_to_anchor=(0.5,0.,0.5,0.3),   #BboxBase, 2-tuple, or 4-tuple of floats; 此参数可以将图例放在任意位置
                                                #loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5):(x, y, width, height) 放置图例的位置
                                                #loc='upper right', bbox_to_anchor=(0.5, 0.5):2-元组 (x, y) 放置由指定的图例角 loc 例如，要将图例的右上角置于轴（或图）的中心，
            ncol=1,                             #图例的列数:int; 如果有很多图例,可以放成多列
            fontsize="medium",              #字体大小:int或{'xx-small'，'x-small'，'small'，'medium'，'large'，'x-large'，'xx-large'}
            labelcolor='r',            #设置图例中文本的颜色:str,list:labelcolor还可以使用“linecolor”、“markerfacecolor”（或“mfc”）或“markeredgecolor”（或“mec”）使其与线条或标记的颜色匹配
            numpoints=2,              #int, default: rcParams["legend.numpoints"] (default: 1):为创建图例项时，图例中标记点的数目 Line2D （行）。
            # scatterpoints=,         #为创建图例项时，图例中标记点的数目 PathCollection （散点图）。
            # scatteryoffsets=,       #为散点图图例项创建的标记的垂直偏移量（相对于字体大小）。0.0位于图例文本的底部，1.0位于顶部。若要在同一高度绘制所有标记，请设置为 [0.5] .
            markerscale=0.5,        # float, default: rcParams["legend.markerscale"] (default: 1.0)浮动，默认值：与最初绘制的图例标记相比，图例标记的相对大小。
            markerfirst=False,       #bool，默认值：True:如果 True ，图例标记放置在图例标签的左侧。如果 假 ，将图例的标签放置在图例的右侧。
            frameon=True,            #bool, default: rcParams["legend.frameon"] (default: True):图例是否应绘制在补片（框架）上。
            fancybox=False,           #bool, default: rcParams["legend.fancybox"] (default: True)布尔:是否应在 FancyBboxPatch 构成了图例的背景。
            shadow=True,            #bool, default: rcParams["legend.shadow"] (default: False):是否在传说背后画上阴影。
            framealpha=0.3,         #float, default: rcParams["legend.framealpha"] (default: 0.8):背景的透明度。如果 阴影 激活并 框架α 是 None ，默认值将被忽略。
            facecolor='g',      #"inherit" or color, default: rcParams["legend.facecolor"] (default: 'inherit'):图例的背景色。如果 "inherit" 使用 rcParams["axes.facecolor"] (default: 'white') .
            edgecolor='b',      #"inherit" or color, default: rcParams["legend.edgecolor"] (default: '0.8'):边缘颜色。如果 "inherit" ，使用take rcParams["axes.edgecolor"] (default: 'black') .
            mode="expend",      #{"expand", None}:如果 mode 设置为 "expand" 图例将水平展开以填充轴区域（或 bbox_to_anchor 如果定义了图例的大小）。
            # bbox_transform=,    #无或 matplotlib.transforms.Transform:边界框的变换( bbox_to_anchor ）对于一个值 None （默认）轴' transAxes 将使用转换。
            title="legend",         #str or None,图例的标题
            title_fontsize='small', #int or {{'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}}, default: rcParams["legend.title_fontsize"] (default: None)int或{'xx-small'、'x-small'、'small'、'medium'、'large'、'x-large'、'xx-large'}，默认值：
            borderpad=1,              #float, default: rcParams["legend.borderpad"] (default: 0.4)
            labelspacing=0.8,           #float, default: rcParams["legend.labelspacing"] (default: 0.5):图例项之间的垂直间距，以字体大小为单位。
            handlelength=1.5,           #float, default: rcParams["legend.handlelength"] (default: 2.0):图例句柄的长度，以字体大小为单位。
            handletextpad=0.2,          #float, default: rcParams["legend.handletextpad"] (default: 0.8):图例句柄和文本之间的填充区，以字体大小为单位。
            borderaxespad=0.1,            #float, default: rcParams["legend.borderaxespad"] (default: 0.5)浮动，:轴和图例边框之间的填充区，以字体大小为单位。
            columnspacing=0.5,            #float default: rcParams["legend.columnspacing"] (default: 2.0):列之间的间距，以字体大小为单位。
            # handler_map=,               #dict or None:将实例或类型映射到图例处理程序的自定义字典。这个 handler_map 更新在中找到的默认处理程序映射 matplotlib.legend.Legend.get_legend_handler_map .
           )        

'''loc 参数:
Location String	Location Code
'best'	0
'upper right'	1
'upper left'	2
'lower left'	3
'lower right'	4
'right'	5
'center left'	6
'center right'	7
'lower center'	8
'upper center'	9
'center'	10
'''

ax3 = fig.add_subplot(233)
line3, = ax3.plot(data["close"][:50])
# line3.set_label("ax2_line")

ax3.legend(
            handles=[line1,line3],        #plot等是有返回值的,
            labels=["ax1_line","ax2_line"],
            labelspacing=1,     #图例之间的行距;
            )



ax4 = fig.add_subplot(234)
ax4.plot([1,2,3],[2,3,2.5],color='g')
# plt.legend(["ax3_legend"])


ax5 = fig.add_subplot(235)
ax5.plot([[1,1.5,2],[1.3,1,0.5]],label=["ax4_line1","_line2","ax4_line3"])      #如果标签前面有下划线'_',则这个标签将不会显示;
ax5.legend(
            ncol=2,
            )




ax6 = fig.add_subplot(236)
data[["open","close"]].plot(ax=ax6)     #DataFrame.plot: 会默认显示legend;

# plt.figlegend(loc="upper left")
plt.show()