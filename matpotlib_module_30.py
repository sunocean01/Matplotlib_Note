import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from numpy.random import multivariate_normal



#  解决中文字体显示问题
font = {'family' : 'SimHei'};
mpl.rc('font', **font);

'''测试数据'''
filep = r".\datasource\000061.csv"
data = pd.read_csv(filep,index_col=1,nrows=1000,parse_dates=True)
data.sort_index(ascending=True,inplace=True)
data.reset_index(inplace=True)
# print(data)
# exit()
# 创建基图: fig = plt.figure(): 返回的是matplotlib.figure.Figure()的实例化对象(最大的artist),这个很重要,所以fig就有了Figure类的所有的属性和方法!!!!
fig = plt.figure(figsize=[12,8],dpi=100,facecolor='white',edgecolor='blue',linewidth=1,frameon=True)


'''bar:柱状图'''
x = data["low"][:10].tolist()
y = data["close"][:100].tolist()
z = data["high"][:100].tolist()
# print(x,y)


ax1 = fig.add_subplot(221)
def imshow_plt():           #热图
    plt.imshow(                     
               (y,z),               #图像数据。M，N）：具有标量数据的图像。使用规格化和颜色映射将值映射到颜色。请参见参数 norm ， cmap ， vmin ， vmax .
                                            #（M，N，3）：具有RGB值（0-1浮点或0-255 int）的图像。
                                            # （M，N，4）：具有RGBA值（0-1 float或0-255 int）的图像，即包括透明度。
               # cmap=cm.gray,                # str or Colormap, default: rcParams["image.cmap"] (default: 'viridis')str或用于映射ColorName或ColorScalar实例的已注册颜色。RGB（A）数据忽略此参数。
               # norm=                # Normalize 可选正常化，可选;这个 Normalize 用于将标量数据缩放到 [0, 1] 在映射到颜色之前使用 cmap . 默认情况下，使用线性缩放将最小值映射为0，将最大值映射为1。对于RGB（A）数据，忽略此参数。
               
               
               aspect="auto",       #[{'equal', 'auto'} or float, default: rcParams["image.aspect"] (default:'equal')] The aspect ratio of the Axes. 
               # alpha=0.5,           #[float or array-like, optional]
               # interpolation='bilinear',    #str, default: rcParams["image.interpolation"] (default: 'antialiased')str，默认值：
                                        #支持的值为“none”、“antialiased”、“nearest”、“双线性”、“bicubic”、“spline16”、“spline36”、“hanning”、“hamming”、“hermite”、“kaiser”、“quadric”、“catrom”、“gaussian”、“bessel”、“mitchell”、“sinc”、“lanczos”。
               
               origin='upper',          #{{'upper', 'lower'}}, default: rcParams["image.origin"] (default: 'upper'){'upper'，'lower'}，默认值：放置 [0, 0] 位于轴左上角或左下角的数组索引。约定（默认值）“upper”通常用于矩阵和图像。请注意，垂直轴向上指向“下部”，向下指向“上部”。
               # extent=[-3, 3, -3, 3], #[floats (left, right, bottom, top), optional] 图像将填充的数据坐标中的边界框。图像分别沿X和Y拉伸以填充方框。
               filternorm=False,
               filterrad=4.0,           #浮点>0，默认值：4.0;具有半径参数的过滤器的过滤器半径，即当插值是“sinc”、“lanczos”或“blackman”之一时。
               
               url = "http://www.baidu.com"   #添加超连接, 视图在被save成svg格式下可用: plt.savefig("test.svg")
               # data=data,
               
               
               #Artist属性
               
               )
    plt.colorbar(cax=None,
                 ax=None,
                 shrink=0.5,        #色条缩放比例
                 location="right",   #[None or {'left', 'right', 'top', 'bottom'}]
                 # orientation="horizontal",        #[None or {'vertical', 'horizontal'}] 
                 fraction=0.2,              #float,用于色条的原始轴的分数。
                 aspect=40,                 #色条长宽比例
                 pad=0.05,
                 anchor=(0.5,1.0),          #颜色条轴的定位点。如果垂直，则默认为（0.0，0.5）；如果水平，则默认为（0.5，1.0）。
                 panchor=False,             #（float，float）或 假 可选（浮动，浮动），或点颜色条的父颜色条。如果 假 ，父轴的定位将保持不变。如果垂直，则默认为（1.0，0.5）；如果水平，则默认为（0.5，0.0）。
                 
                 
                 # colorbar属性
                 extend="neither",          #{'neither', 'both', 'min', 'max'}:这些是使用colormap set_under和set_over方法为给定colormap设置的。
                 extendfrac="length",         #{None, 'auto', length, lengths}:最小和最大三角形颜色条延长线的长度为内部颜色条长度的5%（这是默认设置）。如果设置为“自动”，则使三角形颜色条延长与内部框的长度相同（当 间距 设置为“统一”或与相应的相邻内箱相同的长度（当 间距 设置为“成比例”）。如果是标量，则指示作为内部颜色条长度的一部分的最小和最大三角形颜色条扩展的长度。还可以给出分数的两个元素序列，分别表示作为内部颜色条长度的分数的最小和最大颜色条扩展的长度。
                 spacing="uniform",               #{'uniform', 'proportional'} :均匀间距为每个离散颜色提供相同的空间；proportional使空间与数据间隔成比例。
                 # ticks=,        # None or list of ticks or Locator If None, ticks are determined automati-cally from the input.
                 format="%.1f",     #另见formater类
                 # drawedges=True,    #bool是否在颜色边界绘制线条
                 label="Close_Open",
                                 
                 )
imshow_plt()

# --------------------------------------------------------------------
ax2 = fig.add_subplot(222)
plt.figtext(                #放在figure上的文本
            x=0.7,
            y=0.8,
            s="tst\nagain",
            # fontdict={},        #替代文本属性的字典; rcParams["font.*"] .
            
            # Text文本属性:
            alpha=0.6,
            # backgroundcolor="r",
            # bbox=,
            color='c',          #color,c:
            fontfamily='cursive',         #fontfamily, family: 'serif'、'sans-serif'、'cursive'、'fantasy'、'monospace'
            # fontproperties=                        #fontproperties or font or font_properties:font_manager.FontProperties or str or pathlib.Path
            fontsize=16,               #float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
            fontstretch='ultra-condensed',            #fontstretch or stretch:{a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'}
            fontstyle='oblique',              #fontstyle or style:{'normal', 'italic', 'oblique'}
            fontvariant='small-caps',                #fontvariant or variant:{'normal', 'small-caps'}
            fontweight='semibold',                                #fontweight or weight:{a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}
            ha="left",                            #horizontalalignment or ha:{'center', 'right', 'left'}
            linespacing=1.1,              #float(multiple of font size), 行距
            multialignment="right",                        #multialignment or ma:{'left', 'right', 'center'}
            position=(0.7,0.7),                #(float,float):重置文本的位置
            rotation=45,            #float
            rotation_mode='anchor',         #{None, 'default', 'anchor'}
            url="http://www.baidu.com",     #当被保存为 svg格式的图片时可用
            visible=True,
            zorder=1,
            wrap=True,
            )

ax2.grid(               #或plt.grid(),网格线,
         b=True,
         which="major",     #optional,{'major'，'minor'，'both'}，可选
         axis='y',          #'both','x','y'
         
         # Line2D属性
         
         )

ax2.hist(
         # x=data["low"],
         x=data[["close","open"]],
         # x=data["low"].tolist(),
         # x=[data["low"].tolist(),data["open"].tolist()],
         # x=(data["low"].tolist(),data["open"].tolist()),
         
         
         
         # bins=[4,6,8,12],       #int 或者列表,str, 如果是列表如[4,6,8,12]表示[4,6),[6,8),[8,12)三个bin; str:'auto', 'fd', 'doane', 'scott', 'stone', 'rice', 'sturges', or 'sqrt'
         bins='scott',       #int 或者列表,str, 如果是列表如[4,6,8,12]表示[4,6),[6,8),[8,12)三个bin; str:'auto', 'fd', 'doane', 'scott', 'stone', 'rice', 'sturges', or 'sqrt'
         range=(4,10),        #tuple or None, default None; (x.min(),x.max())
         density=False,          #bool, default False; True:总和是1,各个bin的占比; False:各个bin包含的个数
         # cumulative=True,       #bool or -1, default False;  堆积图
         # bottom=5             #?
         histtype="bar",       #柱子的形状: {'bar', 'barstacked', 'step', 'stepfilled'}, default: 'bar'
         align="right",              #{'left', 'mid', 'right'}, default: 'mid'
         orientation="vertical",   #{'vertical', 'horizontal'}, default: 'vertical'
         rwidth=1,                   #The relative width of the bars as a fraction of the bin width. If None, automatically compute the width.Ignored if histtype is 'step' or 'stepfilled'.
         log=False,
         # color=['g','b'],         #柱子的颜色
         # label=["low","open"],       #so that legend will work as expected.后面ax.legend()用
         stacked=False,      #有两组数据的时候,是堆着放还是并列放,If True, multiple data are stacked on top of each other If False multiple data are arranged side by side if histtype is 'bar' or on top of each other if histtype is 'step'
         
         
         alpha=0.3,
         zorder=-1
         
         )
ax2.legend()        #或plt.legend()

# -------------------------------------------------------------
samplefile = r"..\testfile\FFmc0320210126.csv"
data_ax3 = pd.read_csv(samplefile,usecols=["T008016_Value","T008034_Value"])
data_ax3.dropna(how="any",inplace=True)

ax3 = fig.add_subplot(223)
ax3.hist2d(
           x=data_ax3["T008016_Value"],
           y=data_ax3["T008034_Value"],
           bins=200,     #default 10
                     #int: 则表示两个维度的箱数（nx=ny=bin）
                     #[int,int]:每个维度中的箱数（nx，ny=箱）
                     #如果类似数组，则为两个维度（x_edges=y_edges=bin）的bin边。
                     #如果 [array, array] ，每个维度中的肥料箱边缘（x_边缘，y_边缘=肥料箱）。
           # range=[[8,10],[8,12]],    # [[xmin, xmax], [ymin, ymax]] . 此范围之外的所有值都将被视为异常值，并且不在柱状图中计数。
           density=True,        ##bool, default False; True:总和是1,各个bin的占比; False:各个bin包含的个数
           # weights=,            #权重系数;加权每个样本的值数组（x_i，y_i）。
           # cmin=1,             #所有计数小于 cmin 或超过 cmax 将不显示（在传递到imshow之前设置为NaN），并且返回值计数直方图中的这些计数值也将在返回时设置为NaN。
           # cmax=200,
           
           
           #Other parameters:
           norm=mcolors.PowerNorm(0.3),
           # cmap=,           #颜色映射或str，可选
           alpha=0.8,           
           
           #pcolormesh方法及QuadMesh artist           
           )
plt.colorbar(cax=None,ax=ax3)

ax4 = fig.add_subplot(224)




# ax.legend(loc="upper left")             # 图例放的位置;“upper right”,"lower left","lower right"   https://blog.csdn.net/chichoxian/article/details/101058046
'''
loc:
    best
    upper right
    upper left
    lower left
    lower right
    right
    center left
    center right
    lower center
    upper center
    center
'''

def ax_legend():
    ax.legend(
              ("line1","line2"),
              loc=0            #对axes上面的图例(legend)进行设置
                        # 'best' 0; 'upper right' 1;'upper left' 2;'lower left' 3;'lower right' 4;'right' 5;'center left' 6;'center right' 7;'lower center' 8;'upper center' 9;'center' 10;
              )         
# ax_legend()

def plt_legend():
    plt.legend(
               labels=["line1","line2"],
               
               
               
               
               )

plt_legend()

# plt.figlegend()                                     #对figure上的图例(legend)进行设置,包括所有axes; 见plt.figlegend;
# fig.legend()
# plt.savefig("test.svg")

plt.show()
