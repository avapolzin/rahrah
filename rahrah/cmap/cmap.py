import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

maps = {}
maps['Albion'] = ['#4b306a', '#ffc845']
maps['Amherst'] = ['#ffffff', '#3f1f69']
maps['ASU'] = ['#ffc627', '#8c1d40', '#000000']
maps['Bowdoin'] = ['#ffffff', '#000000']
maps['Brown'] = ['#ffffff', '#ed1c24', '#4e3629']
maps['BrownBright'] = ['#b7b09c', '#4e3629']
maps['Thayer'] = ['#ed1c24', '#ffffff', '#4e3629']
maps['Caltech'] = ['#ffffff', '#ff6c0c']
maps['CaltechBright'] = ['#00a1df', '#ffffff', '#ff6c0c']
maps['CarnegieMellon'] = ['#6d6e71', '#ffffff', '#c41230']
maps['CarnegieMellonBright'] = ['#182c4b', '#ffffff', '#941120']
maps['CUNY'] = ['#0033a1', '#ffb71b']
maps['Colgate'] = ['#821019', '#ffffff']
maps['Columbia'] = ['#ffffff', '#b9d9eb', '#1d4f91']
maps['ColumbiaBright'] = ['#53565a', '#d0d0ce', '#ffffff', '#b9d9eb', '#1d4f91']
maps['Cornell'] = ['#ffffff', '#b31b1b']
maps['Dartmouth'] = ['#ffffff', '#00693e']
maps['DartmouthMono'] = ['#707070', '#ffffff', '#00693e']
maps['BigGreen'] = ['#ffffff', '#00693e', '#12312b', '#000000']
maps['Duke'] = ['#ffffff', '#012169']
maps['GeorgiaTech'] = ['#ffffff', '#b3a369']
maps['GSU'] = ['#ffffff', '#0039a6']
maps['Harvard'] = ['#ffffff', '#a51c30']
maps['HarveyMudd'] = ['#000000', '#fdb913', '#ffffff']
maps['Haverford'] = ['#000000', '#8b0000', '#ffffff']
maps['Indiana'] = ['#ffffff', '#990000']
maps['JohnsHopkins'] = ['#ffffff', '#68ace5', '#002d72', '#000000']
maps['JohnsHopkinsMono'] = ['#31261d', '#ffffff', '#002d72']
maps['MIT'] = ['#40464c' ,'#ffffff', '#750014']
maps['MITBright'] = ['#ffffff', '#750014']
maps['Middlebury'] = ['#0d395f', '#ffffff']
maps['McGill'] = ['#ffffff', '#ed1b2f']
maps['MichiganState'] = ['#ffffff', '#18453b']
maps['NCState'] = ['#000000', '#cc0000', '#ffffff']
maps['NMSU'] = ['#8c0b42', '#ffffff']
maps['NYU'] = ['#57068c', '#ffffff']
maps['NIU'] = ['#000000', '#c8102e', '#ffffff']
maps['Northwestern'] = ['#ffffff', '#4e2a84']
maps['PurpleLine'] = ['#e4e0ee', '#4e2a84', '#1d0235']
maps['NotreDame'] = ['#0c2340', '#ae9142']
maps['Oberlin'] = ['#ffc72c', '#e81727']
maps['OhioState'] = ['#a7b1b7', '#ffffff', '#ba0c2f']
maps['OregonState'] = ['#ffffff', '#d73f09', '#000000']
maps['PennState'] = ['#ffffff', '#1e407c']
maps['Princeton'] = ['#ffffff', '#ee7f2d', '#000000']
maps['Purdue'] = ['#000000', '#cfb991']
maps['QUB'] = ['#d6000d','#ffffff']
maps['QUBBright'] = ['#d6000d', '#ffffff', '#00afab']
maps['Reed'] = ['#eceae4', '#a70e16', '#000000']
maps['Rutgers'] = ['#ffffff', '#cc0033', '#000000']
maps['Stanford'] = ['#ffffff', '#8c1515']
maps['StonyBrook'] = ['#000000', '#990000', '#bebebe']
maps['Syracuse'] = ['#000e54', '#f76900','#ffffff']
maps['Arizona'] = ['#ab0520', '#ffffff', '#0c234b']
maps['UBC'] = ['#002145', '#ffffff']
maps['Berkeley'] = ['#ffffff', '#fdb515', '#002676']
maps['GoBears'] = ['#fdb515', '#ffffff', '#002676']
maps['UCLA'] = ['#ffd100', '#ffffff', '#2774ae']
maps['Cambridge'] = ['#0072cf', '#ffffff', '#ef3340']
maps['Chicago'] = ['#ffffff', '#800000']
maps['ChicagoBright'] = ['#007396', '#ffffff', '#800000']
maps['Colorado'] = ['#a2a4a3', '#ffffff', '#cfb87c']
maps['Buffs'] = ['#cfb87c', '#000000']
maps['UConn'] = ['#ffffff', '#000e2f']
maps['Idaho'] = ['#191919', '#f1b300']
maps['Illinois'] = ['#ffffff', '#ff5f05', '#13294b']
maps['Iowa'] = ['#ffcd00', '#000000']
maps['Kansas'] = ['#e8000d', '#ffc82d', '#0051ba']
maps['Maryland'] = ['#ffd200', '#ffffff', '#e21833']
maps['Terrapins'] = ['#ffffff', '#ffd200', '#e21833', '#000000']
maps['UMass'] = ['#a2aaad', '#881c1c', '#212721']
maps['UMassBright'] = ['#505759', '#ffffff', '#881c1c']
maps['Michigan'] = ['#ffcb05', '#00274c']
maps['Minnesota'] = ['#ffcc33', '#7a0019']
maps['Nebraska'] = ['#f5f1e7', '#d00000']
maps['UNC'] = ['#ffffff', '#78afd4']
maps['UNCBright'] = ['#ffffff', '#7bafd4', '#13294b']
maps['Oregon'] = ['#fee11a', '#007030']
maps['Oxford'] = ['#ffffff', '#002147']
maps['Penn'] = ['#011f5b', '#ffffff', '#990000']
maps['Pitt'] = ['#003594', '#ffb81c']
maps['USC'] = ['#ffcc00', '#990000']
maps['Doheny'] = ['#ffcc00', '#ffffff', '#990000']
maps['Texas'] = ['#ffffff', '#bf5700']
maps['Toronto'] = ['#ffffff', '#1e3765']
maps['Utah'] = ['#ffffff', '#be0000']
maps['UVA'] = ['#f9dcbf', '#232d4b']
maps['Washington'] = ['#85754d', '#ffffff', '#4b2e83']
maps['Dubs'] = ['#ffffff', '#b7a57a', '#32006e']
maps['Wisconsin'] = ['#f7f7f7', '#9b0000']
maps['Vanderbilt'] = ['#1c1c1c', '#cfae70']
maps['Wellesley'] = ['#0142a4', '#ffffff']
maps['WellesleyBlue'] = ['#0c2142', '#0142a4', '#ffffff']
maps['WVU'] = ['#002855', '#eaaa00']
maps['Yale'] = ['#ffffff', '#00356b']
maps['OrangeSt'] = ['#bd5319', '#f9f9f9', '#00356b']


##########
# * * * *
##########


def get_map(name, reverse_cmap = False):
	"""
	Access colormaps.

	Parameters:
		name (str): Name of colormap.
		reverse_cmap (str): Default is False.
	"""

	if not reverse_cmap:
		cmap = LinearSegmentedColormap.from_list(name, maps[name])
	if reverse_cmap:
		cmap = LinearSegmentedColormap.from_list(name+"_r", maps[name][::-1])
	return cmap


def register_all():
	"""
	Register all of the colormaps.
	"""


	for k in maps.keys():
		if k not in matplotlib.pyplot.colormaps():
			cmap = LinearSegmentedColormap.from_list(k, maps[k])
			matplotlib.colormaps.register(cmap=cmap)
		if k+"_r" not in matplotlib.pyplot.colormaps():
			cmap_r = LinearSegmentedColormap.from_list(k+"_r", maps[k][::-1])
			matplotlib.colormaps.register(cmap = cmap_r)

register_all()

def list_maps():
	"""
	List all available colormaps by name. 
	"""
	
	for k in maps.keys():
		print(k)
