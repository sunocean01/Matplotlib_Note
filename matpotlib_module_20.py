import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

#  解决中文字体显示问题
font = {'family' : 'SimHei'};
mpl.rc('font', **font);

'''测试数据'''
filep = r".\datasource\000061.csv"
data = pd.read_csv(filep,index_col=1,nrows=100,parse_dates=True)
data.sort_index(ascending=True,inplace=True)
data.reset_index(inplace=True)
# print(data)
# exit()
# 创建基图: fig = plt.figure(): 返回的是matplotlib.figure.Figure()的实例化对象(最大的artist),这个很重要,所以fig就有了Figure类的所有的属性和方法!!!!
fig = plt.figure(figsize=[12,8],dpi=100,facecolor='white',edgecolor='blue',linewidth=1,frameon=True)


'''bar:柱状图'''
x = data["trade_date"][:10].tolist()
y = data["close"][:10].tolist()



ax1 = fig.add_subplot(221)
def bar_plot():
    ax1.bar(
            x=x,
            height=y,
            width=0.5,          #柱子的宽度;
            bottom=3,           #y坐标从多少开始;
            align="edge",     #x轴的刻度线在柱子的什么位置:{'center'，'edge}，默认值：'center'
            
            #其他及Rectangle参数
            # color='r',          #柱子的颜色; Set both the edgecolor and the facecolor.
            edgecolor='r',      #柱子边框颜色; 只设置edgecolor
            facecolor='b',      #只设置facecolor;
            # linestyle="-",       #线型,实际柱状图不需要;
                # '''
                    # '-' or 'solid' solid line;
                    # '--' or 'dashed' dashed line;
                    # '-.' or 'dashdot' dash-dotted line
                    # ':' or 'dotted' dotted line
                    # 'None' draw nothing
                    # 'none' draw nothing
                    # ' ' draw nothing
                    # '' draw nothing
                # '''
            linewidth=2,        #柱子边框宽度; 0 就是没有边框;
            # tick_label=[1,2,3,4,5,6,7,8,9,10],  #x轴刻度值, 相似 ax1.set_xticklabels()
            xerr = None,        #设置误差,标量：所有条的对称+/-值;形状（n，）：每根钢筋的对称+/-值;形状（2，N）：为每个条形图单独设置-和+值。第一行包含下面的错误，第二行包含上面的错误。
            yerr = None,        #设置误差;
            ecolor='green',     #误差线的颜色;
            # capsize=,           #以点为单位的误差线帽的长度。
            log=False,           #bool,是否将一轴设置成对数刻度;
            
            # 下面是属性,和Figure属性比较相似:
            alpha=0.3,
            animated=False,     #是否画动态图;
            antialiased=False,  #bool,设置是否使用抗锯齿渲染。
            capstyle="round",   #线型的连接点形状,bar图上好像用不到 [CapStyle or {'butt', 'projecting', 'round'}]
            # contains= False,  #bool,用于评估事件是否在艺术家内部的自定义选取器函数。函数必须具有签名：不知怎么用
            fill=True,
            gid="name",         #设置id
            hatch="/",          #填充图案,'/'、''、''、'-'、'+'、'X'、'O'、'O'、'、'、'*';
            in_layout=True,     #Set if artist is to be included in layout calculations, E.g. Constrained Layout Guide, Figure.tight_layout(), and fig.savefig(fname, bbox_inches='tight').
            joinstyle="miter",       #[JoinStyle or {'miter', 'round', 'bevel'}]
            label="Test",       #Set a label that will be displayed in the legend
            snap=False,          #设置捕捉行为;
            # transform="",       #设置艺术家变换。
            visible=True,      #bool,设置柱状图是否可见;
            zorder=1,           #叠放顺序;

            )

    ax1.tick_params(labelrotation=45)
bar_plot()

# -------------------------------------------------------------
'''plot:画折线或点'''
ax2 = fig.add_subplot(222)

# 方法一:
def plot_one():   # 参数介绍
    ax2.plot(
             x,     #x轴坐标的值
             y,     #y轴坐标的值
             # [fmt], #fmt是定义基本格式(如颜色,宽度,标记等,),可以使用 Line2D 属性作为关键字参数
             # 下面是Line2D属性
             alpha=0.6,     #float,折线的透明度;
             animated=False,    #是否生成动态图;
             # antialiased=False, #bool,设置是否使用抗锯齿渲染。
             
             clip_box = [[0.1,0.1],[3,3]],          # 可变边界框,clipbox: [[xmin, ymin], [xmax, ymax]]或 (xmin, ymin, xmax, ymax)
             color='r',         #color,c: 线条颜色
             # contains=,         #定义一个容器;
             
             # dash_capstyle='round',     #如果线型是dash, 线的末端的形状
             dash_joinstyle='round',        # JoinStyle or {'miter', 'round', 'bevel'}
             dashes=(5, 2, 1, 2) ,          #设定线型的频率,(5, 2, 1, 2) describes a sequence of 5 point and 1 point dashes separated by 2 point spaces.
             drawstyle='default',            #drawstyle or ds : {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default'
             
             # fillstyle='full',          #标记marker的填充风格:{'full', 'left', 'right', 'bottom', 'top', 'none'}
             
             # gid = "testid",        #没明白这个地方是哪个的id?
             in_layout=True,        #Set if artist is to be included in layout calculations, E.g. Constrained Layout Guide, Figure.tight_layout(), and fig.savefig(fname, bbox_inches='tight').
             
             label="testplot",      #图例上的标签, 图例显示需要使用ax2.legend;
             linestyle='--',        #linestyle or ls : {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
             linewidth=2,           #线宽
             
             marker="o",            #见maplotlib手册p2283, 部分标记:".", ",","o","v","^","<",">","*","x","X"
             markeredgecolor='b',   #markeredgecolor or mec
             markeredgewidth=1,     #markeredgewidth or mew 
             markerfacecolor='green',   #markerfacecolor or mfc
             # markerfacecoloralt='orange',   #交替的颜色;
             markersize=8,          #标记大小
             markevery=3,           #有选择性的标记  None or int or (int, int) or slice or list[int] or float or (float, float) or list[bool] 
             solid_capstyle='projecting',       # CapStyle or {'butt', 'projecting', 'round'}
             # solid_joinstyle='miter',      #JoinStyle or {'miter', 'round', 'bevel'}
             # visible=True,         #bool, 是否可见;
             # xdata=x,
             # ydata=y,
             # zorder=0.5,               #顺序;
             # data,#data参数见plot_two介绍;
             )
# plot_one()

def plot_two():     # 以DataFrame 或 Dict的形式传数据
    ax2.plot(
             'open',      # 传入 对应列的标签
             'close',           # 传入 对应列的标签
             # [fmt],     #fmt是定义基本格式(如颜色,宽度,标记等,),可以使用 Line2D 属性作为关键字参数
             data=data,
             )
plot_two()

def plot_three():
    ax2.plot(
             [1,2,3],
             [2,5,1],
             )
# plot_three()

def plot_four():
    ax2.plot(
             [[1,2,3],[2,5,1]]
             )

# plot_four()

ax2.legend()
ax2.tick_params(labelrotation=45,)

'''annotate:标注,或者画箭头'''
def plot_annotate(): 
    ax2.annotate(
                 text="annotate",       #文本内容
                 
                 xy=(5.75,6),          #被注释地方，使用坐标xy=(x,y)给出；[(float, float)] The point (x, y) to annotate. The coordinate system is determined by xycoords
                 xytext=(6.0,7.0),  #插入文本的地方，使用坐标xytext=(x,y)给出。[(float, float), default: xy] The position (x, y) to place the text at. The coordinate system is determined by textcoords.
                 
                 # xycoords='figure points',  #另外一种坐标系
                 # textcoords='offset points',
                 
                 
                 arrowprops=dict(width=0.5,headwidth=10,headlength=15,facecolor='black', shrink=0.1),    #dict,在注释点和文本框之间画一个箭头:dict={}
                 # arrowprops=dict(arrowstyle='->'),    #如何使用了arrowstyle参数,上面那些参数是不被允许的; 见maplotlib手册p2458
                 # textcoords='offset points',
                 annotation_clip=True,      #bool,当x,y坐标值不在现有坐标内,如何显示;
                 )
plot_annotate()

def textnotate():
    ax2.text(
             s="textnotate",
             x=6.5,         #坐标y轴位置;
             y=5.5,         #坐标y轴位置;
             alpha=0.9,     #字体透明度;
             # backgroundcolor='r',   #文本框背景颜色;
             # bbox=,
             color='g',      #字体颜色
             fontfamily='cursive',   #字体,fontfamily or family:{FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
             # fontproperties=,       #fontproperties or font or font_properties:font_manager.FontProperties or str or pathlib.Path
             fontsize=14,             #fontsize or size : float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
             fontstretch= 100,      #fontstretch or stretch: 范围0-1000内的数值，'ultra condensed'、'extra condensed'、'condensed'、'semi condensed'、'normal'、'semi expanded'、'expanded'、'extra expanded'、'extra expanded'、'extra expanded'、'extra exp 
             fontstyle='italic',            #fontstyle or style: {'normal', 'italic', 'oblique'}
             fontvariant='small-caps',          #fontvariant or variant: {'normal', 'small-caps'}
             fontweight='light',            #范围为0-1000、'ultralight'、'light'、'normal'、'regular'、'book'、'medium'、'roman'、'semibold'、'demi bold'、'demi'、'bold'、'heavy'、'extra bold'、'black'的数值。
             gid='textnotate',      #str, id
             # horizontalalignment='right',  #horizontalalignment or ha:{'center', 'right', 'left'}
             multialignment='left',             #multialignment or ma:{'left', 'right', 'center'}
             position=(7,6),        #位置,(float, float);这个优先级更高
             rotation=45,           #文本框角度,float or {'vertical', 'horizontal'}
             rotation_mode='anchor',#{None, 'default', 'anchor'}
             visible=True,
             )
textnotate()

ax2.autoscale(                  #将轴视图自动缩放为数据（切换）
              enable=True,      #bool或None，默认值：True; True打开自动缩放，False关闭自动缩放。无保留自动缩放状态不变。
              axis="both",      #{'both'，'x'，'y'}，默认值：'both', 在哪个轴上操作。
              tight=True,       #bool或None，默认值：None; 如果为True，请先将页边距设置为零。然后，此参数被转发到 autoscale_view （不管其值如何）；请参见此处对其行为的描述。
              )


# -------------------------------------------------------------
ax3 = fig.add_subplot(223)

ax3.set_xlim((1,16))
ax3.set_ylim((3,14))
ax3.arrow(
          x=2,    #起始点x
          y=7,    #起始点y
          dx=2,  #沿x轴方向的长度;
          dy=2,  #沿y轴方向的长度
          width=0.5,        #箭头线的宽度;
          length_includes_head=True,    #如果计算长度时要计算头部，则为真。
          head_width=0.8,              #float or None, default: 3*width 全箭头的总宽度。
          head_length=0.8,              #float or None, default: 1.5*head_width, 箭头的长度
          shape="full",                    #箭头形状['full', 'left', 'right'], default: 'full']
          overhang=-0.3,                #[float, default: 0],箭头向后扫的分数（0表示三角形）。可以是负数或大于1。
          head_starts_at_zero=False, #bool,如果为True，则在坐标0处开始绘制头部，而不是在坐标0处结束。???
          
          #patch属性
          alpha=0.8,
          capstyle="butt",            # CapStyle or {'butt', 'projecting', 'round'}
          # color='r',                  #包括facecolor 和edgecolor
          edgecolor='green',        
          facecolor='r',
          fill=True,                        #bool,是否填充补丁
          gid="arrow",              #id
          hatch="o" ,                #{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
          joinstyle="round",        #JoinStyle or {'miter', 'round', 'bevel'}
          label="arrow",
          linestyle='--',           #linestyle or ls: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
          linewidth=0.2,            #linewidth or lw :float or None
          visible=True,            #bool,
          zorder=0,
          )

ax3.axhline(        #在轴上添加一条水平线
            y=5,    #y轴的位置;
            xmin=0.3,  #浮点，默认值：0; 应该在0和1之间，0是图的最左边，1是图的最右边。
            xmax=0.6,  #浮点，默认值：0; 应该在0和1之间，0是图的最左边，1是图的最右边。
            
            #line2D 属性;
            )
            
ax3.axhspan(        #添加一个方框
            ymin=8,     # float,跨度的下y坐标，以数据单位表示。
            ymax=9,     # float,跨度的下y坐标，以数据单位表示。
            xmin=0.05,   #跨度的下x坐标，以x轴（0-1）为单位。
            xmax=0.2,   #跨度的下x坐标，以x轴（0-1）为单位。
            
            #polygon 属性
            alpha=0.8,
            # color='y',
            edgecolor='b',
            facecolor='y',
            fill=True,
            gid='span',
            hatch='*',          #'/'、''、''、'-'、'+'、'X'、'O'、'O'、'、'、'*'
            linestyle='-.',       #linestyle,ls:	{'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
            linewidth=0.3,
            visible=True,
            zorder=0,
            )

ax3.axline(         #加一条无限长的直线
           xy1=(2,3),  #(float,float), 直线通过的一个点
           # xy2=(6,5),  #(float,float), 直线通过的另一个点
           slope=1.2,    #或者给定一个点+斜率
           
           #line2D 属性          
           )

ax3.axvline(    #添加一条竖直的线
            x=4,        #x轴上的坐标
            ymin=0.4,
            ymax=0.7,
            
            #Line2D属性
            c='r',
            )

ax3.axvspan(        #添加一个方框
            xmin=1.5,
            xmax=2.5,
            ymin=0.2,
            ymax=0.5,
            
            #polygon属性
            color='g',
            )

def hline01():
    ax3.hlines(         #返回值:LineCollection
               y=7,     #y轴的位置
               xmin=3,    #线的起点, 标量或数组
               xmax=7,    #线的终点
               linestyle="solid",   #线型:'solid'、'dashdot'、'dashdot'、'dotted'，可选
               
               #LineCollection属性
               color='r',
               linewidth=3,
               )
def hline02():
    ax3.hlines(         #使用data关键子参数传递数值
               y="open",     #y轴的位置
               xmin=[8,9,10],
               xmax=[11,12,13],
               linestyle='dashdot',
               
               data=data.iloc[:3,:],
               
               #LineCollection属性
               )

hline01()
hline02()

def vlines():
    ax3.vlines(
               x=[0.2,0.9],   #可以是标量,数组
               ymin=10,
               ymax=13,
               linestyle=["solid","dotted"],    #'solid'、'dashdot'、'dashdot'、'dotted'，可选
               
               # LineCollection属性
               color=['b','g'],
               )
# vlines()



plt.box(on=False)   #on:bool, 是否显示图框,类似Figure的frame_on属性


ax4 = fig.add_subplot(224)

def boxplot01():      #基本功能
    ax4.boxplot(
                [data["open"],data["close"]],         #[Array or a sequence of vectors.] The input data.数据
                # notch=True,             #bool, 是否绘制有缺口的图形
                
                vert=True,             #bool,绘制垂直的还是水平的箱型图
                # whis=(0,100),              #[float or (float, float), default: 1.5] 指定上下须与上下四分位的距离; (0,100)表示上下须就是最大值和最小值
                # positions=(1,1)          #指定箱线图的位置
                # widths=0.1,            #指定箱型图的宽度;[float or array-like]:The default is 0.5, or 0.15*(distance between extreme positions), if that is smaller.
                # patch_artist=True,      #是否填充箱体的颜色；
                labels=["tst1","tst2"],           #[sequence, optional] Labels for each dataset (one per dataset).
                # manage_ticksbool=True，  #默认值：True;则刻度位置和标签将调整以匹配方框图位置。
                meanline=True,          #bool,是否用线的形式表示均值
                
                #其他参数
                showcaps=True,          #bool,把帽子戴在胡须的末端
                showbox=True,              #bool,是否显示箱体
                showfliers=True,       #bool,是否显示异常值;
                showmeans=True,        #显示算术平均值。
                # capprops=,              #帽子的样式。
                boxprops={'color':'orangered',"linestyle":"--"},              #dict，默认值：无箱体的样式 Line2D属性; boxprops = {'color':'orangered','facecolor':'pink'}
                whiskerprops={'color':'r','alpha':0.2,'linewidth':5},
                flierprops={'linewidth':1,'alpha':0.3},
                medianprops={'color':'grey','alpha':0.3},       #中间值那根线的格式
                meanprops={'color':'yellow','alpha':0.8}
                )
boxplot01()


def boxplot02():        #关键字参数
    ax4.boxplot(
                "open",
                # "close",
                
                data = data
                )
# boxplot02()

# ax4.cla()       #清除当前轴

# plt.clf()           #清除当前的数字

# plt.close()         #关闭图形窗口


plt.show()
exit()
