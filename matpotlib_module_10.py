import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

#  解决中文字体显示问题
font = {'family' : 'SimHei'};
mpl.rc('font', **font);

'''测试数据'''
filep = r".\matplotlib\testdata.csv"
data = pd.read_csv(filep,index_col=0,parse_dates=True,usecols=['trade_date','open','high','low','close'])
data.sort_index(ascending=True,inplace=True)




# 创建基图: fig = plt.figure(): 返回的是matplotlib.figure.Figure()的实例化对象(最大的artist),这个很重要,所以fig就有了Figure类的所有的属性和方法!!!!
fig = plt.figure(figsize=[12,8],dpi=100,facecolor='white',edgecolor='blue',linewidth=1,frameon=True)
# '''
# 参数:
# figsize：    default: [6.4, 4.8], Figure dimension (width, height) in inches.
# dpi：        float, default: rcParams["figure.dpi"] (default: 100.0),
             # Dots per inch.
# facecolor：  default: rcParams["figure.facecolor"] (default: 'white')
             # 画板背景颜色设置
# edgecolor：  default: rcParams["figure.edgecolor"] (default: 'white')
             # 画板边框线颜色设置
# linewidth：  float,The linewidth of the frame (i.e. the edge linewidth of the figure patch).
             # 边框线的宽度
# frameon：    bool, default: rcParams["figure.frameon"] (default: True)
            # If False, suppress drawing the figure background patch.
            # 表示是否绘制窗口的图框，如果是False，图形将完全盖住画板，即画板的颜色，边框都看不到了；
# subplotpars：SubplotParams,	Subplot parameters. If not given, the default subplot parameters rcParams["figure.subplot.*"] are used.	subplot参数
# tight_layout：bool or dict, default: rcParams["figure.autolayout"] (default: False)
                # If False use subplotpars. If True adjust subplot parameters using tight_layout with default padding. When providing a dict containing the keys pad, w_pad, h_pad, and rect, the default tight_layout paddings will be overridden.
# constrained_layout：bool
            # If True use constrained layout to adjust positioning of plot elements. Like tight_layout, but designed to be more flexible. See Constrained Layout Guide for examples. (Note: does not work with subplot() or subplot2grid().) Defaults to rcParams["figure.constrained_layout.use"] (default: False).
# '''

# plt.show()
# exit()
# ---------------------------------------
# ax = fig.add_subplot(221)
# ax_s = fig.add_subplot(222)
# ax3 = ax_s.twinx()
# -------------------------------------
# axi = fig.subplots(2,2)
# ax = axi[0,0]
# ax_s = axi[0,1]
# ---------------------------------
# fig, (ax1,ax2) = plt.subplots(1, 2)
# ax1.set_facecolor('r')
# ax2.set_facecolor('b')
# ----------------------------------
# fig,ax = plt.subplots(2, 2)
# ax[0,0].set_facecolor('r')
# ax[0,1].set_facecolor('b')
# -------------------------------------------
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# ----------------------------------------
# plt.subplot(211,facecolor='r',xlabel="plot1",ylabel='frequency',xlim=(2,4),ylim=(4,10),title="t1")
# plt.plot([1,2,3],[3,6,9])

plt.subplot(
            212,
            facecolor='b',
            xlabel="plot2",
            ylabel="frequency",
            xlim=(1,6),
            ylim=(5,100),
            
            #Axis基类的关键字参数
            adjustable='box',       #'box'、'datalim'
            # agg_filter=,            #一种过滤函数，它接受一个（m，n，3）浮点数组和一个dpi值，并返回一个（m，n，3）数组。
            alpha=0.6,  #           #浮动或无
            # anchor=,                #2-浮点数或'c'、'sw'、's'、'se'、…
            animated=False,         #布尔
            # aspect=,                #{auto}或num
            autoscale_on=False,     #布尔
            autoscalex_on=False,    #布尔
            autoscaley_on=False,    #布尔
            # axes_locator=,          #	可赎回的 [[轴，渲染器]] Bbox
            axisbelow=False,        #	布尔或“线”
            box_aspect=False,       #	没有，或者是一个数字
            # clip_box=,              #	Bbox
            clip_on=False,          #	布尔
            # clip_path=,             #	面片或（路径、变换）或无
            # contains=,              #	未知的
            c='b',                  #facecolor 或fc	颜色
            # figure=,                #	Figure
            frame_on=False,         #	布尔
            # gid=,                   #	STR
            in_layout=False,        #	布尔
            label='tst',            #	对象
            navigate=False,         #	布尔
            # navigate_mode=,         #	未知的
            # path_effects=,              #	AbstractPathEffect
            picker=None,                #	无、布尔或可呼叫
            # position=,              #	[左、下、宽、高] 或 Bbox
            # prop_cycle=,            #	未知的
            rasterization_zorder=None,  #	浮动或无
            # rasterized	布尔或无
            # sketch_params=,         #	（比例：浮动，长度：浮动，随机性：浮动）
            snap=False,             #	布尔或无
            title='tst',            #	STR
            # transform=,             #	Transform
            url='https://www.baidu.com/',   #svg格式有效
            visible=True,           #	布尔
            # xbound=,                #	未知的
            xmargin=0.3,            #	float, >-0.5
            xscale="linear",        #	“Linear”，“Log”，“SymLog”，“Logit”，…
            # xticklabels=,           #	未知的
            # xticks=,                #	未知的
            # ybound=,                #	未知的
            ymargin=0.2,            #	float, >-0.5
            yscale="Linear",        #	“Linear”，“Log”，“SymLog”，“Logit”，…
            # yticklabels=,           #	未知的
            # yticks=,                #	未知的
            zorder=2.4,             #float,
            
            
            )
# plt.plot([1,3,5],[2,30,90])



# plt.show()
exit()

def set_xxx():
    # matplotlib.figure.Figure()属性:
    '''除去set_axis_off,set_axis_on,set_axisbelow，其他去掉set_前缀都可以做为plt.subplot的参数。'''


    ax.set_alpha = 0.2
    ax.set_anchor("NE")     #实际画图区域可能比axes小,根据实际情况定义画图区域位置,
    # ax.set_animated(b=True) #Set whether the artist is intended to be used in an animation.
    # ax.set_aspect(aspect=0.5)    # 
    '''
    aspect:"auto","equal",float
        "auto": 根据数据自动调整
        "equal": 长宽相等
        float: 长宽的比例
    adjustable: [None or {'box', 'datalim'}, optional]
    '''

    ax.set_autoscale_on(b=False) #Set whether autoscaling is applied to axes on the next draw or call to Axes.autoscale_view.

    ax.set_autoscalex_on(b=True)

    ax.set_autoscaley_on(b=True)

    # ax.set_axes_locator()               #Set the axes locator.
    '''
    locator: [Callable[[Axes, Renderer], Bbox]]
    '''

    ax.set_axisbelow(b='line')        #Set whether axis ticks and gridlines are above or below most artists.
    '''
    • True (zorder = 0.5): Ticks and gridlines are below all Artists.
    • 'line' (zorder = 1.5): Ticks and gridlines are above patches (e.g. rectangles, with
    default zorder = 1) but still below lines and markers (with their default zorder
    = 2).
    • False (zorder = 2.5): Ticks and gridlines are above patches and lines / markers.
    '''

    # ax.set_box_aspect(aspect=2)     #[float or None]  axes的横竖比例,in physical units is equal to aspect. Defining a box aspect will change the adjustable property to 'datalim' 

    ax.set_clip_box([[1,2],[3,7]])

    # ax.set_clip_path()

    # ax.set_contains(picker=)

    ax.set_facecolor('w')       #ax.set_fc()    设置背景颜色

    # ax.set_figure()             #Set the Figure instance the artist belongs to.

    ax.set_frame_on(b=True)        # bool, default: True, 是否有边框,Set whether the axes rectangle patch is drawn.

    # ax.set_gid('-')                   # str, Set the (group) id for the artist.

    # ax.get_gid()        #填充设置

    ax.set_in_layout(in_layout=True)          # Set if artist is to be included in layout calculations, E.g. Constrained Layout Guide, Figure.tight_layout(), and fig.savefig(fname, bbox_inches='tight').

    ax.set_label("test")

    ax.set_xlabel("xlabel",loc="left")
    '''
    xlabel: [str] The label text.
    labelpad: [float, default: rcParams["axes.labelpad"] (default: 4.0)] Spacing in points from the axes bounding box including ticks and tick labels. If None, the previous value is left as is.
    loc:  [{'left', 'center', 'right'}, default: rcParams["xaxis.labellocation"],(default: 'center')] The label position. This is a high-level alternative for pass-ing parameters x and horizontalalignment.
    '''

    ax.set_ylabel("ylabel")

    ax.set_navigate(b=True)     # 设置轴是否响应导航工具栏命令

    # ax.set_path_effects()

    # ax.set_picker(True)
    '''
    picker
    [None or bool or float or callable] This can be one of the following:
    • None: Picking is disabled for this artist (default).
    • A boolean: If True then picking will be enabled and the artist will fire a pick
    event if the mouse event is over the artist.
    • A float: If picker is a number it is interpreted as an epsilon tolerance in points
    and the artist will fire off an event if its data is within epsilon of the mouse
    event. For some artists like lines and patch collections, the artist may provide
    additional data to the pick event that is generated, e.g., the indices of the data
    within epsilon of the pick event
    • A function: If picker is callable, it is a user supplied function which determines
    whether the artist is hit by the mouse event:

    hit, props = picker(artist, mouseevent)

    to determine the hit test. if the mouse event is over the artist, return hit=True and
    props is a dictionary of properties you want added to the PickEvent attributes.
    '''

    # ax.set_position(pos=?)

    ax.set_title("sub_ax_title",loc="left")    #设置子图名称
    '''
        labelSTR
        用于标题的文本

        fontdict双关语
        控制标题文本外观的字典，默认值 方块 是：：

        {'fontsize': rcParams['axes.titlesize'],
         'fontweight': rcParams['axes.titleweight'],
         'color': rcParams['axes.titlecolor'],
         'verticalalignment': 'baseline',
         'horizontalalignment': loc}
        loc : {{'center', 'left', 'right'}}, default: rcParams["axes.titlelocation"] (default: 'center'){'center'，'left'，'right'}，默认值：
        要设置的标题。

        y : float, default: rcParams["axes.titley"] (default: None)浮动，默认值：
        标题的垂直轴浮动（1.0为顶部）。如果没有（默认值），则自动确定y以避免轴上的装饰器。

        pad : float, default: rcParams["axes.titlepad"] (default: 6.0)浮动，默认值：
        标题与轴顶部的偏移量，以点为单位。
    '''

    # ax.set_transform(t=?)

    ax.set_url(url="https://www.baidu.com/")

    ax.set_visible(b=True)  # Set the artist's visibility

    # ax.set_xbound(lower=2,upper=8)         # Set the lower and upper numerical bounds of the x-axis.

    ax.set_xlim((-2,10),emit=False,auto=False)
    '''
    left:   [float, optional] The left xlim in data coordinates. Passing None leaves the limit unchanged.The left and right xlims may also be passed as the tuple (left, right) as the first positional argument (or as the left keyword argument).
    right:  [float, optional] The right xlim in data coordinates. Passing None leaves the limit unchanged.
    emit:   [bool, default: True] Whether to notify observers of limit change.
    auto:   [bool or None, default: False] Whether to turn on autoscaling of the x-axis. True turns on, False turns off, None leaves unchanged.
    xmin, xmax: [float, optional] They are equivalent to left and right respectively, and it is an error to pass both xmin and left or xmax and right.
    '''

    ax.set_xmargin(m=0.5)        # x轴左端再预留多少空间;Set padding of X data limits prior to autoscaling.
    '''
    m:  [float greater than -0.5]
    例如，如果数据在范围内 [0, 2] 一个因素 m = 0.1 将产生一个范围 [-0.2, 2.2] 
    负值-0.5<m<0将导致数据范围的剪切。即数据范围 [0, 2] 一个因素 m = -0.1 将产生一个范围 [0.2，1.8] .
    '''

    ax.set_xscale(value="linear")
    '''
    value:  [{"linear", "log", "symlog", "logit", ...} or ScaleBase] The axis scale type to apply.
    '''


    # set_xticklabels: 设置x轴刻度线标签,可以是任意类型的数据; 注意要赋值给变量
    '''
    labels: str列表,标签文本。

    fontdict:可选的,控制滴答标签外观的字典。默认值 方块 是：：
        {'fontsize': rcParams['axes.titlesize'],
         'fontweight': rcParams['axes.titleweight'],
         'verticalalignment': 'baseline',
         'horizontalalignment': loc}
    minor: bool，默认值：False,是否设置次要刻度线标签而不是主要刻度线标签。
    '''
    # labels = ax.set_xticklabels(labels=["one","two","three","four","five"],minor=False,rotation = 30,fontsize = 'small') # 设置刻度标签
    # ticks = ax.set_xticklabels(labels=[2,3,4,5,6,7,9.5])

    '''
    labels: [list of str] The label texts
    minor:  [bool, default: False] Whether to set the minor ticklabels rather than the major
    ones.
    '''

    # ax.set_xticks(ticks=[1,3,4,5,6,7,9.5])     # 设置刻度线,Set the xaxis' tick locations. 不会改变要显示数据对应的x轴位置;
    '''
    ticks:  [list of floats] List of tick locations.
    minor:  [bool, default: False] If False, set the major ticks; if True, the minor ticks.
    '''

    # ax_s.set_ybound(lower=1,upper=5)     # 同set_ylim;   Set the lower and upper numerical bounds of the y-axis.
    '''
    lower, upper:   [float or None] The lower and upper bounds. If None, the respective axis bound is not modified.
    '''

    # ax_s.set_ylim([3,8])    # 设置上下限

    # ax_s.set_ymargin(m=10)
    '''
    m times the data interval will be added to each end of that interval before it is used in autoscaling. For
    example, if your data is in the range [0, 2], a factor of m = 0.1 will result in a range [-0.2, 2.2].
    Negative values -0.5 < m < 0 will result in clipping of the data range. I.e. for a data range [0, 2], a
    factor of m = -0.1 will result in a range [0.2, 1.8].
    '''

    ax_s.set_yscale(value="linear")
    '''
    value:  [{"linear", "log", "symlog", "logit", ...} or ScaleBase] The axis scale type to apply.
    '''

    ax_s.set_yticklabels(["1st","2nd","3th","4th"],minor=True)     # minor=True不起作用
    '''
    labels: [list of str] The label texts.
    fontdict:
        [dict, optional] A dictionary controlling the appearance of the ticklabels. The de-
        fault fontdict is:
        {'fontsize': rcParams['axes.titlesize'],
        'fontweight': rcParams['axes.titleweight'],
        'verticalalignment': 'baseline',
        'horizontalalignment': loc}
    minor:  [bool, default: False] Whether to set the minor ticklabels rather than the major ones.
    '''

    # ax_s.set_yticks([10,20,30,40,50,60])


    # line = mlines.Line2D([2,3],[4,7],lw=3.,ls='-',alpha=1,color='red')
    # line.set_zorder(0)        #axes上多个图形时,设置它们的顺序,谁在谁上面


    # ax.plot([[1,2,3],[1.3,2.4,3.8]],[[2.5,3.6,4.9],[2,3,4]])




    plt.show()

# set_xxx()

# 所有axes的set_xxx的属性,都可以用set函数一次设置多个属性的值
def set_func():
    ax.set( 
            # adjustable="datalim",                 # axes的长高是否根据数据的limits自动调整: {'box', 'datalim'}
            alpha=0.5,                  #透明度,不支持所有后端;
            anchor="W",                 #? 啥作用?
            animated=False,             #是否用来画动态图: https://zhuanlan.zhihu.com/p/371392107
            # aspect=1,                #aspect:[{'auto', 'equal'} or float] Possible values: x轴和y轴刻度的比例;
            # autoscale_on=True,        #bool,设置是否对绘图命令应用自动缩放,见官方案例:https://www.osgeo.cn/matplotlib/gallery/event_handling/resample.html#sphx-glr-gallery-event-handling-resample-py
            # autoscalex_on=True,         #bool,自动设置坐标轴刻度的范围: https://www.lizenghai.com/archives/68020.html
            # autoscaley_on=True,
            # axes_locator= "Bbox",              #locator, [Callable[[Axes, Renderer], Bbox]],用来设置axes的位置;
            axisbelow = True,                #bool, 图上有网格线, 图是要在网格线上方,还是下方;
            # box_aspect=0.8,               #aspect=[float or None]图框的长宽比例;
            clip_box = [[0.1,0.1],[3,3]],          # 可变边界框,clipbox: [[xmin, ymin], [xmax, ymax]]或 (xmin, ymin, xmax, ymax)
            clip_on = True,                     #bool,设置艺术家是否使用剪辑。当虚假的艺术家将可见的轴以外，这可能会导致意想不到的结果。
            # clip_path = (path=?,transform=?), #设置艺术家的剪辑路径
            facecolor='white',
            frame_on = False,           # bool, axes的边框是否显示;
            gid = "testid",                 # str, 设置axes的id;图示上看不到,可以用 print(ax.get_gid())查看;
            in_layout = True,           # 设置是否将艺术家包括在布局计算中，例如 受约束的布局参考线 ， Figure.tight_layout() 和 fig.savefig(fname, bbox_inches='tight')
            # label = "high",                   #没看到在哪里显示,设置将在图例中显示的标签。可以用 print(ax.get_label())查看
            navigate = False,           #设置轴是否响应导航工具栏命令
            # navigate_mode = ,           #设置导航工具栏按钮状态；Warning: this is not a user-API function.
            # path_effect = ,             # 设置路径效果。
            # picker = ,                  #定义艺术家的采摘行为。None ：此艺术家禁用拾取（默认）。
                                            # 布尔值：如果 True 然后将启用拾取，并且如果鼠标事件位于艺术家上方，艺术家将触发拾取事件。
                                            # 一个函数：如果picker是可调用的，它是一个用户提供的函数，用于确定艺术家是否被鼠标事件击中：
                                            # hit, props = picker(artist, mouseevent)
                                            # 以确定命中测试。如果鼠标事件在艺术家上方，则返回 hit=True props是一个你想要添加到pickevent属性的属性字典。
                                            # 贬低 为了 Line2D 只是， 捡拾器 也可以是一个float，用于设置检查事件是否“在”行上发生的容差；这是不推荐使用的。使用 Line2D.set_pickradius 相反。
            # position= [100,3,3,5],          # ?设置axes的位置, pos ： [左、下、宽、高] 或 Bbox[左、下、宽、高] 或 在新的位置 Figure 协调。
                                            #which{'both'，'active'，'original'}，默认值：'both' 确定要更改的位置变量。
            rasterized = False,                  #bool,在矢量后端输出中强制栅格化（位图）绘图。
            
            title= "test",              # 见set_xxx函数,要看下rcParams
            # transform=,                 # 转换,
            visible=True,              # bool, axes是否可见;
            # xbound=("2021-04-01","2021-05-15"),
            # ybound=(0,30),              # 和ylim有点相似,adjustble参数要置为False;
            
            xlabel="Month",
            ylabel="Frequence",
            # xlim=(2,8),
            xmargin= -0.3,                   #见set_xxx函数
            # xscale="linear"                 # {"linear", "log", "symlog", "logit", ...} or ScaleBase
            # xticklabel=["one","two","three","four"], 
            # xticks = [1,3,5,7,9],           #注意与xticklabel的区别
            
            # ybound=,
            # ylabel=,
            # ylim=(0,15),
            # ymargin=,
            # yscale=,
            # yticklabels=["one","two","three","four"],   # 见set_xxx函数,
            # yticks=[1,3,5,7,9]
            )

set_func()

data[["open","close"]].plot(ax=ax)

'''
Markers

性格	描述
'.'	点标记
','	像素标记
'o'	圆标记
'v'	三角形下标记
'^'	三角形上标记
'<'	三角形标记
'>'	三角形标记
'1'	三下标记
'2'	三重标记
'3'	三左标记
'4'	三右标记
's'	方形标记
'p'	五角大厦标志
'*'	恒星标记
'h'	六角标记
'H'	六角标记
'+'	加标记
'x'	X标记
'D'	钻石标记
'd'	薄钻石标记
'|'	V线标记
'_'	线性标记

线型

性格	描述
'-'	实线样式
'--'	虚线样式
'-.'	点划线样式
':'	虚线样式
'''



# ax.text(0.2, 1.02,"low")
# prop_cycle:用于设置轴的属性周期,https://vimsky.com/examples/usage/matplotlib-axes-axes-set_prop_cycle-in-python.html
# ax.set_prop_cycle(color =['magenta', 'g', 'y', 'k'], lw =[10, 2, 3, 4]) 
'''
cycler:此参数用于设置给定的Cycler。
label:此参数是属性键。
values:此参数是属性值的finite-length迭代。
'''

# ax.set_sketch_params(): 设置草图参数
'''
scale: 可选,float,垂直于震源线的摆动幅度，以像素为单位。如果规模是 None 或未提供，将不提供草图过滤器。
length: 可选,float,沿直线摆动的长度，以像素为单位（默认为128.0）
randomness: 可选,flaot,缩小或展开长度的比例因子（默认值为16.0）
'''

# ax.set_snap():设置捕捉行为。
'''
True ：将顶点捕捉到最近的像素中心。
False ：不要修改顶点位置。
None ：（自动）如果路径只包含直线线段，则舍入到最近的像素中心。
'''


ax.xaxis.set_major_locator(DayLocator())    #设置x轴时间主刻度
ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))    #设置x轴时间次刻度
# ax.xaxis.set_major_formatter(DateFormatter('% Y-% m-% d'))



ax_s.minorticks_on()        # 次刻度,不是次坐标哦;minorticks_on()
plt.grid()          #是否显示网格线

ax_s.tick_params(
                 axis="y",            #[{'x', 'y', 'both'}, default: 'both'] The axis to which the parameters are applied.
                 which="major",          #[{'major', 'minor', 'both'}, default: 'major'] The group of ticks to which the param-eters are applied.
                 reset=False,           #[bool, default: False] Whether to reset the ticks to defaults before updating them.   
                 direction="inout",        #[{'in', 'out', 'inout'}] Puts ticks inside the axes, outside the axes, or both.
                 length=10,             #float, 刻度线的长度;
                 width=5,               #float,刻度线的宽度;
                 color='r',             #str,刻度线的颜色;
                 pad=5,                 #float, 刻度值离刻度线的距离;
                 labelsize='large',     #[float or str] 刻度值字体的大小;Tick label font size in points or as a string (e.g., 'large').
                 labelcolor='b',        #刻度值字体颜色;
                 # colors='green',        #str,刻度值和刻度线的颜色;另外两个颜色参数优先级更高;
                 zorder=1,              #刻度和刻度值(标签)叠放顺序;
                 right=True,            #bottom, top, left, right, 是否在这些遍显示对应的刻度;
                 labelright=True,       #labelbottom, labeltop, labelleft, labelright;是否在这些遍显示对应的刻度值;
                 labelrotation=45,      #float,刻度值旋转的角度;
                 grid_color='green',    #str,
                 grid_alpha=0.5,        #float,网格线透明度;
                 grid_linewidth=10,     #float,网格线的线宽;
                 grid_linestyle=':',    #线型,见 matplotlib.lines.Line2D;
                )



# fig.text(.2, .8,
         # "Both axes' location are adjusted\n"
         # "so that they have equal heights\n"
         # "while maintaining their aspect ratios",
         # va="center", ha="center",
         # bbox=dict(boxstyle="round, pad=1", facecolor="w"))
# fig.set(facecolor='r',alpha=0.1)
# ax.plot([1.3,2.4,3.8],[2.5,3.6,4.9],alpha=0.1,c='r')


# ax_s.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)

ax3 = fig.add_subplot(223)
ax3.acorr(data["close"])


plt.show()
exit()
