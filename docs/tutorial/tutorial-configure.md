back to [home](/)/[tutorial](/tutorial)

# Prerequisites

For the non linear solver, you need to install the following libraries on your system:

- HDF5
- FFTW
- UmfPack

And for the linear solver, you need

- SLEPc, PETSc 

install petsc with complex numbers enabled: ./configure --with-scalar-type=complex
```
export SLEPC_DIR=/opt/slepc/linux-c-opt
export PETSC_DIR=/opt/petsc/linux-c-opt
```

- and their python bindings slepsc4py, petsc4py 
```
pip install mpi4py --user
pip install petsc4py --user
pip install slepc4py --user
```
Note: you shouldn't have to reinstall slepc and petsc at this stage. (make sure SLEPC_DIR and PETSC_DIR are defined)

# Prerequisites (Optional)

-OpenMPI
-MUMPS 

# Preliminary steps on Janus (soon to be decommissioned)

- On Janus, the Configuration and Compile steps are best performed on the compilation nodes:

```
ssh janus-compile1
```

- If you have a recent account (for sure not created before October 2016) the following command may needed to be entered to access the modules needed for configuring/compiling the code

```
/curc/tools/utils/switch_lmod.sh -r
```

- Environmental modules needs to be loaded to satisfy the above mentioned pre-requisites. The following works for Janus (with GCC as compiler and for compiling the code with openmpi)  

```
module load cmake
module load intel/intel-13.0.0
module load python/anaconda-2.0.0
module load gcc/gcc-4.9.1
module load openmpi/openmpi-1.8.2_gcc-4.9.1
module load hdf5/hdf5-1.8.13_szip-2.1_zlib-1.2.8_jpeglib-9a_openmpi-1.8.2_gcc-4.9.1
module load fftw/fftw-3.3.4_openmpi-1.8.2_gcc-4.9.1_double
```

- Algebra libraries are linked in (assuming the QuICC folder has been cloned in myself's home)

```
/home/myself/QuICC/cmake.d/platforms/Janus.cmake
```

One should check that the sparse linear algebra libraries are all linked correctly or the Configuration step is not going to work.

# Preliminary steps on Summit

After having cloned or pulled the latest version of QuICC:

1. Login to Summit. That is, login on the rc.colorado.edu login node and then `ssh scompile1` 
2. Install SuiteSparse libraries:

    a. grab the latest stable version of the libraries from, e.g., `http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-4.5.4.tar.gz `

    b. load the modules `intel`, `impi`, `mkl` and `cmake`

    c. untar the SuiteSparse repository, go in the directory and build with the following command:
        `make MKLROOT=${CURC_MKL_ROOT} BLAS="-L $CURC_MKL_ROOT/lib/intel64 -lmkl_intel_lp64 -lmkl_core -lmkl_intel_thread -lpthread -lm" LAPACK=''`
        hat builds the code and runs through some tests.  It puts the library files in SuiteSparse/lib and include files in SuiteSparse/include.  Note that after LAPACK above, it is two single quotes with no space in between (LAPACK is coming through MKL, which is already linked in place of BLAS).
3. Change the file `cmake.d/platforms/Summit.cmake` so that the SuiteSparse is correctly linked. At the moment the file points at the libraries in `/home/mica5951/QuICC/` : change `mica5951` into your username.
4. Modules that you need to load:
```
module load cmake
module load intel
module load impi
module load hdf5
module load fftw
module load python
module load mkl
```
5. config and compile as indicated below

# Preliminary steps on Anvil
After having cloned or pulled the latest version of QuICC:

1. Install SuiteSparse libraries:
    
    a. grab the latest stable version of the libraries from, e.g., `http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-4.5.4.tar.gz `
    
    b. purge modules: `module purge`
    
    c. It's easiest to build SuiteSparse with the intel compiler. load the modules `intel`, `impi`, `intel-mkl` and `cmake`

    d. untar the SuiteSparse repository, go in the directory and build with the following command:
        `make MKLROOT=${RCAC_MKL_ROOT} BLAS="-L $RCAC_MKL_ROOT/lib/intel64 -lmkl_intel_lp64 -lmkl_core -lmkl_intel_thread -lpthread -lm" LAPACK=''`
        that builds the code and runs through some tests.  It puts the library files in SuiteSparse/lib and include files in SuiteSparse/include.  Note that after LAPACK above, it is two single quotes with no space in between (LAPACK is coming through MKL, which is already linked in place of BLAS).
    
    e. purge modules: `module purge`
2. Change the file `cmake.d/platforms/Anvil.cmake` so that the SuiteSparse is correctly linked. At the moment the file points at the libraries in `/home/x-oliver/QuICC/` : change `x-oliver` into your username.
3. Load the following modules to compile with `gcc`:
```
module load cmake
module load gcc
module load openmpi
module load fftw
module load hdf5
module load intel-mkl
module load python/3.9.5
module load petsc
```
For some reason intel-mkl prepends some problematic directories to the `$CPATH` environment. Run 

`export CPATH=...` 

to fix.

4. config and compile as indicated below

# Preliminary steps on Daint

-  One can add following lines to your local ~/.ssh/config 

```
Host daint*
   Hostname %h.cscs.ch
   ForwardAgent yes
   Port 22
   User USERNAME
   ProxyJump USERNAME@ela.cscs.ch
```

and log onto Daint with 

```
ssh daint
```

- The following modules should be loaded for Daint with GCC compiler

```
module load daint-gpu
module switch PrgEnv-cray PrgEnv-gnu
module load cray-fftw
module load cray-hdf5-parallel
module load cray-python
module load cray-tpsl
module load CMake
```

- or the following modules should be loaded for Daint with Cray compiler

```
module load daint-gpu
module load cray-fftw
module load cray-hdf5-parallel
module load cray-python
module load cray-tpsl
module load CMake
```

# Configure

CMake is used to generate the Makefile that will allow the compilation of the simulations. The build process uses an out-of-source approach to keep 
the sources clean. The following steps are required to create and configure the build. To fix the notations, we assume:

   - The sources are in: /home/myself/QuiCC

   - The binaries should be somewhere under: $SCRATCH

   1. Create a new directory where you'll like all the binaries to be (Warning: directory might grow large!):
      ```
      mkdir $SCRATCH/QuiCC
      ```

   2. Binaries with different options/parallelisations need to have separate directories
      ```
      mkdir $SCRATCH/QuiCC/Release-Serial #(serial version)
      mkdir $SCRATCH/QuiCC/Release-Tubular #(tubular parallelisation)
      ```

   3. Change into one of the newly create directories,as an example Release-Tubular/:
      ```
      cd $SCRATCH/QuiCC/Release-Tubular
      ```

   4. Initialise CMake and start the configuration process:
      ```
      ccmake /home/myself/QuiCC
      ```
   5. Press 'c' to configure and then 'e' to exit

   6. Set the build type and the platform (cf. [Platform](/tutorial/tutorial-platforms)).  Press 'c' to reconfigure then 'e' to exit. More options should now be avaiable (depending on platform). Details about the CMake configuration options are given [here](/tutorial/options/options-cmake).

   7. Configure the sources and press 'c' (possibly multiple times) and generate generate the Makefile by pressing 'g'

   8. Once back to the shell, the build directory should be ready to compile the sources


back to [home](/)/[tutorial](/tutorial)
