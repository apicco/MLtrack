# MLtrack
Machine learning algorithms and automation tools for classification of large trajectory datasets

# Examples

There are two steps in the automation process. First, the trajectories are automatically selected. This step is detailed in the *AUTOMATED_SELECTION* folder. The output trajectories need to be verified manually. This procedure is detailed in the *MANUAL_VALIDATION* folder.

## Image J

The trajectories that are feeded to the software must be tracked with the modified version of Particle Tracker (Sbalzarini and Koumoutsakos, 2005), where also the different moments of brightness are outputed. The code, in the `imagej` folder, should be placed into the pluging folder of your ImageJ application. 

## AUTOMATED SELECTION

bla bla

## MANUAL VALIDATION

In `setup.py` define the path to the trajectories that need to be validate. In this example, the trajectories are the output of the automated selection and are under `AUTOMATED_SELECTION/SELECTED_TRAJECTORIES`. 

The software needs also to know what is the original movie to overlay each trajectory to its patch for the validation. 


