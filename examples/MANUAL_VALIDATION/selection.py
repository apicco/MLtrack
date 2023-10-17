# append parent directory for testing mltrack
# these two lines should be commented if mltrack
# is properly installed
import sys
sys.path.append( '../../' )

from mltrack.ctrlfuns import icheck
from trajalign.average import load_directory

# load trajectories
path_trajectories = '../AUTOMATED_SELECTION/SELECTED_TRAJECTORIES/'

tts = load_directory(
		path = path_trajectories ,
		pattern = '.txt$' ,
		comment_char = '#' , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		t = 1 ,
		coord = ( 2 , 3 ) , 
		f = 4  )

# run the icheck to control manually the 
# trajectories selected by ichose
icheck( 
	tts ,
	path_movie = '../Image/image_large.tif' ,
	path_output = 'MANUAL_SELECTION' ,
	r = 20 , 
    cmap = 'viridis' ,
    marker = '+', 
    offset = (  - 0.5 ,  - 0.5 ) , 
    buffer_frames = 5  ) 
