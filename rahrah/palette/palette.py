import matplotlib
from matplotlib.colors import LinearSegmentedColormap
from rahrah.cmap import register_all

class Vividict(dict):
	## with thanks to https://stackoverflow.com/a/24089632
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

palettes = Vividict()

palettes['Albion']['cycle'] = ['#4b306a', '#ffc845', '#00747a', '#8cc8e6', '#333333', '#cccccc']
palettes['Albion']['cmap'] = ['#4b306a', '#ffc845']
palettes['Albion']['ncolors'] = 6
palettes['Albion']['maptype'] = "sequential"

palettes['Amherst']['cycle'] = ['#3f1f69', '#0099bc', '#505061', '#df723d', '#458246', '#b7a5d3']
palettes['Amherst']['cmap'] = ['#ffffff', '#3f1f69']
palettes['Amherst']['ncolors'] = 6
palettes['Amherst']['maptype'] = "sequential"

palettes['ASU']['cycle'] = ['#8c1d40', '#ffc627', '#000000', '#747474', '#4ab7c4', '#af674b']
palettes['ASU']['cmap'] = ['#ffc627', '#8c1d40', '#000000']
palettes['ASU']['ncolors'] = 6
palettes['ASU']['maptype'] = "sequential"

palettes['Bowdoin']['cycle'] = ['#00506a', '#730051', '#955021', '#9b2822', '#1d5c57', '#687c2f']
palettes['Bowdoin']['cmap'] = ['#ffffff', '#000000']
palettes['Bowdoin']['ncolors'] = 6
palettes['Bowdoin']['maptype'] = "sequential"

palettes['Brown']['cycle'] = ['#4e3629', '#ed1c24', '#98a4ae', '#ffc72c']
palettes['Brown']['cmap'] = ['#ffffff', '#ed1c24', '#4e3629']
palettes['Brown']['ncolors'] = 4
palettes['Brown']['maptype'] = "sequential"

palettes['BrownBright']['cycle'] = ['#4e3629', '#ed1c24', '#b7b09c', '#00b398', '#ffc72c', '#59cbe8']
palettes['BrownBright']['cmap'] = ['#b7b09c', '#4e3629']
palettes['BrownBright']['ncolors'] = 6
palettes['BrownBright']['maptype'] = "sequential"

palettes['Caltech']['cycle'] = ['#76777b', '#ff6c0c', '#849895', '#c8c8c8']
palettes['Caltech']['cmap'] = ['#ffffff', '#ff6c0c']
palettes['Caltech']['ncolors'] = 4
palettes['Caltech']['maptype'] = "sequential"

palettes['CaltechBright']['cycle'] = ['#003b4c', '#ff6c0c', '#00a1df', '#644b78', '#e41937', '#849895']
palettes['CaltechBright']['cmap'] = ['#00a1df', '#ffffff', '#ff6c0c']
palettes['CaltechBright']['ncolors'] = 6
palettes['CaltechBright']['maptype'] = "diverging"

palettes['CarnegieMellon']['cycle'] = ['#c41230', '#000000', '#6d6e71', '#e0e0e0']
palettes['CarnegieMellon']['cmap'] = ['#6d6e71', '#ffffff', '#c41230']
palettes['CarnegieMellon']['ncolors'] = 4
palettes['CarnegieMellon']['maptype'] = "diverging"

palettes['CarnegieMellonBright']['cycle'] = ['#941120', '#6d6e71', '#719f94', '#182c4b', '#bcb49e', '#1f4c4c']
palettes['CarnegieMellonBright']['cmap'] = ['#182c4b', '#ffffff', '#941120']
palettes['CarnegieMellonBright']['ncolors'] = 6
palettes['CarnegieMellonBright']['maptype'] = "diverging"

palettes['CUNY']['cycle'] = ['#0033a1', '#ffb71b', '#011d49', '#a3c9ff']
palettes['CUNY']['cmap'] = ['#0033a1', '#ffb71b']
palettes['CUNY']['ncolors'] = 4
palettes['CUNY']['maptype'] = "sequential"

palettes['Colgate']['cycle'] = ['#821019', '#e10028', '#000000', '#5a646e']
palettes['Colgate']['cmap'] = ['#821019', '#ffffff']
palettes['Colgate']['ncolors'] = 4
palettes['Colgate']['maptype'] = "sequential"

palettes['Columbia']['cycle'] = ['#b9d9eb', '#d0d0ce', '#1d4f91', '#75787b']
palettes['Columbia']['cmap'] = ['#ffffff', '#b9d9eb', '#1d4f91']
palettes['Columbia']['ncolors'] = 4
palettes['Columbia']['maptype'] = "sequential"

palettes['ColumbiaBright']['cycle'] = ['#b9d9eb', '#75787b', '#ae2573', '#d0d0ce', '#ff9800', '#76881d']
palettes['ColumbiaBright']['cmap'] = ['#53565a', '#d0d0ce', '#ffffff', '#b9d9eb', '#1d4f91']
palettes['ColumbiaBright']['ncolors'] = 6
palettes['ColumbiaBright']['maptype'] = "diverging"

palettes['Cornell']['cycle'] = ['#222222', '#b31b1b', '#006699', '#9fad9f']
palettes['Cornell']['cmap'] = ['#ffffff', '#b31b1b']
palettes['Cornell']['ncolors'] = 4
palettes['Cornell']['maptype'] = "sequential"

palettes['Dartmouth']['cycle'] = ['#00693e', '#8a6996', '#d94415', '#267aba', '#707070', '#ffa00f']
palettes['Dartmouth']['cmap'] = ['#ffffff', '#00693e']
palettes['Dartmouth']['ncolors'] = 6
palettes['Dartmouth']['maptype'] = "sequential"

palettes['DartmouthMono']['cycle'] = ['#0d1e1c', '#00693e', '#707070', '#c4dd88', '#e2e2e2', '#a5d75f']
palettes['DartmouthMono']['cmap'] = ['#707070', '#ffffff', '#00693e']
palettes['DartmouthMono']['ncolors'] = 6
palettes['DartmouthMono']['maptype'] = "diverging"

palettes['Duke']['cycle'] = ['#012169', '#dad0c6', '#666666', '#e2e6ed']
palettes['Duke']['cmap'] = ['#ffffff', '#012169']
palettes['Duke']['ncolors'] = 4
palettes['Duke']['maptype'] = "sequential"

palettes['GeorgiaTech']['cycle'] = ['#b3a369', '#003057', '#d6dbd4', '#54585a', '#eaaa00', '#008c95']
palettes['GeorgiaTech']['cmap'] = ['#ffffff', '#b3a369']
palettes['GeorgiaTech']['ncolors'] = 6
palettes['GeorgiaTech']['maptype'] = "sequential"

palettes['GSU']['cycle'] = ['#0039a6', '#1c272d', '#0d9ddb', '#cc0000']
palettes['GSU']['cmap'] = ['#ffffff', '#0039a6']
palettes['GSU']['ncolors'] = 4
palettes['GSU']['maptype'] = "sequential"

palettes['Harvard']['cycle'] = ['#1e1e1e', '#a51c30', '#8c8179', '#c3d7a4', '#293352', '#bac5c6']
palettes['Harvard']['cmap'] = ['#ffffff', '#a51c30']
palettes['Harvard']['ncolors'] = 6
palettes['Harvard']['maptype'] = "sequential"

palettes['HarveyMudd']['cycle'] = ['#000000', '#fdb913', '#007fa3', '#5b6770']
palettes['HarveyMudd']['cmap'] = ['#000000', '#fdb913', '#ffffff']
palettes['HarveyMudd']['ncolors'] = 4
palettes['HarveyMudd']['maptype'] = "sequential"

palettes['Haverford']['cycle'] = ['#8b0000', '#000000', '#cccccc', '#5da423', '#666666', '#2ba6cb']
palettes['Haverford']['cmap'] = ['#000000', '#8b0000', '#ffffff']
palettes['Haverford']['ncolors'] = 6
palettes['Haverford']['maptype'] = "sequential"

palettes['Indiana']['cycle'] = ['#990000', '#243142', '#ffd6db', '#ff636a']
palettes['Indiana']['cmap'] = ['#ffffff', '#990000']
palettes['Indiana']['ncolors'] = 4
palettes['Indiana']['maptype'] = "sequential"

palettes['JohnsHopkins']['cycle'] = ['#002d72', '#cf4520', '#76a04c', '#ff9e1b', '#a45c98', '#68ace5']
palettes['JohnsHopkins']['cmap'] = ['#ffffff', '#68ace5', '#002d72', '#000000']
palettes['JohnsHopkins']['ncolors'] = 6
palettes['JohnsHopkins']['maptype'] = "sequential"

palettes['JohnsHopkinsMono']['cycle'] = ['#31261d', '#68ace5', '#002d72', '#0077d8']
palettes['JohnsHopkinsMono']['cmap'] = ['31261d', '#ffffff', '#002d72']
palettes['JohnsHopkinsMono']['ncolors'] = 4
palettes['JohnsHopkinsMono']['maptype'] = "diverging"

palettes['MIT']['cycle'] = ['#750014', '#8b959e', '#000000', '#ff1423']
palettes['MIT']['cmap'] = ['#40464c', '#ffffff', '#750014']
palettes['MIT']['ncolors'] = 4
palettes['MIT']['maptype'] = "diverging"

palettes['MITBright']['cycle'] = ['#750014', '#8b959e', '#1966ff', '#00ad00', '#bfb3ff', '#ff1423']
palettes['MITBright']['cmap'] = ['#ffffff', '#750014']
palettes['MITBright']['ncolors'] = 6
palettes['MITBright']['maptype'] = "sequential"

palettes['Middlebury']['cycle'] = ['#0d395f', '#aaa59f', '#fdd16d', '#4c4b4c']
palettes['Middlebury']['cmap'] = ['#0d395f', '#ffffff']
palettes['Middlebury']['ncolors'] = 4
palettes['Middlebury']['maptype'] = "sequential"

palettes['McGill']['cycle'] = ['#ed1b2f', '#999999', '#27bdbe', '#44c8f5', '#b2d235', '#c768a9']
palettes['McGill']['cmap'] = ['#ffffff', '#ed1b2f']
palettes['McGill']['ncolors'] = 6
palettes['McGill']['maptype'] = "sequential"

palettes['MichiganState']['cycle'] = ['#18453b', '#7bbd00', '#000000', '#008934']
palettes['MichiganState']['cmap'] = ['#ffffff', '#18453b']
palettes['MichiganState']['ncolors'] = 4
palettes['MichiganState']['maptype'] = "sequential"

palettes['NCState']['cycle'] = ['#cc0000', '#000000', '#6f7d1c', '#4156a1', '#d14905', '#008473']
palettes['NCState']['cmap'] = ['#000000', '#cc0000', '#ffffff']
palettes['NCState']['ncolors'] = 6
palettes['NCState']['maptype'] = "sequential"

palettes['NMSU']['cycle'] = ['#8c0b42', '#ededed', '#cfc7bd', '#a7babe']
palettes['NMSU']['cmap'] = ['#8c0b42', '#ffffff']
palettes['NMSU']['ncolors'] = 4
palettes['NMSU']['maptype'] = "sequential"

palettes['NYU']['cycle'] = ['#57068c', '#eee6f3', '#8900e1', '#000000']
palettes['NYU']['cmap'] = ['#57068c', '#ffffff']
palettes['NYU']['ncolors'] = 4
palettes['NYU']['maptype'] = "sequential"

palettes['NIU']['cycle'] = ['#c8102e', '#000000', '#a5a7a8', '#d0df00']
palettes['NIU']['cmap'] = ['#000000', '#c8102e', '#ffffff']
palettes['NIU']['ncolors'] = 4
palettes['NIU']['maptype'] = "sequential"

palettes['Northwestern']['cycle'] = ['#4e2a84', '#007fa4', '#ef553f', '#008656', '#ffc520', '#0d2d6c']
palettes['Northwestern']['cmap'] = ['#ffffff', '#4e2a84']
palettes['Northwestern']['ncolors'] = 6
palettes['Northwestern']['maptype'] = "sequential"

palettes['NotreDame']['cycle'] = ['#0c2340', '#ae9142', '#0a843d', '#1c4f8f']
palettes['NotreDame']['cmap'] = ['#0c2340', '#ae9142']
palettes['NotreDame']['ncolors'] = 4
palettes['NotreDame']['maptype'] = "sequential"

palettes['Oberlin']['cycle'] = ['#a6192e', '#e81727', '#ffc72c', '#585252']
palettes['Oberlin']['cmap'] = ['#ffc72c', '#e81727']
palettes['Oberlin']['ncolors'] = 4
palettes['Oberlin']['maptype'] = "sequential"

palettes['OhioState']['cycle'] = ['#ba0c2f', '#a7b1b7', '#6bbbab', '#70071c']
palettes['OhioState']['cmap'] = ['#a7b1b7', '#ffffff', '#ba0c2f']
palettes['OhioState']['ncolors'] = 4
palettes['OhioState']['maptype'] = "diverging"

palettes['OregonState']['cycle'] = ['#d73f09', '#000000', '#c6dae7', '#d3832b', '#0d5257', '#8e9089']
palettes['OregonState']['cmap'] = ['#ffffff', '#d73f09', '#000000']
palettes['OregonState']['ncolors'] = 6
palettes['OregonState']['maptype'] = "sequential"

palettes['PennState']['cycle'] = ['#1e407c', '#96bee6', '#001c3a', '#5f2a24']
palettes['PennState']['cmap'] = ['#ffffff', '#1e407c']
palettes['PennState']['ncolors'] = 4
palettes['PennState']['maptype'] = "sequential"

palettes['Princeton']['cycle'] = ['#000000', '#ee7f2d', '#7f7f83', '#bdbec1']
palettes['Princeton']['cmap'] = ['#ffffff', '#ee7f2d', '#000000']
palettes['Princeton']['ncolors'] = 4
palettes['Princeton']['maptype'] = "sequential"

palettes['Purdue']['cycle'] = ['#cfb991', '#000000', '#daaa00', '#9d9795']
palettes['Purdue']['cmap'] = ['#000000', '#cfb991']
palettes['Purdue']['ncolors'] = 4
palettes['Purdue']['maptype'] = "sequential"

palettes['QUB']['cycle'] = ['#d6000d', '#9b9b9b', '#8f0e20', '#4a4a4a']
palettes['QUB']['cmap'] = ['#d6000d','#ffffff']
palettes['QUB']['ncolors'] = 4
palettes['QUB']['maptype'] = "sequential"

palettes['QUBBright']['cycle'] = ['#d6000d', '#00afab', '#94d604', '#672e6c', '#00a1e1', '#f18903']
palettes['QUBBright']['cmap'] = ['#d6000d', '#ffffff', '#00afab']
palettes['QUBBright']['ncolors'] = 6
palettes['QUBBright']['maptype'] = "diverging"

palettes['Reed']['cycle'] = ['#a70e16', '#000000', '#7e8a65', '#dfe7e7', '#e84a37', '#3f6574']
palettes['Reed']['cmap'] = ['#eceae4', '#a70e16', '#000000']
palettes['Reed']['ncolors'] = 6
palettes['Reed']['maptype'] = "sequential"

palettes['Rutgers']['cycle'] = ['#cc0033', '#000000', '#00626d', '#007fac', '#ebb600', '#666666']
palettes['Rutgers']['cmap'] = ['#ffffff', '#cc0033', '#000000']
palettes['Rutgers']['ncolors'] = 6
palettes['Rutgers']['maptype'] = "sequential"

palettes['Stanford']['cycle'] = ['#8c1515', '#2e2d29', '#007c92', '#53565a', '#6fa287', '#5d4b3c']
palettes['Stanford']['cmap'] = ['#ffffff', '#8c1515']
palettes['Stanford']['ncolors'] = 6
palettes['Stanford']['maptype'] = "sequential"

palettes['StonyBrook']['cycle'] = ['#990000', '#000000', '#1791ad', '#828282', '#f1ea86', '#104247']
palettes['StonyBrook']['cmap'] = ['#000000', '#990000', '#bebebe']
palettes['StonyBrook']['ncolors'] = 6
palettes['StonyBrook']['maptype'] = "sequential"

palettes['Syracuse']['cycle'] = ['#f76900', '#000e54', '#eb3300', '#f2a900']
palettes['Syracuse']['cmap'] = ['#000e54', '#f76900','#ffffff']
palettes['Syracuse']['ncolors'] = 4
palettes['Syracuse']['maptype'] = "sequential"

palettes['Arizona']['cycle'] = ['#ab0520', '#0c234b', '#378dbd', '#f4ede5', '#a95c42', '#007d84']
palettes['Arizona']['cmap'] = ['#ab0520', '#ffffff', '#0c234b']
palettes['Arizona']['ncolors'] = 6
palettes['Arizona']['maptype'] = "diverging"

palettes['UBC']['cycle'] = ['#002145', '#6ec4e8', '#0055b7', '#00a7e1']
palettes['UBC']['cmap'] = ['#002145', '#ffffff']
palettes['UBC']['ncolors'] = 4
palettes['UBC']['maptype'] = "sequential"

palettes['Berkeley']['cycle'] = ['#002676', '#808080', '#fdb515', '#770747', '#010133', '#c09748']
palettes['Berkeley']['cmap'] = ['#ffffff', '#fdb515', '#002676']
palettes['Berkeley']['ncolors'] = 6
palettes['Berkeley']['maptype'] = "sequential"

palettes['UCLA']['cycle'] = ['#2774ae', '#ffd100', '#003b5c', '#8bb8e8', '#ffb81c', '#005587']
palettes['UCLA']['cmap'] = ['#ffd100', '#ffffff', '#2774ae']
palettes['UCLA']['ncolors'] = 6
palettes['UCLA']['maptype'] = "diverging"

palettes['Cambridge']['cycle'] = ['#d6083b', '#0072cf', '#ea7125', '#55a51c', '#8f2bbc', '#00b1c1']
palettes['Cambridge']['cmap'] = ['#0072cf', '#ffffff', '#ef3340']
palettes['Cambridge']['ncolors'] = 6
palettes['Cambridge']['maptype'] = "diverging"

palettes['Chicago']['cycle'] = ['#737373', '#800000', '#a6a6a6', '#d9d9d9']
palettes['Chicago']['cmap'] = ['#ffffff', '#800000']
palettes['Chicago']['ncolors'] = 4
palettes['Chicago']['maptype'] = "sequential"

palettes['ChicagoBright']['cycle'] = ['#800000', '#3eb1c8', '#59315f', '#de7c00', '#737373', '#275d38']
palettes['ChicagoBright']['cmap'] = ['#007396', '#ffffff', '#800000']
palettes['ChicagoBright']['ncolors'] = 6
palettes['ChicagoBright']['maptype'] = "diverging"

palettes['Colorado']['cycle'] = ['#000000', '#cfb87c', '#565a5c', '#a2a4a3']
palettes['Colorado']['cmap'] = ['#a2a4a3', '#ffffff', '#cfb87c']
palettes['Colorado']['ncolors'] = 4
palettes['Colorado']['maptype'] = "diverging"

palettes['UConn']['cycle'] = ['#000e2f', '#7c878e', '#004369', '#64c7c9']
palettes['UConn']['cmap'] = ['#ffffff', '#000e2f']
palettes['UConn']['ncolors'] = 4
palettes['UConn']['maptype'] = "sequential"

palettes['Idaho']['cycle'] = ['#f1b300', '#191919', '#808080', '#827655']
palettes['Idaho']['cmap'] = ['#191919', '#f1b300']
palettes['Idaho']['ncolors'] = 4
palettes['Idaho']['maptype'] = "sequential"

palettes['Illinois']['cycle'] = ['#13294b', '#9c9a9d', '#ff5f05', '#707372']
palettes['Illinois']['cmap'] = ['#ffffff', '#ff5f05', '#13294b']
palettes['Illinois']['ncolors'] = 4
palettes['Illinois']['maptype'] = "sequential"

palettes['Iowa']['cycle'] = ['#000000', '#ffcd00', '#bd472a', '#63666a']
palettes['Iowa']['cmap'] = ['#ffcd00', '#000000']
palettes['Iowa']['ncolors'] = 4
palettes['Iowa']['maptype'] = "sequential"

palettes['Kansas']['cycle'] = ['#0051ba', '#e8000d', '#ffc82d', '#85898a']
palettes['Kansas']['cmap'] = ['#e8000d', '#ffc82d', '#0051ba']
palettes['Kansas']['ncolors'] = 4
palettes['Kansas']['maptype'] = "diverging"

palettes['Kentucky']['cycle'] = ['#0033a0', '#ffa360', '#1b365d', '#4cbcc0', '#ffdc00', '#1e8aff']
palettes['Kentucky']['cmap'] = ['#ffffff', '#0033a0']
palettes['Kentucky']['ncolors'] = 6
palettes['Kentucky']['maptype'] = "sequential"

palettes['Maryland']['cycle'] = ['#e21833', '#ffd200', '#e6e6e6', '#000000']
palettes['Maryland']['cmap'] = ['#ffd200', '#ffffff', '#e21833']
palettes['Maryland']['ncolors'] = 4
palettes['Maryland']['maptype'] = "diverging"

palettes['UMass']['cycle'] = ['#881c1c', '#212721', '#a2aaad', '#505759']
palettes['UMass']['cmap'] = ['#a2aaad', '#881c1c', '#212721']
palettes['UMass']['ncolors'] = 4
palettes['UMass']['maptype'] = "sequential"

palettes['UMassBright']['cycle'] = ['#881c1c', '#212721', '#86c8bc', '#5e4b3c', '#00aec7', '#505759']
palettes['UMassBright']['cmap'] = ['#505759', '#ffffff', '#881c1c']
palettes['UMassBright']['ncolors'] = 6
palettes['UMassBright']['maptype'] = "diverging"

palettes['Michigan']['cycle'] = ['#00274c', '#ffcb05', '#655a52', '#75988d', '#575294', '#00b2a9']
palettes['Michigan']['cmap'] = ['#ffcb05', '#00274c']
palettes['Michigan']['ncolors'] = 6
palettes['Michigan']['maptype'] = "sequential"

palettes['Minnesota']['cycle'] = ['#7a0019', '#ffcc33', '#333333', '#777677']
palettes['Minnesota']['cmap'] = ['#ffcc33', '#7a0019']
palettes['Minnesota']['ncolors'] = 4
palettes['Minnesota']['maptype'] = "sequential"

palettes['Nebraska']['cycle'] = ['#d00000', '#f5f1e7', '#c7c8ca', '#249ab5']
palettes['Nebraska']['cmap'] = ['#f5f1e7', '#d00000']
palettes['Nebraska']['ncolors'] = 4
palettes['Nebraska']['maptype'] = "sequential"

palettes['UNC']['cycle'] = ['#7bafd4', '#13294b', '#4b9cd3', '#151515']
palettes['UNC']['cmap'] = ['#ffffff', '#78afd4']
palettes['UNC']['ncolors'] = 4
palettes['UNC']['maptype'] = "sequential"

palettes['UNCBright']['cycle'] = ['#7bafd4', '#00a5ad', '#4f758b', '#ffd100', '#ef426f', '#c4d600']
palettes['UNCBright']['cmap'] = ['#ffffff', '#7bafd4', '#13294b']
palettes['UNCBright']['ncolors'] = 4
palettes['UNCBright']['maptype'] = "sequential"

palettes['Oregon']['cycle'] = ['#007030', '#fee11a', '#004f6e', '#a2aaad', '#8d1d58', '#4d5859']
palettes['Oregon']['cmap'] = ['#fee11a', '#007030']
palettes['Oregon']['ncolors'] = 6
palettes['Oregon']['maptype'] = "sequential"

palettes['Oxford']['cycle'] = ['#002147', '#fe615a', '#789e9e', '#89827a', '#15616d', '#ed9390']
palettes['Oxford']['cmap'] = ['#ffffff', '#002147']
palettes['Oxford']['ncolors'] = 6
palettes['Oxford']['maptype'] = "sequential"

palettes['Penn']['cycle'] = ['#900000', '#011f5b', '#000000', '#f2c100']
palettes['Penn']['cmap'] = ['#011f5b', '#ffffff', '#990000']
palettes['Penn']['ncolors'] = 4
palettes['Penn']['maptype'] = "diverging"

palettes['Pitt']['cycle'] = ['#003594', '#ffb81c', '#c8c9c7', '#00205b', '#b87333', '#dbeeff']
palettes['Pitt']['cmap'] = ['#003594', '#ffb81c']
palettes['Pitt']['ncolors'] = 6
palettes['Pitt']['maptype'] = "sequential"

palettes['USC']['cycle'] = ['#000000', '#990000', '#ffcc00', '#908c13']
palettes['USC']['cmap'] = ['#ffcc00', '#990000']
palettes['USC']['ncolors'] = 4
palettes['USC']['maptype'] = "sequential"

palettes['Texas']['cycle'] = ['#bf5700', '#00a9b7', '#005f86', '#9cadb7', '#d6d2c4', '#333f48']
palettes['Texas']['cmap'] = ['#ffffff', '#bf5700']
palettes['Texas']['ncolors'] = 6
palettes['Texas']['maptype'] = "sequential"

palettes['Toronto']['cycle'] = ['#1e3765', '#d0d1c9', '#007894', '#000000']
palettes['Toronto']['cmap'] = ['#ffffff', '#1e3765']
palettes['Toronto']['ncolors'] = 4
palettes['Toronto']['maptype'] = "sequential"

palettes['Utah']['cycle'] = ['#be0000', '#000000', '#708e99', '#3abfc0']
palettes['Utah']['cmap'] = ['#ffffff', '#be0000']
palettes['Utah']['ncolors'] = 4
palettes['Utah']['maptype'] = "sequential"

palettes['UVA']['cycle'] = ['#232d4b', '#c8cbd2', '#e57200', '#f9dcbf']
palettes['UVA']['cmap'] = ['#f9dcbf', '#232d4b']
palettes['UVA']['ncolors'] = 4
palettes['UVA']['maptype'] = "sequential"

palettes['Washington']['cycle'] = ['#32006e', '#b7a57a', '#2ad2c9', '#ffc700']
palettes['Washington']['cmap'] = ['#85754d', '#ffffff', '#4b2e83']
palettes['Washington']['ncolors'] = 4
palettes['Washington']['maptype'] = "diverging"

palettes['Wisconsin']['cycle'] = ['#9b0000', '#e6e6e6', '#333333', '#0479a8']
palettes['Wisconsin']['cmap'] = ['#f7f7f7', '#9b0000']
palettes['Wisconsin']['ncolors'] = 4
palettes['Wisconsin']['maptype'] = "sequential"

palettes['Vanderbilt']['cycle'] = ['#cfae70', '#1c1c1c', '#b3c9cd', '#ecb748', '#946e24', '#8ba18e']
palettes['Vanderbilt']['cmap'] = ['#1c1c1c', '#cfae70']
palettes['Vanderbilt']['ncolors'] = 6
palettes['Vanderbilt']['maptype'] = "sequential"

palettes['Wellesley']['cycle'] = ['#0142a4', '#0c2142', '#f15623', '#1b9de5']
palettes['Wellesley']['cmap'] = ['#0142a4', '#ffffff']
palettes['Wellesley']['ncolors'] = 4
palettes['Wellesley']['maptype'] = "sequential"

palettes['WVU']['cycle'] = ['#eaaa00', '#002855', '#988e8b', '#0062a3']
palettes['WVU']['cmap'] = ['#002855', '#eaaa00']
palettes['WVU']['ncolors'] = 4
palettes['WVU']['maptype'] = "sequential"

palettes['Yale']['cycle'] = ['#00356b', '#bd5319', '#978d85', '#5f712d', '#63aaff', '#ffd55a']
palettes['Yale']['cmap'] = ['#ffffff', '#00356b']
palettes['Yale']['ncolors'] = 6
palettes['Yale']['maptype'] = "sequential"


register_all()

##########
# * * * *
##########

def list_palettes(mincolors = False, maptype = False, verbose = False):
    """
    List all available palettes by name. Optionally filter for color cycle and colormap properties.

    Parameters:
        mincolors (int): Minimum number of colors in color cycle. Use this to filter the available palettes. Default is no minimum.
        maptype (str): Either "sequential" or "diverging". Use this to filter the available palettes. Default is no preference for colormap type.
        verbose (bool): Default is False. Enables printing of additional information.

    Returns:
        The list of available palettes (that match search criteria).
    """
    
    for k in covers.keys():
        if not mincolors and not maptype:
            if verbose:
                print(k, palettes[k]['cycle'], palettes[k]['maptype'] + 'colormap')
            if not verbose:
                print(k)
        if mincolors and not maptype:
            if palettes[k]['ncolors'] >= mincolors:
                if verbose:
                    print(k, palettes[k]['cycle'], palettes[k]['maptype'] + 'colormap')
                if not verbose:
                    print(k)
        if maptype and not mincolors:
            if palettes[k]['maptype'] == maptype:
                if verbose:
                    print(k, palettes[k]['cycle'], palettes[k]['maptype'] + 'colormap')
                if not verbose:
                    print(k)
        if mincolors and maptype:
            if (palettes[k]['ncolors'] >= mincolors) & (palettes[k]['maptype'] == maptype):
                if verbose:
                    print(k, palettes[k]['cycle'], palettes[k]['maptype'] + 'colormap')
                if not verbose:
                    print(k)




def set_default(palette, verbose = False, reverse_cmap = False):
    """
    Set palette as default colormap and color cycle.

    Parameters:
        palette (str): Name of palette to set as default.
        verbose (bool): Default is False. Enables printing of additional information about the color cycle.
        reverse_cmap (bool/str): Default is False. To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., set_default('LondonCalling', 'reverse').
    """

    matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=palettes[palette]['cycle']) 
    if not reverse_cmap:
        matplotlib.rcParams['image.cmap'] = palette
    if reverse_cmap:
        matplotlib.rcParams['image.cmap'] = palette+"_r"
    if verbose:
        print("Cycled colors in %s are: "%(palette) + palettes[palette]['cycle'].values)



def set_default_cmap(palette, reverse_cmap = False):
    """
    Set palette as default colormap.

    Parameters:
            palette (str): Name of palette to set as default.
            reverse_cmap (bool/str): Default is False. To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., set_default('LondonCalling', 'reverse').
    """

    if not reverse_cmap:
        matplotlib.rcParams['image.cmap'] = palette
    if reverse_cmap:
        matplotlib.rcParams['image.cmap'] = palette+"_r"


def set_default_ccycle(palette, verbose = False):
    """
    Set palette as default color cycle.

    Parameters:
        palette (str): Name of palette to set as default.
        verbose (bool): Default is False. Enables printing of additional information about the color cycle.
    """

    # matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=palettes['palette'][palettes['name'] == palette]['cycle']) 
    # if verbose:
    #   print("Cycled colors in %s are: "%(palette) + palettes['palette'][palettes['name'] == palette]['cycle'].values)

    matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=palettes[palette]['cycle'])
    if verbose:
        print("Cycled colors in %s are: "%(palette) + palettes[palette]['cycle'].values)


def return_colors(palette):
    """
    Return colors in a particular palette's color cycle.

    Parameters:
            palette (str): Name of palette.
    """

    return palettes[palette]['cycle']

