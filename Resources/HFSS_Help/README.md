# HFSS Help

Each lab requires you to simulate designs in HFSS. For the first few labs, you will be given pre-made HFSS files that will already have the core design, simulation setup, and result graphs that you need. For these pre-made files, you will need to input your calculated dimensions into the design parameters, run the simulation, and export the data as a .csv file. This document will provide some basic tips for running your simulation and getting the data you need for the lab reports.<br>

(Edit 3/11/2016) This document now also serves as a tutorial to model, analyze, and obtain data for original designs.

## Creating a New Design
When you open HFSS you will see a blank project in the Project Manager window. Click the blue icon in the upper left corner to 'Insert HFSS Design' to the project. You can add multiple designs to a single project as needed. Each design will have its own parameters, solutions setups, frequency sweeps, data reports, etc. Double-click on the design name in the Project Manager window to make it the active design. You may also copy and paste designs in the project, which is useful when you want to make variations on a similar design.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/New_Deisgn.png)

## Navigating the Model Space
Rotate: Hold Alt -> click and drag <br>
Pan: Hold Shift -> click and drag <br>
Zoom: Hold Alt+Shift -> click and drag OR use scroll wheel <br>
Zoom Fit: Hold Alt+Shift -> double-click <br>
Snap to View: Hold Alt -> double-click near edge of design window <br>

## Creating Objects
A new HFSS design file consists of an empty model space. HFSS will not solve for fields in the empty space, therefore it can be treated as a perfect electric conductor (PEC) since there are no fields inside it. In order to simulate something, you must model your design using 2- and 3-dimensional objects. Then, you assign materials to the objects such as FR4, Duroid 5880, PEC, Copper, Vacuum etc. This section will walk through the process of creating a microstrip line on a substrate with a region of air above it.

### Step 1: Create Box for Substrate
The substrate is modeled as a 3-D box in HFSS. Click 'Draw box' in the toolbar to enter the drawing mode (note the other 3-D shapes available in the toolbar).  Now click in three different points in the model space to set the dimensions for the box. These points can be completely random, because we will define the exact dimensions next. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Draw_Box.png)

To the left of the model space you will see a list of all of the objects in your design. Expand the branch for the box you just created and double-click on ‘CreateBox’. This brings up the model position and dimension information for the box. For boxes, the Position refers to the x,y,z coordinates of one corner of the box. The XSize, YSize, and ZSize values are the dimensions in x, y, and z from the corner referenced by Position. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Create_Box.png)

For this example, we want the substrate centered at the origin with the top surface on the XY-plane. We will use parameters to define all of the dimensions in our design so that we can easily make modifications later. Parameters are automatically created when you enter a string as a value. <br>

First, enter a string as the value for XSize, we will use ‘subx’ in this example which stands for “substrate x dimension”, but you can choose whatever name makes sense to you. When you hit Enter you will be prompted to define your newly created parameter, this value can be changed later from your parameter list. Repeat this process for the YSize and ZSize. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Create_Box_Parameters.png)

Now you can use your substrate parameters to define the Position of the box. For the Position value, enter “-subx/2,-suby/2,0”, or the equivalent with the parameter names you chose. This sets the reference corner of the box such that it is centered in X and Y. If you set the ZSize to be a negative value of the substrate height, then the box will start at z=0 and extend down from there. If you consistently use parameters to define dimensions and positions then your design will automatically adjust each object if you change the value of a parameter. Click 'OK' to close the CreateBox window and keep your changes. <br>  

Now in the sidebar double-click on the name of the box you created (‘Box1’ by default) to bring up the properties window for the object. In this window you can change the name of the object, adjust the color and transparency, and assign a material to the object. First, change the name to ‘Substrate’ or whatever makes sense to you (this is to help you keep organized when you have several objects in your design). Next, click on the drop-down value for Material and click ‘Edit’. This brings up the HFSS materials library. You can use the search bar to find a particular material, or you can add a material if it is not already in the library.<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Box_Properties.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Assign_Material.png)

<b>The FR4 in the materials library has a relative permittivity of 4.4 which is different from the FR4 we have. To change this, highlight FR4_epoxy in the list and click on ‘View/Edit Materials …’. Then, change the value of the relative permittivity to 4.1 and click ‘OK’.</b> <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Edit_Materials.png)<br>

I typically change the transparency of substrates to 0.8 to make the traces on top easier to see, but that is up to the designer. 

### Step 2: Create Rectangle for Microstrip Line
The top trace for a microstrip line is modeled as a 2-D rectangle in HFSS (could be modeled as a box if design is sensitive to metal thickness). Click 'Draw Rectangle' in the toolbar to enter the drawing mode (note the other 2-D shapes available in the toolbar).  Now click in two different points in the model space to set the dimensions for the rectangle. These points can be completely random, because we will define the exact dimensions next. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Draw_Rectangle.png)

In the object list, double-click 'CreateRectangle' under the rectangle you just created. The options here are similar to the cube except there are only 2 dimensions to define. There is also the option 'Axis' which defines the normal vector for the object, for this design Axis should be set to 'Z'. We first define the dimensions (using parameters) of the rectangle and then we set the position such that it is centered on the substrate. Notice how the position is defined as '-feed_line_width/2,-suby/2,0' and the Ysize is set to 'suby'. This ensures that if we change our 'suby' parameter, the feed line we just created will automatically resize to match the substrate dimension and remain centered. Click 'OK' to close the CreateRectangle window and keep your changes. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Create_Rectangle.png)

You can change the name, color, and transparency of the rectangle in the same way you did for the box, however, applying material properties to 2-D objects is different than for 3-D objects. This will be covered in a later step. <br>

### Step 3: Create Air Box
As mentioned before, the unassigned space in HFSS is treated as a perfect conductor. In order to truly model our microstrip line, we need to define a region of air above our substrate. This region is a 3-D box just like the substrate, but we will use the default "vacuum" material instead of assigning a material. Click on 'Draw Box' in the tool bar and click three different points to draw the box. Next, double-click on 'CreateBox' under the box you just created in the object list. The Xsize and Ysize properties should be the same as the substrate, and the Zsize should be some positive value that is about 10 times the height of the substrate (15 mm in this design). The position is also set using the substrate parameters such that the air box remains centered on the substrate. I typically make the air box completely transparent so that I can see the design inside.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Create_AirBox.png)

## Assigning Boundaries to 2-D objects

### Perfect E / Finite Conductivity
Typically, we can use ideal perfect electric conductor boundaries to model our traces. Right-click on the name of your 2-D microstrip line object in the object list and select "Assign Boundary -> Perfect E" and click 'OK' on the window that appears. You could instead use a Finite Conductivity boundary and select a material from the materials library (e.g. copper, gold, etc.) if your design requires that level of precision. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Assign_PerfectE.png)

### Radiation
We need to assign a radiation boundary to the external faces of our design. Right-click somewhere in the design space and click "Select Faces" (or just press the 'f' key). Now hold ctrl on the keyboard and click on each external face of the design except for the bottom face of the substrate (Ground Plane). Right-click and select "Assign Boundary -> Radiation" and click 'OK'on the window that appears. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Assign_Radiation.png)

## Assigning Wave Ports
In order to simulate the design, we must create/assign at least one port excitation. There are a few different types of excitations to choose from, but the most common excitation we use in this lab is the Wave Port. You can create a wave port from either an existing object face or from a new 2D object. Wave Ports must be on an external face or backed by a perfect conductor on one side. In this design we will have two Wave Ports, one on each side of the transmission line. To create the first Wave Port, draw a 2D rectangle. Rename this object to 'Port1' and open the CreateRectangle window. Change the axis to 'Y' and close and re-open the CreateRectangle window. Now the rectangle will be normal to the Y-axis and you will be able to set the Xsize and Zsize. Use parameters to set the port width and height (for example: 'portx' and 'porth') to 15mm. Change the position of the port such that the bottom edge is on the ground plane and the port is on the face of the airbox/substrate on one end of the transmission line. Follow the same steps to create 'Port2' on the opposite side of the transmission line. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Create_Port_Face.png)

Right-Click on Port1 and select "Assign Excitation -> Wave Port...". <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Assign_Waveport.png)

In the window that appears, keep the default name (should be '1', this is how the excitation will be referenced when you go to plot S-parameters and other port related results) and click Next. Under 'Integration Line' click the drop-down list and select 'New Line...', this will bring up a drawing interface to draw the integration line. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/New_Integration_Line.png)

Click on the middle of the bottom edge of the wave port (should see a triangle when you hover over the midpoint) to begin the line, then click the middle of the top edge of the wave port to finish the line. Then click Next and Finish. Do the same thing for Port2. The direction of the integration line is important for getting accurate phase results. The integration line direction should be the same for all ports, otherwise you will have a 180deg phase error. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Draw_Integration_Line.png)

## Add Solution Setup and Frequency Sweep
### Solution Setup
We need to define our solution setup with parameters such as solution frequency, maximum number of passes, and convergence criteria. Right-click on 'Analysis' in the Project Manager window and select 'Add Solution Setup...'. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Add_Solution_Setup.png)

In the window that appears, change the Solution Frequency to the design frequency (2.5 GHz in this case). Change the Maximum Number of Passes to 20 and the Maximum Delta S to 0.01. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Solution_Setup_Properties.png)

In the 'Options' tab, change the Minimum Converged Passes to 2. Click OK to close this window. The simulation will continue to run until the convergence criteria is met or until the Maximum Number of Passes is reached, whichever comes first. The convergence criteria is that the Maximum Delta S needs to be below 0.01 for 2 consecutive passes. Before we run the simulation, we need to setup a frequency sweep. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Solution_Setup_Options.png)

### Frequency Sweep
Right-click on the solution setup you just created (Setup1) in the Project Manager window and select 'Add Frequency Sweep...' <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Add_Frequency_Sweep.png)

In the window that appears, change the start and stop frequencies to 1 GHz and 5 GHz, respectively. Change the step size to 0.001 GHz. For now you may leave the Sweep Type as 'Fast', however 'Interpolating' and 'Discrete' can be more precise at the expense of longer simulation time. Click OK to close this window. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Frequency_Sweep_Properties.png)

## Running the Simulation and Checking the Progress
### Design Validation
Though it is not required, it is sometimes good to use the validation check to make sure there are no obvious errors in your design (no ports defined, no solution setup, invalid object geometry, etc.). To do this simply click the green check mark located in the toolbar. This will quickly check your design for errors and list them in the Message Manager window in the bottom-left part of the screen. If this succeeds without errors, you can run the simulation. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Validation_Check.png)

### Running the Simulation
To run the simulation, click the green exclamation point in the toolbar (located next to the green validation check mark). This will run all simulation setups associated with the current design. Alternatively, you may right-click on an individual solution setup (such as Setup1) in the Project Manager and select 'Analyze'. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Analyze_All.png)

This will start the simulation and you should see the red progress bar in the bottom-right part of the screen. To see more information about the simulation, click on the icon in the toolbar that says 'Solution Data' when you hover over it. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Solution_Data_Icon.png)

In the window that appears you will see the S Matrix at the solution frequency in (Magnitude, Phase[deg]) by default. You can also check the boxes for Gamma, Z0, Y Matrix, and Z Matrix to see the reflection coefficient, port impedance, Y Matrix, and Z Matrix, respectively. Typically, this is a good way to verify that the port impedances are approximately 50 ohms or whatever impedance you designed for. This information is updated every time a new pass is solved. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Solution_Data.png)

If you click on the 'Convergence' tab, you will see a table that has the Maximum Delta S for each pass number. According to our convergence criteria, the simulation will finish when this is below 0.01 for two consecutive passes. You can also view this information as a plot by clicking the 'Plot' button instead of 'Table'. This will graphically show you how your solution is converging. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Convergence_Data.png)

## Creating Results Plots
### Modal Solution Data: Rectangular Plot
Once the simulation has finished, you can create plots to view the results. Rectangular plots are good for plotting S-parameters and VSWR data. For now, we will plot S11 and S21 in dB. Right-click on 'Results' in the Project Manager window and select 'Create Modal Solution Data Report -> Rectangular Plot'. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Add_Results_Plot.png)

In the window that appears, select 'S parameter' under Category, then hold Ctrl and select 'S(1,1)' and 'S(2,1)' under Quantity, then select dB under Function. Then click 'New Report' to create the plot.<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Create_Report_Traces.png)

You can adjust the scale of the graph by double-clicking on one of the numbers on the y-axis. In the window that appears, click on the 'Scaling' tab. If there is no 'Scaling' tab then you probably clicked in the wrong place and it pulled up a different window. In the 'Scaling' tab check 'Specify Min', 'Specify Max', and 'Specify Spacing'. A typical scale for S-parameters in dB is a min of -40, a max of 0, and a spacing of 10. Modify these values and click OK to close the window. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Adjust_Plot_Scale.png)

You can add a marker by righ-clicking on the graph and selecting 'Marker -> Add Marker'. Click on the trace at the point you wish to add a marker. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Add_Marker.png)

A table with the list of markers will appear when you create a marker. Double-click on the marker you just created in the list to bring up its properties. Here you can change the name of the marker, the trace it corresponds to, and the frequency. Change the marker frequency to the solution frequency of 2.5 GHz to see the value at the design frequency. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Marker_Details.png)

You could also follow similar steps to plot the phase of the S-parameters, to do this you would just select 'cang_deg' under Function when creating the rectangular plot. You could also plot VSWR by selecting 'VSWR' under Category, then select which port under Quantity, and then select '<none>' under Function since it is a unit-less value. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Create_Report_Traces.png)

### Far Fields Report: Radiation Pattern
To plot the radiation pattern, you need to first define a geometry over which to plot. In this example, we will plot over the xz (phi = 0deg) and yz (phi = 90deg) cutplanes. I am using the patch antenna from Lab 9 for this demonstration since transmission lines are not designed to radiate. Right-click on 'Radiation' in the Project Manager window and select 'Insert Far Field Setup -> Infinite Sphere...'. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Insert_Far_Field_Setup.png)

In the window that appears, it is helpful to change the name of the geometry to something that you will remember later. In this example we are plotting over the xz and yz cutplanes, so I will name this 'XZ/YZ'. Now we must think about how to define the xz and yz planes in terms of phi and theta. The xz plane is equivalent to phi = 0deg and theta = [-180,180)deg. The yz plane is equivalent to phi = 90deg and theta = [-180,180)deg. Mathematically, theta is bound between 0 and 180deg, but the software allows theta to go from -180deg to 180deg or even 0deg to 360deg if you prefer. So, we can set phi to start at 0deg and stop at 90deg with a step size of 90deg. This gives us phi = 0deg,90deg. And we can set theta to start at -180deg and stop at 180deg with a step size of 1deg. This gives us theta = -180deg,-179deg,...,179deg,180deg. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Far_Field_Radiation_Sphere_Setup.png)

Now, right-click on 'Results' in the Project Manager window and select 'Create Far Fields Report -> Radiation Pattern'. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Create_Radiation_Pattern.png)

In the window that appears, make sure the geometry is set to 'XZ/YZ'. Set the Primary Sweep to 'Theta' since we want the polar graph to sweep over theta and show seperate traces for different values of phi. We will plot the phi-polarized gain and the theta-polarized gain on one graph. Select 'Gain' under Category, then hold Ctrl and select 'GainPhi' and 'GainTheta' under Quantity, then select 'dB' under Function. Click 'New Report' to create the plot. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Create_Radiation_Pattern_Traces.png)

You can change the scaling by double-clicking on the numbers on the radial axis. Make sure you are on the 'Grid' tab and scroll down until you see Min Scale, Max Scale, and Spacing. Typically, we look at radiation patterns over a 40 dB range, that is the difference between the Max and Min. So change the 'Min Scale' to '-30', the 'Max Scale' to '10', and 'Spacing' to '10'. Click OK to close this window. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Radiation_Pattern_Scaling.png)

You should see 4 different traces corresponding to GainPhi Phi=0deg, GainPhi Phi=90deg, GainTheta Phi=0deg, and GainTheta Phi=90deg. The Phi=0deg traces are for the xz plane and the Phi=90deg are for the yz plane, and theta is the variable that is swept on the polar plot with 0deg being the positive z direction. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Radiation_Pattern.png)

## Modify Design Parameters
First double-click on a design in the Project Manager window to make it the active design. Single-clicking the design name will bring up the parameter list in the Properties window below. Here you must enter the values for the physical dimensions of your design (e.g. widths and lengths of transmission lines). You should only modify parameters that pertain to your specific design, changing the substrate parameters can lead to errors in the simulation. When you have entered all of your design parameters and are ready to simulate, click on the green exclamation point ('Analyze All') to begin the simulation. 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/HFSS_Help_Slide1.png)

## View/Export Results
The pre-made HFSS files already have the graphs set up for the data that you need. To view the graphs, expand the design in the Project Manager window and expand the Results section. Here you will find the graphs of the data that you will need for the report (typically S parameters in dB). Double click on the graph names to view them. Right-click on the graph and click "Export...", then choose the file path and click OK. You will need to combine this data with calculations and z0lver data into one .csv file, then use the python program to plot the data. You will need to modify the python code to produce the required plots for a particular lab report.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/HFSS_Help_Slide2.png)

## Port De-Embedding
Since we will be using a TRL calibration when measuring our devices, it is important to use port de-embedding in our HFSS simulations so that the reference plane is the same for simulated and measured data. To de-embed a port, expand the Excitations section under the design name in the Project Manager window and click on the port number. Then, in the Properties window below, click the "Deembed" checkbox and enter the "Deembed Distance" (TRL reference plane). Repeat this for each port. 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/HFSS_DeEmbedding.png)
