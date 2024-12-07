import matplotlib
from matplotlib.colors import LinearSegmentedColormap
from rahrah.cmap import register_all

class Vividict(dict):
	## with thanks to https://stackoverflow.com/a/24089632
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

palettes = Vividict()

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

palettes['Harvard']['cycle'] = ['#1e1e1e', '#a51c30', '#8c8179', '#c3d7a4', '#293352', '#bac5c6']
palettes['Harvard']['cmap'] = ['#ffffff', '#a51c30']
palettes['Harvard']['ncolors'] = 6
palettes['Harvard']['maptype'] = "sequential"

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

palettes['Northwestern']['cycle'] = ['#4e2a84', '#007fa4', '#ef553f', '#008656', '#ffc520', '#0d2d6c']
palettes['Northwestern']['cmap'] = ['#ffffff', '#4e2a84']
palettes['Northwestern']['ncolors'] = 6
palettes['Northwestern']['maptype'] = "sequential"

palettes['Princeton']['cycle'] = ['#000000', '#ee7f2d', '#7f7f83', '#bdbec1']
palettes['Princeton']['cmap'] = ['#ffffff', '#ee7f2d', '#000000']
palettes['Princeton']['ncolors'] = 4
palettes['Princeton']['maptype'] = "sequential"

palettes['Stanford']['cycle'] = ['#8c1515', '#2e2d29', '#007c92', '#53565a', '#6fa287', '#5d4b3c']
palettes['Stanford']['cmap'] = ['#ffffff', '#8c1515']
palettes['Stanford']['ncolors'] = 6
palettes['Stanford']['maptype'] = "sequential"

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

palettes['Illinois']['cycle'] = ['#13294b', '#9c9a9d', '#ff5f05', '#707372']
palettes['Illinois']['cmap'] = ['#ffffff', '#ff5f05', '#13294b']
palettes['Illinois']['ncolors'] = 4
palettes['Illinois']['maptype'] = "sequential"

palettes['Indiana']['cycle'] = ['#990000', '#243142', '#ffd6db', '#ff636a']
palettes['Indiana']['cmap'] = ['#ffffff', '#990000']
palettes['Indiana']['ncolors'] = 4
palettes['Indiana']['maptype'] = "sequential"

palettes['Iowa']['cycle'] = ['#000000', '#ffcd00', '#bd472a', '#63666a']
palettes['Iowa']['cmap'] = ['#ffcd00', '#000000']
palettes['Iowa']['ncolors'] = 4
palettes['Iowa']['maptype'] = "sequential"

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

palettes['MichiganState']['cycle'] = ['#18453b', '#7bbd00', '#000000', '#008934']
palettes['MichiganState']['cmap'] = ['#ffffff', '#18453b']
palettes['MichiganState']['ncolors'] = 4
palettes['MichiganState']['maptype'] = "sequential"

palettes['Minnesota']['cycle'] = ['#7a0019', '#ffcc33', '#333333', '#777677']
palettes['Minnesota']['cmap'] = ['#ffcc33', '#7a0019']
palettes['Minnesota']['ncolors'] = 4
palettes['Minnesota']['maptype'] = "sequential"

palettes['UNC']['cycle'] = ['#7bafd4', '#13294b', '#4b9cd3', '#151515']
palettes['UNC']['cmap'] = ['#ffffff', '#78afd4']
palettes['UNC']['ncolors'] = 4
palettes['UNC']['maptype'] = "sequential"

palettes['UNCBright']['cycle'] = ['#7bafd4', '#00a5ad', '#4f758b', '#ffd100', '#ef426f', '#c4d600']
palettes['UNCBright']['cmap'] = ['#ffffff', '#7bafd4', '#13294b']
palettes['UNCBright']['ncolors'] = 4
palettes['UNCBright']['maptype'] = "sequential"

palettes['Oxford']['cycle'] = ['#002147', '#fe615a', '#789e9e', '#89827a', '#15616d', '#ed9390']
palettes['Oxford']['cmap'] = ['#ffffff', '#002147']
palettes['Oxford']['ncolors'] = 6
palettes['Oxford']['maptype'] = "sequential"

palettes['Penn']['cycle'] = ['#900000', '#011f5b', '#000000', '#f2c100']
palettes['Penn']['cmap'] = ['#011f5b', '#ffffff', '#990000']
palettes['Penn']['ncolors'] = 4
palettes['Penn']['maptype'] = "diverging"

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

