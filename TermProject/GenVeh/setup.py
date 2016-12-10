from distutils.core import setup
import matplotlib.backends.backend_tkagg
import py2exe
import matplotlib
import FileDialog
import scipy
from distutils.core import setup
import numpy


setup(options={'py2exe':{"includes":["matplotlib.backends.backend_tkagg", 'scipy', 'scipy.integrate', 'scipy.special.*','scipy.linalg.*','scipy.sparse.csgraph._validation']}},
	data_files=matplotlib.get_py2exe_datafiles(),
	console=['GenVehApp.pyw']
)
