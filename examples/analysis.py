from trajalign.average import load_directory
from trajalign.automate import split_pt , ichose , save_directory

filename = 'Traj_image.txt'
path_trajectories = './TRAJECTORIES'

i0 = split_pt( filename , path_trajectories )

tt = load_directory( 
		path = path_trajectories , 
		pattern = '.txt$' , 
		comment_char = '%' , 
		dt = 0.5 ,
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		frames = 0 ,
		coord = ( 2 , 1 ) ,  #< note that I inverted the columns
		f = 3 , 
		u20 = 12 ,
		u02 = 11 , 
		u11 = 10 , 
		dataset = filename )

rtt = load_directory( 
		path = path_trajectories , 
		pattern = '.txt$' , 
		comment_char = '%' , 
		dt = 0.5 ,
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		frames = 0 ,
		coord = ( 2 , 1 ) ,  #< note that I inverted the columns
		f = 3 , 
		u20 = 15 ,
		u02 = 14 , 
		u11 = 13 ,
		dataset = filename )

output_tt , output_rtt = ichose( tt , rtt , ( 512 , 176 ) , 600 , fimax = False , f0 =  6 ) 

save_directory( output_tt , './SELECTED_TRAJECTORIES/' )
save_directory( output_rtt , './SELECTED_TRAJECTORIES/RTT/' )

