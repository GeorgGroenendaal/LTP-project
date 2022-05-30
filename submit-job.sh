#!/bin/bash
#SBATCH --job-name=gpt-j-run
#SBATCH --partition regular 
#SBATCH --mem 60000
#SBATCH --nodes=1
#SBATCH --ntasks=24
#SBATCH --time=05:00:00
poetry run python -m ltp run 29522_gpt_j_test
