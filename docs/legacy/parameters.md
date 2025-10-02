back to [home](/)/[legacy](/legacy)

# Parameters.cfg

The XML file parameters.cfg contains the simulation setup that can be changed without the need to recompile the code.

\<file\> tag
------------

This part of the file is used by the XML reader to check the right type of file is used. It should not be modified.

\<framework\> tag
-----------------

The framework part of the contains simulation independent parameters. Except for the truncation part, everything is also independent of the geometry of the problem.

   - \<truncation\> tag:

      + Resolution of the simulation: \<dim1D\>, \<dim2D\>, \<dim3D\>. The value given is the highest index in the expansion and the first index is 0. For example 19 will compute the simulation with 20 modes. Note: in spectral space both positive and negative horizontal wavenumbers are considered, so setting  \<dim2D\> or  \<dim3D\> = 19, will generate a simulation that considers 2*19+1=39 modes.

      + For periodic directions, the box size, in units of k_c, is set by \<box2D\>, \<box3D\>

      + For periodic directions, the unit length of the box is set by \<kc2D\>, \<kc3D\>

   - \<parallel\> tag:

      Set the number of processor to be used. If a serial code has been compiled, \<cpus\> has to be 1. If a MPI code has been compiled \<cpus\> has to be at least 2. While there is no formal constain on the number of CPUs, best performance is usually achieved with a even number of CPUs. Furthermore, for a "Tubular" parallelisation the best performance is achieved with a number of CPUs that can be factorized into smaller factors.

   - \<timestepping\> tag:

      - \<time\> tag:
         
         This tags sets the initial time of the simulations. A value of zero or larger will set the initial time to the given value. A value of -1 will use the time provided in the initial state file. IMPORTANT NOTE: When converting state files to visualization files this should be set to -1, otherwise the time information in the visualization file will be wrong.

      - \<timestep\> tag:

         This tag sets the timestep to be used if it is positive. A negative value will use an adaptive timestep scheme. The absolute value of the timestep is used as the maximum allowable timestep.

     - \<error\> tag:

        For Runge-Kutta ImEx schemes with embedded lower order scheme, the error tag can be used to enable adaptive timestepping based on the computed error. This should only be enabled (other value than -1) for testing and development of the feature. It only got partial testing and there are open questions on how to best measure the error on a spectral expansion.


   - \<run\> tag:

      - \<sim\> tag:

         This tag sets the simulation time constraint. Set to 0, no simulation time constraint is imposed. A positive value will stop the simulation if the given simulation time is reached. This is NOT the wall time, it is based on the actual integration time. A negative value sets a limit on the number of timesteps.

      - \<wall\> tag:

         This tag sets the wall time of the simulation. Set to 0, there is no limit on the wall time. A positive decimal value is the wall time in hours.

   - \<io\> tag:

      - \<ascii\> tag:

         Controls the frequency of the ASCII file output. The value should be a positive integer representing the frequency in timesteps at which the ASCII files should be written.

      - \<hdf5\> tag:

         Controls the frequency of the HDF5 file output. The value should be a positive integer representing the frequency in timesteps at which the HDF5 files should be written.

   - \<statistics\> tag: 

      Statistics are currently only implemented in Cartesian plane layer geoemtry.

      - \<output_rate\> tag:

         Controls the frequency of the statistics file output.

      - \<time_avg_rate\> tag:

         Controls the rate at which time averaging is performed.

\<simulation\> tag
------------------

The simulation part depends on the simulation that is being used.

   - \<physical\> tag:
      
      This part contains the nondimensional parameters of the simulation. The meaning of the parameters should be checked in the Python model file.

   - \<boundary\> tag:
      
      This part contains the boundary condition flags of the simulation. The meaning of the values should be checked in the Python model file.
         

back to [home](/)/[legacy](/legacy)
