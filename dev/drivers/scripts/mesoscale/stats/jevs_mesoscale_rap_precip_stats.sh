#PBS -N jevs_mesoscale_rap_precip_stats_00
#PBS -j oe
#PBS -S /bin/bash
#PBS -q "dev"
#PBS -A VERF-DEV
#PBS -l walltime=00:15:00
#PBS -l place=vscatter:exclhost,select=1:ncpus=128:ompthreads=1:mem=30GB
#PBS -l debug=true
#PBS -V

set -x

cd $PBS_O_WORKDIR

export model=evs

export RUN_ENVIR=emc
export SENDECF=YES
export SENDCOM=YES
export KEEPDATA=NO
export SENDDBN=YES
export SENDDBN_NTC=
export job=${PBS_JOBNAME:-jevs_rap_precip_stats}
export jobid=$job.${PBS_JOBID:-$$}
export SITE=$(cat /etc/cluster_name)  
export envir="dev"
export NET="evs"
export RUN="atmos"
export cyc=$(date +"%H")
export cycle=t${cyc}z

export HOMEevs=/lfs/h2/emc/vpppg/noscrub/${USER}/EVS
export PARMevs=$HOMEevs/parm
export USHevs=$HOMEevs/ush
export EXECevs=$HOMEevs/exec
export FIXevs="/lfs/h2/emc/vpppg/noscrub/emc.vpppg/verification/EVS_fix"

export VDATE=$(date -d "today -2 day" +"%Y%m%d")
export STEP="stats"
export COMPONENT="mesoscale"
export VERIF_CASE="precip"
export MODELNAME="rap" 
export machine=WCOSS2
export USE_CFP=YES
export nproc=128  
export evs_run_mode="production"
export maillist='geoffrey.manikin@noaa.gov,mallory.row@noaa.gov'
export config=$HOMEevs/parm/evs_config/mesoscale/config.evs.prod.${STEP}.${COMPONENT}.${RUN}.${VERIF_CASE}.${MODELNAME}

source /usr/share/lmod/lmod/init/sh
export MET_bin_exec="bin"

module reset
source $HOMEevs/versions/run.ver
source $HOMEevs/modulefiles/${COMPONENT}/${COMPONENT}_${STEP}.sh


export DATAROOT=/lfs/h2/emc/stmp/$USER/evs_test/$envir/tmp
export COMOUT=/lfs/h2/emc/vpppg/noscrub/${USER}/$NET/$evs_ver/$STEP/$COMPONENT

# Job Settings and Run
${HOMEevs}/jobs/mesoscale/stats/JEVS_MESOSCALE_STATS
