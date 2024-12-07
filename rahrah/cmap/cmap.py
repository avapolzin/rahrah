import matplotlib
import matplotlib.pyplot as plt
from matplotlib import LinearSegmentedColormap

maps = {}
maps['Brown'] = ['#ffffff', '#ed1c24', '#4e3629']
maps['BrownBright'] = ['#b7b09c', '#4e3629']
maps['Thayer'] = ['#ed1c24', '#ffffff', '4e3629']
maps['Caltech'] = ['#ffffff', '#ff6c0c']
maps['CaltechBright'] = ['#00a1df', '#ffffff', '#ff6c0c']
maps['CarnegieMellon'] = ['#6d6e71', '#ffffff', '#c41230']
maps['CarnegieMellonBright'] = ['#182c4b', '#ffffff', '#941120']
maps['Columbia'] = ['#ffffff', '#b9d9eb', '#1d4f91']
maps['ColumbiaBright'] = ['#53565a', '#d0d0ce', '#ffffff', '#b9d9eb', '#1d4f91']
maps['Cornell'] = ['#ffffff', '#b31b1b']
maps['Dartmouth'] = ['#ffffff', '#00693e']
maps['DartmouthMono'] = ['#707070', '#ffffff', '#00693e']
maps['BigGreen'] = ['#ffffff', '#00693e', '#12312b', '#000000']
maps['Duke'] = ['#ffffff', '#012169']
maps['Harvard'] = ['#ffffff', '#a51c30']
maps['JohnsHopkins'] = ['#ffffff', '#68ace5', '#002d72', '#000000']
maps['JohnsHopkinsMono'] = ['#31261d', '#ffffff', '#002d72']
maps['MIT'] = ['#40464c' ,'#ffffff', '#750014']
maps['MITBright'] = ['#ffffff', '#750014']
maps['Northwestern'] = ['#ffffff', '#4e2a84']
maps['PurpleLine'] = ['#e4e0ee', '#4e2a84', '#1d0235']
maps['Princeton'] = ['#ffffff', '#ee7f2d', '#000000']
maps['Stanford'] = ['#ffffff', '#8c1515']
maps['Berkeley'] = ['#ffffff', '#fdb515', '#002676']
maps['GoBears'] = ['#fdb515', '#ffffff', '#002676']
maps['UCLA'] = ['#ffd100', '#ffffff', '#2774ae']
maps['Cambridge'] = ['#0072cf', '#ffffff', '#ef3340']
maps['Chicago'] = ['#ffffff', '#800000']
maps['ChicagoBright'] = ['#007396', '#ffffff', '#800000']
maps['Colorado'] = ['#a2a4a3', '#ffffff', '#cfb87c']
maps['Buffs'] = ['#cfb87c', '#000000']
maps['Illinois'] = ['#ffffff', '#ff5f05', '#13294b']
maps['Indiana'] = ['#ffffff', '#990000']
maps['Iowa'] = ['#ffcd00', '#000000']
maps['Maryland'] = ['#ffd200', '#ffffff', '#e21833']
maps['Terrapins'] = ['#ffffff', '#ffd200', '#e21833', '#000000']
maps['UMass'] = ['#a2aaad', '#881c1c', '#212721']
maps['UMassBright'] = ['#505759', '#ffffff', '#881c1c']
maps['Michigan'] = ['#ffcb05', '#00274c']
maps['MichiganState'] = ['#ffffff', '#18453b']
maps['Minnesota'] = ['#ffcc33', '#7a0019']
maps['UNC'] = ['#ffffff', '#78afd4']
maps['UNCBright'] = ['#ffffff', '#7bafd4', '#13294b']
maps['Oxford'] = ['#ffffff', '#002147']
maps['Penn'] = ['#011f5b', '#ffffff', '#990000']
maps['USC'] = ['#ffcc00', '#990000']
maps['Doheny'] = ['#ffcc00', '#ffffff', '#990000']
maps['Texas'] = ['#ffffff', '#bf5700']
maps['Toronto'] = ['#ffffff', '#1e3765']
maps['Yale'] = ['#ffffff', '#00356b']
maps['OrangeSt'] = ['#bd5319', '#f9f9f9', '#00356b']


##########
# * * * *
##########


def get_map(name, reverse_cmap):
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
		cmap = LinearSegmentedColormap.from_list(k, maps[k])
		cmap_r = LinearSegmentedColormap.from_list(k+"_r", maps[k][::-1])
		plt.register_cmap(cmap=cmap)
		plt.register_cmap(cmap = cmap_r)

register_all()

def list_maps():
	"""
	List all available colormaps by name. 
	"""
	
	for k in maps.keys():
		print(k)
