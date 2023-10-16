#PBS -N jevs_subseasonal_grid2obs_prepbufr_plots_31days
#PBS -j oe
#PBS -S /bin/bash
#PBS -q "dev"
#PBS -A EVS-DEV
#PBS -l walltime=00:10:00
#PBS -l place=vscatter,select=1:ncpus=32:ompthreads=1:mem=10GB
#PBS -l debug=true
#PBS -V

set -x

export model=evs

cd $PBS_O_WORKDIR

export HOMEevs=/lfs/h2/emc/vpppg/noscrub/$USER/EVS

export job=${PBS_JOBNAME:-jevs_subseasonal_grid2obs_prepbufr_plots_31days}
export jobid=$job.${PBS_JOBID:-$$}

source $HOMEevs/versions/run.ver
module reset
module load prod_envir/${prod_envir_ver}
source $HOMEevs/modulefiles/subseasonal/subseasonal_plots.sh


export USER=$USER
export ACCOUNT=EVS-DEV
export envir=prod
export KEEPDATA=YES
export SENDDBN=NO
export DATAROOT=/lfs/h2/emc/stmp/$USER/evs_test/$envir/tmp
export QUEUE=dev
export QUEUESHARED=dev_shared
export QUEUESERV=dev_transfer
export PARTITION_BATCH=
export nproc=32
export USE_CFP=YES
export met_ver=${met_ver}
export metplus_ver=${metplus_ver}
export cyc=00
export NET=evs
export evs_ver=${evs_ver}
export STEP=plots
export COMPONENT=subseasonal
export RUN=atmos
export MODELNAME="gefs cfs"
export VERIF_CASE=grid2obs
export VERIF_TYPE=PrepBufr
export NDAYS=31
export DAYS=32

export COMROOT=/lfs/h2/emc/ptmp/$USER
export COMIN=/lfs/h2/emc/vpppg/noscrub/$USER/$NET/$evs_ver

export config=$HOMEevs/parm/evs_config/subseasonal/config.evs.${COMPONENT}.${VERIF_CASE}.${STEP}.${VERIF_TYPE}

# Call executable job script
$HOMEevs/jobs/JEVS_SUBSEASONAL_PLOTS


######################################################################
# Purpose: The job and task scripts work together to generate the
#          subseasonal grid-to-obs 2-m temperature statistical plots
#          for the GEFS and CFS models for past 31 days.
######################################################################