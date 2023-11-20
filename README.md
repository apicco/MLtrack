# MLtrack
Machine learning algorithms and automation tools for the classification of large trajectory datasets

# Examples

There are two steps in the automation process. First, the trajectories are automatically selected. This step is detailed in the *AUTOMATED_SELECTION* folder. The output trajectories need to be verified manually. This procedure is described in the *MANUAL_VALIDATION* folder.

## Image J

The trajectories fed to the software must be tracked with the modified version of Particle Tracker (Sbalzarini and Koumoutsakos, 2005), where the different brightness moments are output. The code in the `imagej` folder should be placed into the plugins folder of your ImageJ application. 

## AUTOMATED SELECTION

The function that performs the automated selection of the trajectories is called `ichose`. This function is fed with the trajectories found by the modified version of the Particle Tracker (Sbalzarini and Koumoutsakos, 2005) software. The modified version of this software is necessary as it outputs additional moments of brightness that are key to selecting the trajectories. Under `examples/AUTOMATED_SELECTION/`, a code `analysis.py` exemplifies the use of ichose. Note that the individual trajectories in the Particle Tracker output file must be extracted with `split_pt` before passing them to `ichose`. The use of `split_pt` is commented in `analysis.py`. When you run the code for the first time, you must un-comment it. 

## MANUAL VALIDATION

In `setup.py`, define the path to the trajectories that need to be validated. In this example, the trajectories are the output of the automated selection and are under `AUTOMATED_SELECTION/SELECTED_TRAJECTORIES`. 

The software also needs to know the original movie to overlay each trajectory to its patch for validation. 


