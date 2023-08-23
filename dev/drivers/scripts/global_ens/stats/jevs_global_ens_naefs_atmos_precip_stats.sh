#PBS -N jevs_global_ens_naefs_atmos_precip_stats
#PBS -j oe
#PBS -S /bin/bash
#PBS -q dev
#PBS -A VERF-DEV
#PBS -l walltime=01:00:00
#PBS -l place=vscatter:exclhost,select=1:ncpus=2:mem=100GB
#PBS -l debug=true


export OMP_NUM_THREADS=1
#Total 18 cpu cores: assigned to 1 nodes, 18 cores for each node 
#Total 9 processes 4(cmce/upper) + 1 (cmce/apcp24h) + 4 (cmce/apcp06h)
#
set -x

export HOMEevs=/lfs/h2/emc/vpppg/noscrub/${USER}/EVS

source $HOMEevs/versions/run.ver

export NET=evs
export RUN=atmos
export STEP=stats
export COMPONENT=global_ens
export VERIF_CASE=precip
export MODELNAME=naefs


module reset
module load prod_envir/${prod_envir_ver}

source $HOMEevs/modulefiles/$COMPONENT/${COMPONENT}_${STEP}.sh




export KEEPDATA=YES

export cyc=00
export COMIN=/lfs/h2/emc/vpppg/noscrub/${USER}/$NET/$evs_ver
export COMOUT=/lfs/h2/emc/vpppg/noscrub/${USER}/$NET/$evs_ver
export FIXevs=/lfs/h2/emc/vpppg/noscrub/emc.vpppg/verification/EVS_fix
export DATA=/lfs/h2/emc/stmp/${USER}/evs/tmpnwprd
export job=${PBS_JOBNAME:-jevs_${MODELNAME}_${VERIF_CASE}_${STEP}}
export jobid=$job.${PBS_JOBID:-$$}

export gefs_number=20
export run_mpi=no

export maillist='geoffrey.manikin@noaa.gov,binbin.zhou@noaa.gov'

${HOMEevs}/jobs/global_ens/stats/JEVS_GLOBAL_ENS_STATS