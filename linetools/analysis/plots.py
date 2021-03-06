""" Classes for making interactive plots.
"""
from __future__ import division, print_function, unicode_literals, absolute_import

import numpy as np
from specutils import Spectrum1D

import astropy.units as u

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib as mpl

def stack_plot(abslines, vlim=[-300,300.]*u.km/u.s, nrow=6, show=True,
               ymnx=(-0.1,1.1), figsz=(18,11)):
    """Show a stack plot of the input lines
    Assumes the data are normalized.

    Parameters
    ----------
    abslines : list
      list of AbsLine objects
    vlim : Quantities
      velocity range for the plot
    nrow : int, optional
      Maximum number of rows per column
    show : bool, optional
      Show the plot?
    ymnx : tuple, optional
      ymin, ymax
    figsz : tuple, optional
      xdim, ydim
    """
    mpl.rcParams['font.family'] = 'stixgeneral'
    mpl.rcParams['font.size'] = 15.
    # Check for spec (required)
    gdiline = []
    for iline in abslines:
        if isinstance(iline.analy['spec'], Spectrum1D):
            gdiline.append(iline)
    nplt = len(gdiline)
    if nplt == 0:
        print("Load spectra into the absline.analy['spec']")
        return
    # Setup plot
    nrow = min(nplt, nrow)
    ncol = nplt // nrow + (nplt % nrow > 0)
    # Plot
    plt.figure(figsize=figsz)
    plt.clf()

    gs = gridspec.GridSpec(nrow, ncol)

    for qq, iline in enumerate(gdiline):
        ax = plt.subplot(gs[qq % nrow, qq//nrow])
        ax.clear()
        # Plot
        velo = iline.analy['spec'].relative_vel((1+iline.attrib['z'])*iline.wrest)
        ax.plot(velo, iline.analy['spec'].flux, 'k-', linestyle='steps-mid')
        ax.plot(velo, iline.analy['spec'].sig, 'r:')
        # Lines
        ax.plot([0]*2, ymnx, 'g--')
        # Axes
        ax.set_xlim(vlim.value)
        ax.set_ylim(ymnx)
        #ax.minorticks_on()
        if ((qq+1) % nrow == 0) or ((qq+1) == nplt):
            ax.set_xlabel('Relative Velocity (km/s)')
        else:
            ax.get_xaxis().set_ticks([])
        # Label
        ax.text(0.1, 0.1, iline.data['name'], transform=ax.transAxes, ha='left', va='center')#, fontsize='large')  # , bbox={'facecolor':'white'})

    #plt.tight_layout(pad=0.2, h_pad=0., w_pad=0.1)
    if show:
        plt.show()
    plt.close()