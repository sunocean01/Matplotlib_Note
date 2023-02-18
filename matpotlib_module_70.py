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
import numpy as np


'''rcParams: 
A dictionary object including validation.

Validating functions are defined and associated with rc parameters in matplotlib.rcsetup.

The list of rcParams is:

backend
backend_fallback
toolbar
interactive
timezone
webagg.port
webagg.address
webagg.open_in_browser
webagg.port_retries
lines.linewidth
lines.linestyle
lines.color
lines.marker
lines.markerfacecolor
lines.markeredgecolor
lines.markeredgewidth
lines.markersize
lines.antialiased
lines.dash_joinstyle
lines.solid_joinstyle
lines.dash_capstyle
lines.solid_capstyle
lines.dashed_pattern
lines.dashdot_pattern
lines.dotted_pattern
lines.scale_dashes
markers.fillstyle
pcolor.shading
pcolormesh.snap
patch.linewidth
patch.edgecolor
patch.force_edgecolor
patch.facecolor
patch.antialiased
hatch.color
hatch.linewidth
hist.bins
boxplot.notch
boxplot.vertical
boxplot.whiskers
boxplot.bootstrap
boxplot.patchartist
boxplot.showmeans
boxplot.showcaps
boxplot.showbox
boxplot.showfliers
boxplot.meanline
boxplot.flierprops.color
boxplot.flierprops.marker
boxplot.flierprops.markerfacecolor
boxplot.flierprops.markeredgecolor
boxplot.flierprops.markeredgewidth
boxplot.flierprops.markersize
boxplot.flierprops.linestyle
boxplot.flierprops.linewidth
boxplot.boxprops.color
boxplot.boxprops.linewidth
boxplot.boxprops.linestyle
boxplot.whiskerprops.color
boxplot.whiskerprops.linewidth
boxplot.whiskerprops.linestyle
boxplot.capprops.color
boxplot.capprops.linewidth
boxplot.capprops.linestyle
boxplot.medianprops.color
boxplot.medianprops.linewidth
boxplot.medianprops.linestyle
boxplot.meanprops.color
boxplot.meanprops.marker
boxplot.meanprops.markerfacecolor
boxplot.meanprops.markeredgecolor
boxplot.meanprops.markersize
boxplot.meanprops.linestyle
boxplot.meanprops.linewidth
font.family
font.style
font.variant
font.stretch
font.weight
font.size
font.serif
font.sans-serif
font.cursive
font.fantasy
font.monospace
text.color
text.usetex
text.latex.preamble
text.latex.preview
text.hinting
text.hinting_factor
text.kerning_factor
text.antialiased
mathtext.cal
mathtext.rm
mathtext.tt
mathtext.it
mathtext.bf
mathtext.sf
mathtext.fontset
mathtext.default
mathtext.fallback_to_cm
mathtext.fallback
image.aspect
image.interpolation
image.cmap
image.lut
image.origin
image.resample
image.composite_image
contour.negative_linestyle
contour.corner_mask
contour.linewidth
errorbar.capsize
xaxis.labellocation
yaxis.labellocation
axes.axisbelow
axes.facecolor
axes.edgecolor
axes.linewidth
axes.spines.left
axes.spines.right
axes.spines.bottom
axes.spines.top
axes.titlesize
axes.titlelocation
axes.titleweight
axes.titlecolor
axes.titley
axes.titlepad
axes.grid
axes.grid.which
axes.grid.axis
axes.labelsize
axes.labelpad
axes.labelweight
axes.labelcolor
axes.formatter.limits
axes.formatter.use_locale
axes.formatter.use_mathtext
axes.formatter.min_exponent
axes.formatter.useoffset
axes.formatter.offset_threshold
axes.unicode_minus
axes.prop_cycle
axes.autolimit_mode
axes.xmargin
axes.ymargin
axes.zmargin
polaraxes.grid
axes3d.grid
scatter.marker
scatter.edgecolors
date.epoch
date.autoformatter.year
date.autoformatter.month
date.autoformatter.day
date.autoformatter.hour
date.autoformatter.minute
date.autoformatter.second
date.autoformatter.microsecond
date.converter
date.interval_multiples
legend.fancybox
legend.loc
legend.numpoints
legend.scatterpoints
legend.fontsize
legend.title_fontsize
legend.markerscale
legend.shadow
legend.frameon
legend.framealpha
legend.borderpad
legend.labelspacing
legend.handlelength
legend.handleheight
legend.handletextpad
legend.borderaxespad
legend.columnspacing
legend.facecolor
legend.edgecolor
xtick.top
xtick.bottom
xtick.labeltop
xtick.labelbottom
xtick.major.size
xtick.minor.size
xtick.major.width
xtick.minor.width
xtick.major.pad
xtick.minor.pad
xtick.color
xtick.labelcolor
xtick.minor.visible
xtick.minor.top
xtick.minor.bottom
xtick.major.top
xtick.major.bottom
xtick.labelsize
xtick.direction
xtick.alignment
ytick.left
ytick.right
ytick.labelleft
ytick.labelright
ytick.major.size
ytick.minor.size
ytick.major.width
ytick.minor.width
ytick.major.pad
ytick.minor.pad
ytick.color
ytick.labelcolor
ytick.minor.visible
ytick.minor.left
ytick.minor.right
ytick.major.left
ytick.major.right
ytick.labelsize
ytick.direction
ytick.alignment
grid.color
grid.linestyle
grid.linewidth
grid.alpha
figure.titlesize
figure.titleweight
figure.figsize
figure.dpi
figure.facecolor
figure.edgecolor
figure.frameon
figure.autolayout
figure.max_open_warning
figure.raise_window
figure.subplot.left
figure.subplot.right
figure.subplot.bottom
figure.subplot.top
figure.subplot.wspace
figure.subplot.hspace
figure.constrained_layout.use
figure.constrained_layout.hspace
figure.constrained_layout.wspace
figure.constrained_layout.h_pad
figure.constrained_layout.w_pad
savefig.dpi
savefig.facecolor
savefig.edgecolor
savefig.orientation
savefig.jpeg_quality
savefig.format
savefig.bbox
savefig.pad_inches
savefig.directory
savefig.transparent
tk.window_focus
ps.papersize
ps.useafm
ps.usedistiller
ps.distiller.res
ps.fonttype
pdf.compression
pdf.inheritcolor
pdf.use14corefonts
pdf.fonttype
pgf.texsystem
pgf.rcfonts
pgf.preamble
svg.image_inline
svg.fonttype
svg.hashsalt
docstring.hardcopy
path.simplify
path.simplify_threshold
path.snap
path.sketch
path.effects
agg.path.chunksize
keymap.fullscreen
keymap.home
keymap.back
keymap.forward
keymap.pan
keymap.zoom
keymap.save
keymap.quit
keymap.quit_all
keymap.grid
keymap.grid_minor
keymap.yscale
keymap.xscale
keymap.all_axes
keymap.help
keymap.copy
animation.html
animation.embed_limit
animation.writer
animation.codec
animation.bitrate
animation.frame_format
animation.html_args
animation.ffmpeg_path
animation.ffmpeg_args
animation.avconv_path
animation.avconv_args
animation.convert_path
animation.convert_args
_internal.classic_mode

Set the current rcParams. group is the grouping for the rc, e.g., for lines.linewidth the group is lines, for axes.facecolor, the group is axes, and so on. Group may also be a list or tuple of group names, e.g., (xtick, ytick). kwargs is a dictionary attribute name/value pairs, e.g.,
'''

'''rc_context:Return a context manager for temporarily changing rcParams.

'''

'''rcdefaults:恢复 rcParams 来自Matplotlib的内部默认样式。
'''


filep = r".\matplotlib\stackplot_data.xlsx"
data = pd.read_excel(filep,sheet_name=0,index_col=0)
data = data.fillna(0)

# print(data)
# exit()

fig = plt.figure(figsize=(24,16))
# fig.suptitle("matplotlib_module_70 instance")
plt.suptitle("matplotlib_module_70 instance",y=1)

ax = fig.subplots(3,3)

'''setp:设置artist属性'''
line, = ax[0,0].plot("week25",data=data)

ax[0,0].tick_params(labelrotation=90)
plt.setp(line, linestyle='--')
plt.setp(line, linewidth=2, color='r')

ax[0,0].set_title('title:ax[0,0]') 
print(plt.setp(line))       #查看可设置的所有属性及其可能的值
# --------------------------------------------------------------------------
weeks = ['week24', 'week25', 'week25']

ax[0,1].stackplot(
                  data.index.tolist(),
                  data["week24"].tolist(),
                  data["week25"].tolist(),
                  data["week26"].tolist(),
                  
                  labels=weeks,
                  )

ax[0,1].tick_params(labelrotation=90)
ax[0,1].legend(loc='upper left')


# --------------------------------------------------------------------------------

'''stem:茎图,返回StemContainer 容器可以像元组一样处理（ 标记线 ， 茎线 ， 基线 ）'''
ax[0,2].stem(
             # [1,2,3,4,5,6,7,8,9,10,11],     #x类似数组，可选
             [1,2,3,4,5,6,5,4,3,2,1],       #y:类数组;
             linefmt='--',                 #定义垂直线属性的字符串。通常，这将是一种颜色或颜色和线条样式:'-':实线;'--':虚线;'-.':点划线;':':虚线;
             markerfmt='D',                #str,optional,Default: 'C0o', ;
             # basefmt="C2-",                   #str,默认值：“C3-”（经典模式下为“C2-”;定义基线属性的格式字符串。
             bottom=0.5,                      #float,default 0,基线的Y位置。
             label="stem",                  #str,default None:用于图例中的词干的标签。
             )

# ----------------------------------------------------------------------------------------
'''step:步进图; 同plot(drawstyle="steps":{'steps', 'steps-pre', 'steps-mid', 'steps-post'})'''
ax[1,0].step(
             [1,2,3,4,5,6],
             [1,1.5,2,2.5,3,3.5],
             # data=data,                 #
             where="pre",                #“pre”：Y值从 x 位置，即间隔 (x[i-1], x[i]] 具有价值 y[i] ;“post”：y值从每个 x 位置，即间隔 [x[i], x[i+1]) 具有价值 y[i]; “mid”：步骤发生在 x 位置;
             )

# ----------------------------------------------------
index = ['a','b','c','d','e']
data_bar = [1.1,3.2,6.5,3.6,2.8]

ax[1,1].bar(x=index,height=data_bar)

ax[1,1].table(
            cellText=[data_bar],                    #二维str列表，可选:要放入表格单元格中的文本。Note ：当前不考虑字符串中的换行符，这将导致文本超出单元格边界。

            cellColours=[['g','r','b','b','b']],    #二维颜色列表，可选:单元格的背景色。

            cellLoc='left',                 #{'left'、'center'、'right'}，默认值：'right':单元格内文本的对齐方式。

            # colWidths=,                 #浮动列表，可选:以轴为单位的列宽。如果未给定，则所有列的宽度将为 1 / ncols .

            rowLabels=['value1'],            #str列表，可选:行标题单元格的文本。

            rowColours=['grey'],                #颜色列表，可选:行标题单元格的颜色。

            rowLoc='left',                  #{'left'，'center'，'right'}，默认值：'left':行标题单元格的文本对齐方式。

            colLabels=index,                   #str列表，可选:列标题单元格的文本。

            # colColours=,                #颜色列表，可选:列标题单元格的颜色。

            colLoc='left',              #{'left'，'center'，'right'}，默认值：'left':列标题单元格的文本对齐方式。

            # loc=,                       #可选的STR:单元相对于 ax . 这一定是 codes .

            # bbox=,                      # ： Bbox 可选Bbox，可选:一个用来绘制表格的边界框。如果不是这样 None ，此重写 loc .

            edges="closed",                     #“BRTL”或{“open”、“closed”、“horizontal”、“vertical”}的子字符串:要用直线绘制的单元格边缘。另请参见 visible_edges .
          )


'''plt.title:默认应用于最后一个subplot'''
plt.title(
            label="plt.title:last subplot",             #str,
            # fontdict={'fontsize': rcParams['axes.titlesize'],
                         # 'fontweight': rcParams['axes.titleweight'],
                         # 'color': rcParams['axes.titlecolor'],
                         # 'verticalalignment': 'baseline',
                         # 'horizontalalignment': 'left'},                               #dict
            
            loc="left",                             #{'center', 'left', 'right'}, default: rcParams["axes.titlelocation"] (default: 'center') Which title to set.
            y=None,                                 #float, default: rcParams["axes.titley"] (default: None): Vertical Axes loation for the title (1.0 is the top). If None (the default), y is determined automatically to avoid decorators on the Axes.
            pad=6.0,                                #float, default: rcParams["axes.titlepad"] (default: 6.0):The offset of the title from the top of the Axes, in points.
            
            # Text properties:
            c='r',
            )

# -----------------------------------------------------
'''plt.violinplot():   如何要分类的话,用sns.violinplot貌似更方便;
返回值：此函數將violin-plot的每個組件的字典映射返回到各個集合實例的列表。返回的字典具有以下鍵：

bodies:matplotlib.collections.PolyCollection的實例列表，其中包含每個小提琴的填充區域。
cmeans:創建matplotlib.collections.LineCollection的實例以標識每個小提琴分布的均值
cmins:創建了matplotlib.collections.LineCollection的實例來標識每個小提琴發行的底部。
cmaxes:創建了matplotlib.collections.LineCollection的實例來標識每個小提琴發行的頂部。
cbars:創建了matplotlib.collections.LineCollection的實例來標識每個小提琴分布的中心。
cmedians:創建了matplotlib.collections.LineCollection的實例來標識每個小提琴分布的平均值。
'''


fp = r".\testfile\mc03_test01.csv"
data = pd.read_csv(fp)
data = data[data["Omega"].notna()]

ax[1,2].violinplot(
                    dataset=[data.groupby("week").get_group(23)["Omega"],data.groupby("week").get_group(24)["Omega"],data.groupby("week").get_group(25)["Omega"]],          #向量数组或向量序列。

                    # positions=,                     #类似数组，默认值： [1, 2，…，N],设置小提琴的位置。刻度和限制将自动设置为与位置匹配。

                    vert=True,                  #bool,默认值：True。如果为真，则创建垂直小提琴绘图。否则，创建一个水平小提琴绘图。

                    widths=0.5,                     #类似数组，默认值：0.5:设定每把小提琴最大宽度的标量或矢量。默认值为0.5，它使用大约一半的可用水平空间。

                    showmeans=True,                #bool，默认值：False:如果 True ，将切换方法的呈现。

                    showextrema=False,               #bool，默认值：True:如果 True ，将切换极端的渲染。

                    showmedians=True,              #bool，默认值：False:如果 True ，将切换中间带的渲染。

                    quantiles=None,                 #类似数组，默认值：无:如果不是“无”，则按间隔设置浮动列表 [0, 1] 对于每个小提琴，它代表将为该小提琴呈现的分位数。

                    points=100,                     #int，默认值：100:定义用于评估每个高斯核密度估计的点数。

                    bw_method="silverman",              #str，标量或可调用，可选:用于计算估计量带宽的方法。它可以是“scott”、“silverman”、标量常量或可调用的。如果是标量，它将直接用作 kde.factor . 如果是可调用的，则需要 GaussianKDE 实例作为其唯一参数并返回一个标量。如果没有（默认），则使用“scott”。
                    )
ax[1,2].set_xticklabels(labels=["","week23","","week24","","week25"])  #???

# plt.xticks(ticks=[1,2,3], labels=["week23","week24","week25"])


# ----------------------------------------------------------------------

# plt.subplot_tool()              #调整子图之间间距的工具
plt.subplots_adjust(
                    left=0.03,       #float, optional:The position of the left edge of the subplots, as a fraction of the figure width.

                    right=0.98,      #float, optional:The position of the right edge of the subplots, as a fraction of the figure width.

                    bottom=0.03,     #float, optional:The position of the bottom edge of the subplots, as a fraction of the figure height.

                    top=0.95,        #float, optional:The position of the top edge of the subplots, as a fraction of the figure height.

                    wspace=0.1,     #float, optional:The width of the padding between subplots, as a fraction of the average Axes width.

                    hspace=0.2,     #loat, optional:The height of the padding between subplots, as a fraction of the average Axes height.
                    )

plt.show(block=True)