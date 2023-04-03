#!/bin/bash 
#SBATCH -o ./Report/output.%a.out 
#SBATCH --partition=ceewater_cjgleason-cpu 
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=1 
#SBATCH --cpus-per-task=5 
#SBATCH --mem=5G 
#SBATCH --time=10000 
#SBATCH --job-name=confluence-metroman 
#SBATCH --array=0-50%9 

module load singularity 
python3 slurm_run_module.py -n metroman -e ${SLURM_ARRAY_TASK_ID}