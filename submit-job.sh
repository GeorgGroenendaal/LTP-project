#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --job-name=python_example
#SBATCH --mem=2048
module load Python/3.8.6-GCCcore-10.2.0

python3 test.py
