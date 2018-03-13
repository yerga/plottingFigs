#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Short description of this Python module.
Longer description of this module.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Daniel Martin-Yerga"
__email__ = "dyerga@gmail.com"
__copyright__ = "Copyright 2018"
__date__ = "13/03/18"
__license__ = "GPLv3"
__program__ = "plotSciFigs"
__version__ = "0.0.1"

import matplotlib as mpl
mpl.use("Qt5Agg")
from plotstyle import PlotStyle
import matplotlib.pyplot as plt
from extractdata import ExtractData
from lineplot import LinePlot

class Plotting():
    def __init__(self, config, plotsconfig):

        self.nplots, self.singlecolumn, self.verticalplot, self.plotstyle = config

        if self.verticalplot:
            self.singlecolumn = True

        plotstyle = PlotStyle(self.singlecolumn, self.nplots, self.verticalplot, self.plotstyle)
        _params = plotstyle.get_params()
        mpl.rc_context(rc=_params)

        fig, axnumber = self.createFigure()

        #self.plottype, self.filename, self.xlabel1, self.ylabel1, self.xlabel2, self.ylabel2, self.legends = plotsconfig

        for nplot in range(self.nplots):
            print("printing plot: ", nplot + 1)
            plottype = plotsconfig[nplot][0]
            plotfilename = plotsconfig[nplot][1]
            print("filename: ", plotfilename)

            plotdata = self.getPlotData(plottype, plotfilename)

            try:
                naxis = axnumber[nplot]
            except TypeError:
                naxis = axnumber

            plot = self.plotPlot(plottype, plotdata, plotsconfig[nplot], naxis)



        # TODO: remove when creating customized figures
        plt.tight_layout()

        # plt.savefig('test2.png', format='png')
        plt.show()


    def getPlotData(self, plottype, plotfilename):
        exdata = ExtractData(plottype, plotfilename)
        #xdata, ydata, xdata2, ydata2
        plotdata = exdata.get_data()
        #TODO: normalize Y, area elctrodica, unidades, etc.

        return plotdata


    def plotPlot(self, plottype, plotdata, plotconfig, axis):
        xdata1, ydata1, xdata2, ydata2 = plotdata

        #TODO: double axis
        doubleaxis = True

        if plottype == "LinePlot":
            lineplot = LinePlot(doubleaxis, plotconfig)
            lineplot.plot(axis, plotdata)


    def createFigure(self):

        #TODO: create special 2x2 singlecolumn figures; 2+1 single column figures, etc.

        # fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
        # axnumber = [ax1, ax2, ax3, ax4]

        if self.nplots == 1:
            fig, axnumber = plt.subplots(1, 1)
        elif self.nplots == 2:
            if self.verticalplot:
                fig, axnumber = plt.subplots(2, 1)
            else:
                fig, axnumber = plt.subplots(1, 2)
        elif self.nplots == 3:
            if self.verticalplot:
                fig, axnumber = plt.subplots(3, 1)

                # TODO: create customized figures
                # fig = plt.figure()
                # ax1 = fig.add_axes([0.2, .72, .6, .25])
                # ax2 = fig.add_axes([0.08, .34, .85, .32])
                # ax3 = fig.add_axes([0.08, .01, .85, .32])
                # axnumber = [ax1, ax2, ax3]
            else:
                fig, axnumber = plt.subplots(1, 3)
                # fig = plt.figure()
                # ax1 = fig.add_axes([0.07, .21, .25, .75])
                # ax2 = fig.add_axes([0.33, .21, .25, .75])
                # ax3 = fig.add_axes([0.66, .02, .35, .95])
                # axnumber = [ax1, ax2, ax3]

        elif self.nplots == 4:
            if self.verticalplot:
                fig, axnumber = plt.subplots(4, 1)
            else:
                fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
                axnumber = [ax1, ax2, ax3, ax4]

        return fig, axnumber
