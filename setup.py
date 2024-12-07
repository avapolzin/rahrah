import setuptools

setuptools.setup(
	name = "rahrah",
	version = "0.2",
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
	install_requires = ["matplotlib"]
)