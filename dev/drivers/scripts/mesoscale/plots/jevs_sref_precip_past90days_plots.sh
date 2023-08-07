#!/bin/bash

#PBS -N jevs_sref_precip_plot
#PBS -j oe
#PBS -S /bin/bash
#PBS -q dev
#PBS -A EVS-DEV
#PBS -l walltime=00:30:00
#PBS -l place=vscatter:exclhost,select=1:ncpus=30:mem=100GB
#PBS -l debug=true


export OMP_NUM_THREADS=1

export evs_ver=v1.0
export HOMEevs=/lfs/h2/emc/vpppg/noscrub/${USER}/EVS

source $HOMEevs/versions/run.ver.metplus5.0.0

module reset
module load envvar/$envvar_ver
module load PrgEnv-intel/$PrgEnv_intel_ver
module load intel/$intel_ver
module load cray-pals/$craypals_ver
module load libjpeg/$libjpeg_ver
module load grib_util/$grib_util_ver
module load prod_util/$prod_util_ver
module load prod_envir/$prod_envir_ver
module load wgrib2/$wgrib2_ver
module load libpng/$libpng_ver
module load zlib/$zlib_ver
module load jasper/$jasper_ver
module load netcdf/$netcdf_ver
module load cfp/$cfp_ver
export HPC_OPT=/apps/ops/para/libs
module use /apps/ops/para/libs/modulefiles/compiler/intel/$intel_ver
module load gsl/${gsl_ver}
module load python/$python_ver
module load met/$met_ver
module load metplus/$metplus_ver
module load udunits/${udunits_ver}

export met_v=${met_ver:0:4}

module list


export envir=prod

export NET=evs
export STEP=plots
export COMPONENT=mesoscale
export RUN=atmos
export VERIF_CASE=precip
export MODELNAME=sref

export KEEPDATA=YES

export cyc=00
export past_days=90

export run_mpi=yes
export valid_time=both

export COMIN=/lfs/h2/emc/vpppg/noscrub/${USER}/$NET/$evs_ver
export COMOUT=/lfs/h2/emc/vpppg/noscrub/${USER}/$NET/$evs_ver
export DATA=/lfs/h2/emc/ptmp/${USER}/evs/tmpnwprd
export job=${PBS_JOBNAME:-jevs_${MODELNAME}_${VERIF_CASE}_${STEP}}
export jobid=$job.${PBS_JOBID:-$$}

${HOMEevs}/jobs/${COMPONENT}/${STEP}/JEVS_MESOSCALE_PLOTS