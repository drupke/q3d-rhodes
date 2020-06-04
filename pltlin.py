# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:41:09 2020

@author: lily
"""

import matplotlib as plt
import numpy as np
# docformat= 'rst'

#+

#Plot emission line fit and output to JPG

#Categories: IFSFIT

#Returns: None.

#Params:
#instr:in, required, type=structure
   #contains results of fit
#pltpar:in, required, type=structure
   #contains parameters to control plot
#turn this into comments?
label=np.arrange(Nlines)
label= str(label)
#line labels for plot
wave= np.arrange((Nlines), float)
#rest wavelengths of lines
lineoth= np.arrange((Notherlines, Ncomp), float)
#wavelengths of other lines to plot
int(nx) # of plot columns
int(ny) # of plot rows
#

#outfile: in, required, type=string
#Full path and name of output plot.

#Keywords:
#micron: in, optional, type=byte
#Label output plots in um rather than A. 
   #Input wavelengths still assumed to be in A.

#Author:
#  David S. N. Rupke:
#      Department of Physics
#      2000 N. Parkway
#      Memphis, TN 38104
#      drupke@gmail.com

#History:
#   ChangeHistory:
#      2009, DSNR, created
#      13sep12, DSNR, re-written
#      2013oct, DSNR, documented
#      2013nov21, DSNR, renamed, added license and copyright 
#      2015may13, DSNR, switched from using LAYOUT keyword to using CGLAYOUT
#                       procedure to fix layout issues
#      2016aug31, DSNR, added overplotting of continuum ranges masked during
#                       continuum fit with thick cyan line
#      2016sep13, DSNR, added MICRON keyword
#Copyright:
#    Copyright (C) 2013--2016 David S. N. Rupke
#
#    This program is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License or any later version.

#   This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see
#    http://www.gnu.org/licenses/.
#
#-

def ifsf_pltlin (instr, pltpar, outfile):

#in IDL this next section of code directs the output to z-buffer pseudo device
#and sets the resolution, depth, character size/thickness, line thickness
#and erases it
 defaultXtickint= Xtickinterval
 Xtickinterval= plt.xticks(step=50)
 defaultXminor=Xminor
 Xminor=plt.xminorticks(step=10)
 
 if hasattr(pltpar,'micron'):
    plt.xticks(step=0.5E4)= true;
    float(plt.xticks)
    plt.xminorticks(step=0.5E4)= true
    float(plt.xminorticks)
 if hasattr(pltpar,'meter'):
    plt.xticks(step=0.5E10)= true;
    float(plt.xticks)
    plt.xminorticks(step=0.5E10)=true
    float(plt.xminorticks)

#some stuff with margins
     
 ncomp= instr['param']
 colors= ('Magenta', 'Green', 'Orange', 'Teal')

 wave = instr['wave']
 spectot = instr['spec']
 specstars = instr['cont_dat']
 speclines = instr['emlin_dat']
 modstars = instr['cont_fit']
 modlines = instr['emlin_fit']
 modtot = modstars + modlines

#norm = max(modstars)
#spectot /= norm
#specstars /= norm
#speclines /= norm
#modtot /= norm
#modstars /= norm
#modlines /= norm

 zbase= instr['zstar']

 if hasattr (pltpar, 'micron'):
    wave=(1E4)=true
    float(wave)
 if hasattr (pltpar, 'meter'):
    wave=(1E10)=true
    float(wave)
   

#Find masked regions during continuum fit
 nmasked=0 # number of masked regions
#Find consecutive unmasked regions
 consec(instr['ct_indx'],lct,hct,nct)
#Set interior masked regions
 if nct> 1:
    nmasked= nct-1
    masklam= np.arrange((2, nmasked), float)
    for i in (0, nmasked-1):
        masklam[:i] = [wave[instr['ct_indx'[hct[i]]]],
        wave[instr['ct_indx'][lct[i+1]]]] 

#Set masked region if it occurs at beginning of lambda array
 if instr['ct_indx'][0] != 0:
      nmasked+1
      masklam = [[wave[0],wave[instr['ct_indx'][lct[0]-1]]+[masklam]]]

#Set masked region if it occurs at end of lambda array
 if instr['ct_indx'][len(instr['ct_indx'])-1 != len(instr('wave'))-1: 
      nmasked+1
      masklam= [[masklam]+[wave[instr['ct_indx'][hct[nct-1]]], wave[len(instr['wave'])]]
 nlin= len(pltpar['label'])
 linlab= pltpar['label']
 linwav= pltpar['wave']
 off= pltpar['off']

 if hasattr (pltpar, 'linoth'):
    linoth=pltpar['linoth']
 else: 
    linoth= strarr(1, nlin)

 for i in (0,nlin-1):
    linwavtmp= linwav[i]
    xran = (linwavtmp[0] + off[:i]) * (1d + zbase)
    ind = where(wave gt xran[0] AND wave lt xran[1],ct)
    cgplot,[0],/nodata,xsty=4,ysty=4,pos=pos[:i],noerase=i ne 0,backg='Black'
    xwin = [pos[0,i],pos[2,i]]
    ywin = [pos[1,i],pos[3,i]]
    dxwin = xwin[1]-xwin[0]
    dywin = ywin[1]-ywin[0]
    if ct > 0:
        pos_fit = [xwin[0],ywin[0]+0.3*dywin,xwin[1],ywin[1]]
        ydat = spectot
        ymod = modtot
        yran = [min([ydat[ind],ymod[ind]]),max([ydat[ind],ymod[ind]])]
        icol = double(i)/double(pltpar.nx)
        if icol == fix('icol'):
            ytit='Fit'
        else: ytit= ''
        cgplot ('wave', 'ydat', xran=xran, yran=yran, pos=pos_fit,
           xtickn= replicate('', 60), ytit=ytit, /noerase
           axiscol='White', col='White', /norm, /xsty, /ysty, thick=1)
         cgoplot ('wave','ymod',color='Red',thick=4)
         for j in (1,ncomp):
             flux= ifsf_cmplin('instr', 'linlab[i]','j'/velsig)
             cgoplot('wave','yran'[0]+'flux', 'color'=colors[j-1], 'linesty'=2, 'thick'=2)
    cgtext,xran[0]+(xran[1]-xran[0])*0.05d,
      yran[0]+(yran[1]-yran[0])*0.85d,
      linlab[i],charsize=1.5,charthick=2,/dat
     if nmasked > 0:
         for j in (0,nmasked-1):
             cgoplot([masklam[0,j], masklam[1,j]], [yran[0], yran[0]],thick=8, color='Cyan')
    pos_res=[xwin[0],ywin[0], xwin[1],ywin[0]+0.3*dywin]
    ydat = specstars
    ymod = modstars
    yran = [min([ydat[ind],ymod[ind]]),max([ydat[ind],ymod[ind]])]
    if icol eq fix(icol) then ytit = 'Residual' else ytit = ''
        cgplot(wave,ydat,xran=xran,yran=yran,/noerase,ytit=ytit,
        axiscol='White',col='White',/norm,pos=pos_res,/xsty,/ysty,thick=1)
        cgoplot(wave,ymod,color='Red',thick=4)
        
  if hasattr(pltpar,'micron'):
    xtit= 'Observed Wavelength ($\mu$m)'
  elif hasattr(pltpar, 'meter'):
     xtit = 'Observed Wavelength (m)'
  else: 
    xtit = 'Observed Wavelength (!3' + STRING(197B) + '!X)'
  cgtext,0.5,0.02,xtit,/norm,align=0.5,charsize=2,charthick=2
  tmpfile = outfile
  img = cgsnapshot(filename=tmpfile,/jpeg,/nodialog,quality=100)
 return
#test