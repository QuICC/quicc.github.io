# Piz-Daint on GPU nodes

```bash
module load daint-gpu
module switch PrgEnv-cray PrgEnv-gnu
module load cray-fftw cray-hdf5-parallel cray-python cray-tpsl Boost CMake

cmake </path/to/QuICC> -DCMAKE_CXX_COMPILER=CC \
-DQUICC_USE_MPI=ON \
-DQUICC_MULTPRECISION=ON \
-DQUICC_EIGEN_ENABLE_VECTORIZATION=ON \
-DQUICC_MODEL=<GreatSimulation>

make
```

## Kokkos CUDA

```bash
. /apps/daint/UES/anfink/gpu/environment
module load cray-fftw Boost
cmake </path/to/QuICC> -DCMAKE_CXX_COMPILER=CC \
-DQUICC_USE_MPI=ON \
-DQUICC_MULTPRECISION=ON \
-DCMAKE_CUDA_COMPILER=nvcc \
-DKokkos_DIR=$TRILINOS_DIR/lib/cmake/Kokkos \
-DQUICC_USE_KOKKOS=ON -DQUICC_USE_KOKKOS_CUDA=ON \
-DQUICC_MODEL=<GreatSimulation> \
-DCMAKE_VERBOSE_MAKEFILE=ON

make
```

## Kokkos CUDA

```bash
. /apps/daint/UES/anfink/gpu/environment
module load cray-fftw Boost
cmake </path/to/QuICC> -DCMAKE_CXX_COMPILER=CC \
-DQUICC_USE_MPI=ON \
-DQUICC_MULTPRECISION=ON \
-DCMAKE_CUDA_COMPILER=nvcc \
-DKokkos_DIR=$TRILINOS_DIR/lib/cmake/Kokkos \
-DQUICC_USE_KOKKOS=ON -DQUICC_USE_KOKKOS_CUDA=ON \
-DQUICC_MODEL=<GreatSimulation> \
-DCMAKE_VERBOSE_MAKEFILE=ON

make
```

# Piz-Daint on MC nodes

```bash
module load daint-mc
module switch PrgEnv-cray PrgEnv-gnu
module load cray-fftw cray-hdf5-parallel cray-python cray-tpsl Boost CMake

cmake </path/to/QuICC> -DCMAKE_CXX_COMPILER=CC \
-DQUICC_USE_MPI=ON \
-DQUICC_MULTPRECISION=ON \
-DQUICC_EIGEN_ENABLE_VECTORIZATION=ON \
-DQUICC_MODEL=<GreatSimulation>

make
```

## Kokkos OpenMP

```bash
. /apps/daint/UES/anfink/cpu/environment
module load cray-fftw Boost
cmake </path/to/QuICC> -DCMAKE_CXX_COMPILER=CC \
-DQUICC_USE_MPI=ON \
-DQUICC_MULTPRECISION=ON \
-DKokkos_DIR=$TRILINOS_DIR/lib/cmake/Kokkos \
-DQUICC_USE_KOKKOS=ON \
-DQUICC_MODEL=<GreatSimulation> \
-DCMAKE_VERBOSE_MAKEFILE=ON

make
```

# Euler

```bash
module load stack
module load openmpi fftw hdf5 boost python openblas cmake

cmake -DQUICC_USE_MPI=ON \
-DQUICC_MULTPRECISION=ON \
-DQUICC_EIGEN_ENABLE_VECTORIZATION=ON \
-DQUICC_MODEL=<GreatSimulation> \
</path/to/QuICC>
```

Euler login nodes are slow, build on compute nodes
```bash
salloc --nodes=1 --cpus-per-task=64 --time=00:20:00
srun make -j 64
```

In  case of problems with h5py, install into a Python venv

```bash
python -m venv quicc_env
. quicc_env/bin/activate
python -m pip install h5py
```
afterwards you'll only need to activate the python env
```bash
. quicc_env/bin/activate
```

# LUMI-C

## Modules
```sh
module load LUMI
module load PrgEnv-gnu
module load cray-python
module load cray-fftw
module load cray-hdf5-parallel
module load Boost
module load buildtools
module load craype-x86-milan
```

## Compilation
```sh
salloc --nodes=1 --account=PROJECT --partition=standard --time=01:00:00
srun --ntasks=1 cmake .. -GNinja \
-DCMAKE_CXX_COMPILER=CC \
-DQUICC_USE_MPI=ON \
-DQUICC_EIGEN_ENABLE_VECTORIZATION=ON \
-DQUICC_MODEL=MODEL \
-DQUICC_PROFILE_LEVEL=0 \
-DQUICC_PROFILE_BACKEND=none \
-DCMAKE_CXX_FLAGS=-noopenmp

srun --ntasks=1 --cpus-per-task=64 ninja
```
