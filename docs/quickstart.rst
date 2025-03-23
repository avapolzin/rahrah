.. _rahrah.quickstart:

Quickstart Guide
================

How to use ``rahrah``:
----------------------

* **To list all palettes and their properties:**

.. code-block:: python

	from rahrah.palette import list_palettes

	list_palettes()

You can also filter for number of colors in the color cycle or type of colormap (sequential/diverging) with the arguments mincolors and maptype.

* **To list all colormaps:**

.. code-block:: python

	from rahrah.cmap import list_maps

	list_maps()


* **To set palette as default for both color cycle *and* colormap:**

.. code-block:: python

	from rahrah.palette import set_default

	set_default('Northwestern')


* **To set a palette as default for color cycle *or* colormap:**

.. code-block:: python

	from rahrah.palette import set_default_ccycle, set_default_cmap

	set_default_ccycle('ChicagoBright')

*or*

.. code-block:: python

	set_default_cmap('Yale')


* **To access colormaps without setting them as default:**

.. code-block:: python

	import matplotlib.pyplot as plt
	import rahrah.cmap

	plt.imshow(image, cmap = 'USC')

To reverse the colormap, simply append '_r' to the name (e.g., 'USC' becomes 'USC_r').

* **To access the colors in a color cycle/palette without setting a default:**

.. code-block:: python

	from rahrah.palette import return_colors

	return_colors('BrownBright')



All of the individual functions are detailed below.

.. automodule:: rahrah.palette
	:imported-members:
	:members:
	:undoc-members:
	:show-inheritance:


.. automodule:: rahrah.cmap
	:imported-members:
	:members:
	:undoc-members:
	:show-inheritance:
