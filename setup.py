import setuptools
from pathlib import Path
rahrah_home = Path(__file__).parent
pypi_descrip = (rahrah_home / "README.md").read_text()

setuptools.setup(
	name = "rahrah",
	version = "0.6.1",
	author = "Ava Polzin",
	author_email = "apolzin@uchicago.edu",
	description = "University-inspired Matplotlib palettes and colormaps.",
	packages = ["rahrah", "rahrah/palette", "rahrah/cmap"],
	url = "https://github.com/avapolzin/rahrah",
	license = "MIT",
	classifiers = [
		"Development Status :: 4 - Beta",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Programming Language :: Python"],
	python_requires = ">=3",
	install_requires = ["matplotlib"],
	long_description=pypi_descrip,
	long_description_content_type='text/markdown'
)