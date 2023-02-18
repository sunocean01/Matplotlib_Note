import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from numpy.random import multivariate_normal
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import numpy as np


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
data = pd.read_csv(filep,index_col=1,nrows=5,parse_dates=True)
data.sort_index(ascending=True,inplace=True)
data['week'] = data.index.isocalendar().week

# print(data.index.strftime("%Y-%m-%d %H:%M:%S"))
# print(data.index)
# exit()

# 创建基图: fig = plt.figure(): 返回的是matplotlib.figure.Figure()的实例化对象(最大的artist),这个很重要,所以fig就有了Figure类的所有的属性和方法!!!!

fig = plt.figure(figsize=[24,14],dpi=100,facecolor='white',edgecolor='blue',linewidth=1,frameon=True)
ax1 = fig.add_subplot(331)
ax1.pcolor(     #将数值映射成颜色;
            [[2,3,4,5,6,7],[8,4.5,3,1,5,2]],
            shading='auto',       #{'flat'，'nearest'，'auto'}
            cmap='CMRmap',     #str or Colormap, default: rcParams["image.cmap"] (default: 'viridis')str或颜色映射实例或注册的颜色映射名称。彩色地图显示 C 值到颜色。如果给的是'image.cmap'会提示可用值有哪些;
            # norm=,              # Normalize 可选正常化，可选:normalize实例将数据值缩放到标准颜色映射范围。 [0, 1] 用于映射到颜色。默认情况下，使用线性缩放将数据范围映射到颜色条范围。
            alpha=0.3,
            
            #其他参数
            )

# ---------------------------------------------------------
ax2 = fig.add_subplot(332)
ax2.pcolormesh(     #和pcolor类似
                [[3,2,7],[6,9,0]],
                )

# --------------------------------------------------------
ax3 = fig.add_subplot(333)
ax3.plot_date(
              data.index,
              data['open'].tolist(),
              )

ax3.tick_params(labelrotation=45)

ax3.xaxis.set_major_locator(DayLocator())    #设置x轴时间主刻度
ax3.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))    #设置x轴时间次刻度
ax3.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))    #格式化成天, 原始数据需要时datetime格式

# ------------------------------------------------------------
ax4 = fig.add_subplot(334)
data['open'].plot(ax=ax4,rot=45)
ax4.xaxis.set_major_locator(DayLocator())    #设置x轴时间主刻度
ax4.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))    #设置x轴时间次刻度
ax4.xaxis.set_major_formatter(DateFormatter('%m-%d'))    #格式化成天

ax5 = fig.add_subplot(335)
ax5.plot(
         data.index,
         data['open'].tolist()
         
         
         )
ax5.tick_params(labelrotation=45)

ax5.xaxis.set_major_locator(DayLocator())    #设置x轴时间主刻度
# ax5.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))    #设置x轴时间次刻度
ax5.xaxis.set_major_formatter(DateFormatter('%Y%m%d'))    #格式化成天

# ----------------------------------------------
ax6 = fig.add_subplot(336,projection="polar")

theta=np.arange(0,2*np.pi,0.02)

ax6.plot(
          [0.35,0.8,1.3,2.6,3.1,4.5,5.2,6],  #极角
          [0.40,0.5,0.6,0.1,0.8,0.7,1.0,0.3],   #极径,半径值
          
          
          # Line2D属性
          linestyle='None',
          marker="*",
          c='r',
          )

# 如果使用polar函数,是不能用ax.polar, 只能用plt.polar
# plt.polar(
          # [0.35,0.8,1.3,2.6,3.1,4.5,5.2,6],
          # [0.40,0.5,0.6,0.1,0.8,0.7,1.0,0.3],
          # linestyle='None',
          # marker="*",
          # c='r',            
            # )

ax7 = fig.add_subplot(337)
X = np.arange(-10, 10, 2)
Y = np.arange(-10, 10, 2)
U, V = np.meshgrid(X, Y)
q = ax7.quiver(             #绘制二维箭头字段。
           X,          #[X, Y]一维或二维阵列，可选:箭头位置的x和y坐标。如果没有给出，它们将根据 U 和 V .如果 X 和 Y 是1D但是 U ， V 是二维的， X ， Y 使用 X, Y = np.meshgrid(X, Y) . 在这种情况下 len(X) 和 len(Y) 必须匹配的列和行维度 U 和 V .
           Y,
           U,
           V,
           # C=,      #一维或二维阵列，可选:通过colormapping定义箭头颜色的数值数据 norm 和 cmap .这不支持显式颜色。如果要直接设置颜色，请使用 颜色 相反。大小 C 必须匹配箭头位置的数量。
           units='height',      #{'width'、'height'、'dots'、'inches'、'x'、'y''xy'}，默认值：'width':箭头尺寸（除了 长度 ）以该单位的倍数计量。
           # scale=,      #float,optional:每个箭头长度单位的数据单位数，例如每个绘图宽度的m/s；较小的比例参数使箭头更长。默认是 None .如果 None 根据平均向量长度和向量数目，采用了一种简单的自动缩放算法。箭头长度单位由 scale_units 参数。
           scale_units='dots',      #{'width'、'height'、'dots'、'inches'、'x'、'y'、'xy'}，可选
           width=0.01,      #float,optional:以箭头单位表示的轴宽度；默认值取决于单位、上方和向量数目的选择；典型的起始值约为绘图宽度的0.005倍。
           headwidth=2,     #float,default 3: 头部宽度为轴宽度的倍数。
           headlength=3,    #float,默认值：5:头部长度为轴宽度的倍数。
           headaxislength=4,   #float,default4.5:竖井交叉处的头部长度。
           minshaft=2,      #float,default 1:箭头刻度以下的长度，以头部长度为单位。不要将此设置为小于1，否则小箭头将看起来很糟糕！
           minlength=1,     #float, default 1:最小长度是轴宽度的倍数；如果箭头长度小于此值，则绘制此直径的点（六边形）。
           pivot='tip',          #{'tail'，'mid'，'middle'，'tip'}，默认值：'tail':锚定到的箭头部分 X ， Y 网格。箭头围绕该点旋转。“mid”是“middle”的同义词。
           color='r',       #颜色或颜色顺序，可选:箭头的显式颜色。如果 C 已经被设定， 颜色 没有效果。
           
           )
ax7.quiverkey(                  #Axes.quiverkey,在quiver中添加一个键
             q,                #quiver的返回值
             X=0.3, Y=1.1,     #key的位置
             U=10,             #key的长度       
             label='Quiver key, length = 10',   #str,key的标签,例如key的长度和单位
             angle=30,          #float,default 0:键箭头的角度，以与x轴的逆时针角度为单位。
             color='b',         #颜色
             labelpos='E',       #{'N'、'S'、'E'、'W'}:将标签分别放在箭头的上方、下方、右侧和左侧。
             labelsep=0.1,      #float,default 0.1:箭头和标签之间的距离（以英寸为单位）
             labelcolor='g',    #color, default: rcParams["text.color"] (default: 'black')
             # fontproperties=,    #dict, optional:A dictionary with keyword arguments accepted by the FontProperties initializer: family, style, variant, size, weight.
             )

ax8 = fig.add_subplot(338)

# data['close'].plot(ax=ax8)

ax8.scatter(                #返回PathCollection
            data.index.tolist(),        #x轴坐标
            data['close'].tolist(),        #y轴坐标 
            s=50,                     #点的大小,float or array-like, shape (n, ), optional:The marker size in points**2. Default is rcParams['lines.markersize'] ** 2.
            # c='#17becf', 
            marker="o",                #MarkerStyle, default: rcParams["scatter.marker"] (default: 'o')MarkerStyle，默认值：rcParams ["scatter.marker"] （默认值：“o”）:https://www.osgeo.cn/matplotlib/api/markers_api.html#module-matplotlib.markers
            cmap=None,              #str or Colormap, default: rcParams["image.cmap"] (default: 'viridis')str或A Colormap 实例或注册的颜色映射名称。 cmap 仅用于 c 是一个浮点数组。
            norm=None,          # Normalize ，默认值：无规格化，默认值：无:如果 c 是一组浮点数， norm 用于缩放颜色数据， c ，范围为0到1，以便映射到colormap cmap .如果 None ，使用默认值 colors.Normalize .
            vmin=None,          #浮点，默认值：无:vmin 和 vmax 与默认范数一起用于映射颜色数组 c 到颜色图 cmap . 如果没有，则使用颜色数组的相应最小值和最大值。不推荐使用 vmin / vmax 什么时候？ norm 给出。
            vmax=None,          #
            alpha=None,         #浮点:0~1，默认值：无:
            linewidths=0.5,    # float or array-like, default: rcParams["lines.linewidth"] (default: 1.5)浮点或类似数组，默认值：标记边缘的线条宽度。注：默认 绿色染料 是“脸”。你可能也想改变这个。
            # verts=<deprecated parameter>, 
            edgecolors='blue',  #散点边颜色{'face', 'none', None} or color or sequence of color, default: rcParams["scatter.edgecolors"] (default: 'face')
            plotnonfinite=False, 
            data=None,
            
            #collection属性
            # edgecolors=,      #重复
            facecolors='r',         #散点填充色:color or list of colors, default: rcParams["patch.facecolor"] (default: 'C0')
            # linewidths=,      #重复
            linestyles='dashed',      #散点边线样式:str or tuple or list thereof, default: 'solid':Valid strings are ['solid', 'dashed', 'dashdot', 'dotted', '-', '--', '-.', ':']. Dash tuples should be of the form:
                                #linestyles: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
            capstyle="projecting",      #CapStyle-like, default: rcParams["patch.capstyle"]:Style to use for capping lines for all paths in the collection. Allowed values are {'butt', 'projecting', 'round'}.
            joinstyle="bevel",      #JoinStyle-like, default: rcParams["patch.joinstyle"]:Style to use for joining lines for all paths in the collection. Allowed values are {'miter', 'round', 'bevel'}.
            antialiaseds=True,      #bool or list of bool, default: rcParams["patch.antialiased"] (default: True):Whether each patch in the collection should be drawn with antialiasing
            # offsets=(0.1,0.1),            #(float, float) or list thereof, default: (0, 0):A vector by which to translate each patch after rendering (default is no translation). The translation is performed in screen (pixel) coordinates (i.e. after the Artist's transform is applied).
            # transOffset=,           #Transform, default: IdentityTransform:A single transform which will be applied to each offsets vector before it is used.
            # offset_position='data',       #{{'screen' (default), 'data' (deprecated)}}:If set to 'data' (deprecated), offsets will be treated as if it is in data coordinates instead of in screen coordinates.
            hatch='/',       #str, optional:Hatching pattern to use in filled paths, if any. Valid strings are ['/', '', '|', '-', '+', 'x', 'o', 'O', '.', '*']. See Hatch style reference for the meaning of each hatch type.
            pickradius=50,       #float, default: 5.0:
            url=["https://www.osgeo.cn/matplotlib/api/collections_api.html#matplotlib.collections.Collection"],
            zorder=2.5,       #float,default:1; 默认情况下(1)点位于线下方,改成2.5后就变成点位于线上方;集合中所有面片共享的绘图顺序。
            
            )

ax8.tick_params(labelrotation=45)

plt.suptitle(
            t="Matplotlib.pyplot_60",
            x=0.3,                      #float, default: 0.5:The x location of the text in figure coordinates.

            y=0.98,                     #float, default: 0.98:The y location of the text in figure coordinates.

            ha="right",                  #horizontalalignment, ha{'center', 'left', 'right'}, default: center:The horizontal alignment of the text relative to (x, y).

            va="top",                #verticalalignment, va{'top', 'center', 'bottom', 'baseline'}, default: top:The vertical alignment of the text relative to (x, y).

            fontsize="large",           #fontsize/size default: rcParams["figure.titlesize"] (default: 'large'):The font size of the text. See Text.set_size for possible values.

            fontweight="normal",        #fontweight, weightdefault: rcParams["figure.titleweight"] (default: 'normal'):            The font weight of the text. See Text.set_weight for possible values.
             
             )


# plt.savefig(
            # fname="matplotlib_module-60.svg",     #默认png格式;    
            # dpi='figure',               #float or 'figure', default: rcParams["savefig.dpi"] (default: 'figure'):The resolution in dots per inch. If 'figure', use the figure's dpi value.
            # facecolor='auto',          #color or 'auto', default: rcParams["savefig.facecolor"] (default: 'auto')颜色或“自动”，默认值
            # edgecolor='b',              #color or 'auto', default: rcParams["savefig.edgecolor"] (default: 'auto'):The edgecolor of the figure. If 'auto', use the current figure edgecolor.
            # orientation='landscape',     #{'landscape', 'portrait'}:Currently only supported by the postscript backend.
            # format=None,                #str,The file format, e.g. 'png', 'pdf', 'svg', ... The behavior when this is unset is documented under fname.
            # transparent=True,          #
            # bbox_inches='tight',       # str({tight, standard}) or Bbox, default: rcParams["savefig.bbox"] (default: None)str或以英寸为单位的边界框：仅保存图形的给定部分。如果“紧”，试着找出这个数字的紧框。{tight, standard}
            # pad_inches=0.1,             #float, default: rcParams["savefig.pad_inches"] (default: 0.1)浮动，默认值：{tight, standard}
            # metadata=None,
            # )


'''tight_layout: Adjust the padding between and around subplots.'''
plt.tight_layout(
                pad=0.8,            #float, default: 1.08: Padding between the figure edge and the edges of subplots, as a fraction of the font size.

                h_pad=0.5,        #float,子图之间,宽度方向距离
                w_pad=2,          #float, default: pad: Padding (height/width) between edges of adjacent subplots, as a fraction of the font size.

                rect=(0,0,1,1),              #两个对角点的坐标位置,tuple (left, bottom, right, top), default: (0, 0, 1, 1): A rectangle in normalized figure coordinates into which the whole subplots area (including labels) will fit.
                )


plt.show()