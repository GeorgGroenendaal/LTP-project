#!/bin/bash
#SBATCH --job-name=gpt-j-test
#SBATCH --partition short
#SBATCH --mem 60000
#SBATCH --nodes=1
#SBATCH --ntasks=24
#SBATCH --time=00:30:00
poetry run python -m ltp run 29522_test
