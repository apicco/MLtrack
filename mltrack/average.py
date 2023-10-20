# All the software here is distributed under the terms of the GNU General Public License Version 3, June 2007. 
# Trajalign is a free software and comes with ABSOLUTELY NO WARRANTY.
# 
# You are welcome to redistribute the software. However, we appreciate is use of such software would result in citations of 
# Picco, A., Kaksonen, M., _Precise tracking of the dynamics of multiple proteins in endocytic events_,  Methods in Cell Biology, Vol. 139, pages 51-68 (2017)
# http://www.sciencedirect.com/science/article/pii/S0091679X16301546
# 
# Author: Andrea Picco (https://github.com/apicco)
# Year: 2017

import os 
from mltrack.traj import Traj
import copy as cp
import numpy as np
import warnings as wr

from sklearn import linear_model

def load_directory(path , pattern = '.txt' , sep = None , comment_char = '#' , dt = None , t_unit = '' , coord_unit = '' , intensity_normalisation = 'None' , fill_trajectory = True , **attrs ):

	"""
	load_directory(path , pattern = '.txt' , sep = None , comment_char = '#' , dt = None , t_unit = '' , coord_unit = '' , intensity_normalisation = 'None' , **attrs ):
	loads all the trajectories listed in 'path', which have the same 'pattern'.
	columns are separated by 'sep' (default is None: a indefinite number of 
	white spaces). Comments in the trajectory start with 'comment_char'.
	
	intensity_normalisation can be: 'None' (no normalisation, default), 'Integral' (normalise over the integral of the fluorescence intensity), 
	or 'Absolute' (normalise the fluorescence intensity values between 0 and 1)"

	**attrs is used to assign columns to the trajectory attributes and to 
	add annotations. 
	If the time interval is added (and 't' is not called in the **attrs) 
	then the time column 't' is added, and the 't_unit' can be set.
	If 'coord' is called then the unit must be added.
	fill_trajectory = True (default) fills missing frames with nan
	"""

	if ('coord' in attrs.keys()) & (len(coord_unit) == 0): 
		raise AttributeError('Please, specify the coordinate unit \'coord_unit\'')
	if ('t' in attrs.keys()) & (len(t_unit) == 0): 
		raise AttributeError('Please, specify the time unit \'t_unit\'')
	if (dt != None) & (len(t_unit) == 0): 
		raise AttributeError('Please, specify the time unit \'t_unit\'')
	if (dt != None) & ('t' in attrs.keys()):
		raise AttributeError('Time is already loaded by the trajectories, you cannot also compute it from frames. Please, either remove the dt option or do not load the \'t\' column from the trajectories')

	trajectories = [] #the list of trajectories
	if ( pattern[ len( pattern ) - 1 ] == '$' ) : 
		files = [ f for f in os.listdir(path) if f.endswith( pattern[ : - 1 ] ) ] #list all the files in path that have pattern
	else : 
		files = [ f for f in os.listdir(path) if pattern in f] #list all the files in path that have pattern

	print( 'Loading of trajectory files' )
	for file in files:

		trajectory = Traj(experiment = path, path = os.getcwd()+'/'+path)
		trajectory.load(path+'/'+file,sep = sep, comment_char = comment_char, **attrs)
		if (dt != None):
			trajectory.time(dt,t_unit)
		if ('coord' in attrs.keys()):

			trajectory.annotations('coord_unit',coord_unit)

		if intensity_normalisation == 'Integral' :
			
			trajectory.scale_f()

		elif intensity_normalisation == 'Absolute' :
		
			trajectory.norm_f()

		elif intensity_normalisation != 'None' :

			raise AttributeError( "load_directory: Please, choose a value for the variable intensity_normalisation between 'None' (no normalisation, default), 'Integral' (normalise over the integral of the fluorescence intensity), or 'Absolute' (normalise the fluorescence intensity values between 0 and 1)" )

		trajectory.annotations( 'intensity_normalisation' , intensity_normalisation )
		if fill_trajectory : trajectory.fill()
		trajectories.append(trajectory)
	
	print( "\n >> load_directory: The 'intensity_normalisation' applied to the trajectories is '" + intensity_normalisation + "' <<\n" )

	print( 'Loading of trajectory files ended' )
	return trajectories 
