#!/usr/bin/env python

"""
Enable continuum fitting of an input spectrum
"""
import pdb
import sys


# Script to run continuum fitting in linetools
def main(*args, **kwargs):
    """ Runs the continuum fitter
    """
    import argparse

    parser = argparse.ArgumentParser(description='Fit a continuum to a spectrum')
    parser.add_argument("file", type=str, help="Spectral file")
    parser.add_argument("outfil", type=str, help="Output file [can be the same]")
    parser.add_argument("--redshift", type=float, help="Redshift of the Source")
    parser.add_argument("--wchunk", type=float, help="Width of a 'chunk' (Ang)")
    #parser.add_argument("-exten", type=int, help="FITS extension")

    pargs = parser.parse_args()


    from linetools.guis.xspecgui import XSpecGui
    from linetools.spectra import io as lsio

    # Read spectrum
    xspec = lsio.readspec(pargs.file)

    kwrds = {}
    if pargs.wchunk is not None:
        kwrds['dw'] = pargs.wchunk

    # Redshift
    if pargs.redshift is not None:
        kwrds['kind'] = 'QSO'
        kwrds['redshift'] = pargs.redshift

    # Run
    print("WARNING: QUIT with q keystroke, not by clicking to kill.")
    xspec.fit_continuum(**kwrds)

    # Output
    xspec.write_to_fits(pargs.outfil)
