#!/usr/bin/env python
# coding: utf-8

# *hello world*

# **hello world**

# ***hello world***
# 

# ~~~hello world~~~

# test^t

# _hello_
# 

# h_m

# {h}

# In[4]:


$x_{2}$


# $x_{2}$
# 

# $x^{2}$

# **Goals for the Summer**
# 
# (1) Learn how to work in a scientific collaboration <br> (2) Learn more python (and IDL) <br> (3) Determine if I like astronomy research <br> (4) Learn more astronomy terminology <br> (5) Read more papers and try to get a better understanding of what it means and how they gathered their data

# **Goals for Week 1- May 18-23**
# 
# (1) Finish I-9 Form Nightmare <br> (2) Plot something in IDL <br> (3) Attend all of the Q3D meetings and begin to get more familiar with the project and terminology

# ***Week One Notes*** <br>
# *Monday* <br>
# Q3D Meeting; Notes on our proposal, AGN Feedback, and Quasar driven winds; Worked on the I-9 Form situation <br>
# *Tuesday* <br>
# Q3D Meeting; Notes on quasar feedback, IFS observations, infrared spectroscopy (need a better understanding); Rupke Research Meeting- goals for week/summer, questions on 2017 paper <br>
# *Wednesday* <br>
# Q3D Meeting-plotting in IDL and problems; Worked on plotting in python; Called Hadley to try to understand morning meeting <br>
# *Thursday* <br>
# Q3D Meeting- going over topics researched and IDL; RR meeting; Fixed some of the syntax errors with demonstration plot in IDL; Assigned plt.lin <br>
# *Friday* <br>
# Last Q3D Hackathon Meeting; Notes on Github submission; New Meeting time set; Doctors Appt 1:45; Attempted to begin understand plt.lin in IDL; Notes on functions of IDL such as 'set_plot' and '!P.thick' and other things that I did not understand <br>
# 

# **Week One Goals Review** 
# 
# (1) Got I-9 forms completed and submitted. Worked with Rhodes Express to get hours counted for everyday except Monday. (901)-843-3198 has been a super helpful number for issues with workday <br>
# (2) I made a simple plot in IDL work, fixed the demo to where it should work but did not run it successfully- path issue I think? <br>
# (3) Attended all hackathon meetings, Topics that were covered in Nadia Zakamska's talk and Rupke's 2017 paper were more familiar and easier to follow along with
# 

# **Goals for Week 2- May 25-30**
# 
# (1) Make progress on IDL to Python conversion of plt.lin (finish if possible?) <br>
# (2) Understand what plt.lin does in IDL/Research all of the unfamiliar functions plt.lin uses in IDL <br>
# (3) Read through Getting Started with IDL (http://hosting.astro.cornell.edu/academics/courses/astro310/IDL_Getting_Started.pdf) and take notes to gain a better understanding of IDL

# ***Week Two Notes*** <br>
# *Monday* <br>
# 
# off for Memorial Day <br>
# 
# *Tuesday* <br>
# 
# Came up with the goals for week and wrote last week's goal review, struggled with reading through the IDL code (all of the unfamiliarity felt really overwhelming), found some guides to start reading through to start making some sense of the code <br>
# **Helpful links:** <br>
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/ <br>
# http://mathesaurus.sourceforge.net/idl-numpy.html <br>
# http://www.harrisgeospatial.com/portals/0/pdfs/idl/refguide.pdf <br>
# dblarr-double precision array; strarr-string array; gt-greater than; ne- not equal to; oplot- plots new info over existing plot (cgplot/cgoplot)<br>
# 
# *Wednesday* <br>
# 
# RR meeting- The 'd's in the IDL code stand for double precision. This can be represented in python by floating points (which also have double precision). When it's written as 1d4 in IDL it means float(1 x 10^4) or float(1e4) in python. Things with the suffix 'mar' have to do with the margin. Also confirmed that the max hours allowed in a week in 35 and the max total hours is 280 (35 x 8).  Which means I currently have 14 hours to make up past the deadline <br> Q3D meeting- Using dictionary with the same tags found at the end of fitspec. Talked to Carlos about possibily downloading  WSL to upload Jupyter Notebooks to Github (creates a mac book like window not suggested by Rupke also creates issues with matlab) <br>
# **link:** https://docs.microsoft.com/en-us/windows/wsl/install-win10 <br>
# https://stackoverflow.com/questions/43397162/show-matplotlib-plots-in-ubuntu-windows-subsystem-for-linux to fix the issue <br>
# dblarr(2, nmasked) can possibly be written as np.arrange((2,nmasked), float)<br>
# 
# *Thursday* <br>
# 
# Began writing rough translation of code (with lots of questions but less than before); Felt like I had a decent understanding of the first half of the IDL code part- confusion came from translation;
# The line **pro ifsf_pltlin,instr,pltpar,outfile** appears to run these things which are then used throughout the code- python equivalant??; set tick marks with **plt.xticks(np.arrange(a,b, step=c)** where a is the starting value, b is the ending value, and c is the distance between marks. pltxtickminor for minor ticks.; **if hasattr(obj, 'attr_name'** =a possible replacement for **if tag_exist**  (A shorter day because early morning dr appt and brother's birthday) <br>
# 
# *Friday* <br>
# 
# RR meeting canceled. Some confusion cleared up about comment section. Added entire comment section to code.; IDL, python, and numpy have zero-offset indexes (start at 0) Matlab does **NOT**; There is some nested indexing in the for loops. Still doing research on this- haven't reached a solid answer yet. Took some notes on nested indexing in python will test some theories on Monday. Current at around 158 lines of code that I am not certain about but at least it's a start!

# **Week Two Goals Review** <br>
# 
# (1) Decent progress made on the translation (tried my best)<br>
# (2) I feel like I understand the first half a lot better and would've liked to look more at the second half <br>
# (3) Read through it, took notes, and it felt helpful <br>

# **Goals for Week 3- June 1-6** <br>
# (1) Finish the conversion of plt.lin<br>
# (2) Continue to research unfamiliar functions in IDL/python (maybe make into a google doc for other beginners?) <br>
# (3) Watch the Role of AGN Feedback talk, take notes and come up with 3 questions for Friday meeting <br>
# 
# additionally- try to find a solution to the jupyter notebook problem

# ***Week Three Notes*** <br>
# *Monday* <br>
# RR meeting; lct= start of an unmasked region, hct= end of an unmasked region, nct= # of unmasked regions, good regions=unmasked; in IDL instr.tag= in pythong instr['key'], talked about astrophotography :), **pro name parameter 1, parameter 2....** statements **end** = **def name (parameters):** statements **return** ; tried to figure out what was up with my github nb- only worked when I deleted the section I added <br>
# *Tuesday* <br>
# MAJOR progress on the code, for i **in** range, started to fix syntax errors <br>
# *Wednesday* <br>
# RR meeting; Q3D meeting; optional parameters in IDL are /''. This is like an on/off switch or a Boolean keyword. Can be set to =none or =true/false; Notes on the Role of AGN-Feedback in the Baryon Cycle <br>
# *Thursday* <br>
# Rewatched parts of the talk and came up with questions for Friday; struggled with a syntax error for a while (called Hadley and neither of us could figure it out); practiced using github (uploading code, creating a branch, etc); Still unclear why my jupyter notebooks don't work but got .py files to work <br>
# *Friday* <br>
# RR Meeting; Black holes out'shine' host galaxies; **Look up Edditington Ratio/Luminosity**; fixed that syntax error!!
# 
# 
# 

# **Week Two Goals Review** <br>
# 
# (1) Finished!! (not tested but all the lines are there!) <br>
# (2) Forgot about making it into a google doc- might still do this<br>
# (3) Really nice discussion of talk and the science <br>
# <br>
# as for the jupyter notebook problem- I am going to see if uploading it as a .py helps

# In[ ]:




