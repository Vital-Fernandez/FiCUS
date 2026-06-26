from ficus import ficus
from pathlib import Path

fname = Path('./examples/CDFS017345.fits')
cfgfname = Path('./examples/CDFS017345.ini')

ficus(fname, z_spec=3.6052)
