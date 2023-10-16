#PBS -N jevs_global_det_atmos_grid2obs_pres_levs_plots_90days_00
#PBS -j oe
#PBS -S /bin/bash
#PBS -q dev
#PBS -A EVS-DEV
#PBS -l walltime=01:30:00
#PBS -l place=vscatter:exclhost,select=5:ncpus=128:ompthreads=1
#PBS -l debug=true
#PBS -V

set -x

cd $PBS_O_WORKDIR

export model=evs
export HOMEevs=/lfs/h2/emc/vpppg/noscrub/$USER/EVS

export SENDCOM=YES
export KEEPDATA=YES
export SENDDBN=NO
export job=${PBS_JOBNAME:-jevs_global_det_atmos_grid2obs_pres_levs_plots_90days}
export jobid=$job.${PBS_JOBID:-$$}
export SITE=$(cat /etc/cluster_name)
export cyc=00

source $HOMEevs/versions/run.ver
module reset
module load prod_envir/${prod_envir_ver}
source $HOMEevs/modulefiles/global_det/global_det_plots.sh

export machine=WCOSS2
export USE_CFP=YES
export nproc=128

export envir=prod
export NET=evs
export STEP=plots
export COMPONENT=global_det
export RUN=atmos
export VERIF_CASE=grid2obs
export VERIF_TYPE=pres_levs
export NDAYS=90

export DATAROOT=/lfs/h2/emc/stmp/$USER/evs_test/$envir/tmp
export TMPDIR=$DATAROOT
export COMIN=/lfs/h2/emc/vpppg/noscrub/$USER/$NET/$evs_ver
export COMROOT=/lfs/h2/emc/ptmp/${USER}

# Set config file
export config=$HOMEevs/parm/evs_config/global_det/config.evs.prod.${STEP}.${COMPONENT}.${RUN}.${VERIF_CASE}.${VERIF_TYPE}
echo $config

# CALL executable job script here
$HOMEevs/jobs/JEVS_GLOBAL_DET_PLOTS

######################################################################
# Purpose: This does the plotting work for the global deterministic
#          atmospheric grid-to-observations pres_levs for last 90 days
######################################################################