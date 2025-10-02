back to [home](/)/[legacy](/legacy)

# Compile

1. Get the list of available executables:
```   
  make help
```

2. Each implemented simulations (ex: BoussinesqFPlane3DQG) has 4 different executables using the same naming convention:
   - SimNameConfig: Generate a template for the required XML configuration file
   - SimNameState: Generate an initial state file
   - SimNameModel: This is the actual simulation
   - SimNameVisu: Process a state file into physical space data to be visualized

3. Configure and copy the Python modules and scripts:
```
  make install
````
  **Note:** If an MPI version of the code has been configured with CMake all executables will need to be run with the MPI wrapper (usually *mpirun*).

# Generate a configuration file

   1. Compile the "Config" executable:
      ``` 
        make -j 6 SimNameConfig #(Assuming you want 6 compilations in parallel)
      ```

   2. Generate configuration file with serial version of code:
      ```
        Executables/SimNameConfig
      ```
       or with MPI version (assuming *mpirun* is the proper wrapper for MPI):
       ```
        mpirun -n 1 Executables/SimNameConfig
      ```

   3. A new file called parameters\_template\_???.cfg has be written. ??? stands for the three letter spatial scheme name of the simulation.

   4. This template file does NOT contain usable default values and has to be edited and renamed to parameters.cfg

# Generate an initial state file

   1. Compile the "State" executable:
      ```
        make -j 6 SimNameState #(Assuming you want 6 compilations in parallel)
      ```

   2. Edit the parameters.cfg file

   3. Generate state file with serial version of the code:
      ```
       Executables/SimNameState
      ```
      or for the MPI version with 4 cores (assuming *mpirun* is the proper wrapper for MPI) :
      ```
       mpirun -n 4 Executables/SimNameState
      ```

   4. A new HDF5 file name state0000.hdf5 should have been written. It can be used as initial state for a simulation if renamed to state_initial.hdf5.

# Run a simulation

   1. compile the "Model" executable:
      ```
        make -j 6 SimNameModel #(Assuming you want 6 compilations in parallel)
      ```

   2. Edit the parameters.cfg file

   3. Provide an initial state file named state\_initial.hdf5

   4. To run the simulation, three files are required:
       1. Binary: SimNameModel
       2. Configuration file: parameters.cfg
       3. Initial state: state_initial.hdf5

   5. Run simulation with serial version of the code:
        ```
         Executables/SimNameModel
        ```
        or with MPI version with 4 cores (assuming *mpirun* is the proper wrapper for MPI) :
        ```
         mpirun -n 4 Executables/SimNameModel
        ```

# Visualize state files

   0. Make sure the \<time\> tag is set to -1. Otherwise, the visualization files can not be used to create a movie.

   1. compile the "Visu" executable:
      ```
        make -j 6 SimNameVisu #(Assuming you want 6 compilations in parallel)
      ```	

   2. Edit the parameters.cfg file

   3. Provide a state file to be converted. It has to be named state4Visu.hdf5. There is no need to copy the file a symbolic link is sufficient
      ```
        ln -s state0123.hdf5 state4Visu.hdf5
      ```

   4. Generate visualization HDF5 file with serial version of the code :
      ```
        Executables/SimNameVisu
      ```
      or with MPI version with 4 cores (assuming *mpirun* is the proper wrapper for MPI) :
      ```
        mpirun -n 4 Executables/SimNameVisu
      ```

   5. A new file named visState0000.hdf5 has been written. An additional step is required to visualize it.

### Visualization with ParaView

- To visualize a single timestep generate an XDMF file using:
  ```
    python Scripts/Python/createXDMF.py -i visState0000.hdf5 -o vis_me.xdmf
  ```

- To visualize a timeseries generate an XDMF file using:
  ```
    python Scripts/Python/createXDMF.py -i visState0000.hdf5 -n 10 -o vis_series_me.xdmf
  ```
  This command will look for files *visState0000.hdf5* through *visState0009.hdf5*.

### Visualization with Vapor

 1. Generate a NetCDF compatible HDF5 file (flat structure) and grid files
    ```
      python Scripts/Python/createVaporHDF5.py -i visState0000.hdf5 -o vaporVisState0000.hdf5
    ```

 2. Source the *vapor-setup.sh* file. 

 3. Create the VDF file
    1. *TFF* scheme 
       ```
         ncdfvdfcreate -periodic 1:1:0 -level 3 -zcoords visState0000_vapor_z.dat -gridtype stretched -ycoords visState0000_vapor_y.dat -xcoords visState0000_vapor_x.dat vaporVisState0000.hdf5 vis_me.vdf
       ```

    2. *TFT* scheme
       ```
         ncdfvdfcreate -periodic 0:1:0 -level 3 -xcoords visState0000_vapor_z.dat -ycoords visState0000_vapor_y.dat -zcoords visState0000_vapor_x.dat vaporVisState0000.hdf5 vis_me.vdf
       ```

    3. *TTT* scheme 
       ```
         ncdfvdfcreate -periodic 0:0:0 -level 3 -xcoords visState0000_vapor_z.dat -ycoords visState0000_vapor_y.dat -zcoords visState0000_vapor_x.dat vaporVisState0000.hdf5 vis_me.vdf
       ```

 4. Populate NC data
    ```
      ncdf2vdf -level 3 vaporVisState0000.hdf5 vis_me.vdf
    ```

Note: For simulations in periodic horizontal layers (such as `BoussinesqPlaneF3DQG`),  the horizontal size of the visualised box in Paraview (or VisIt) will be $`2\pi \times 2\pi`$ regardless of the size of the periodic box in which the simulation was run.

back to [home](/)/[legacy](/legacy)
