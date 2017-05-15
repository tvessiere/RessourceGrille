#!/bin/bash
#
#SBATCH --job-name=vessiere_thomas_test_itk_timed
#SBATCH --output=vessiere_thomas_test_itk_time_logs_40k.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=200:00:00
#SBATCH --mem=256G
#SBATCH --partition=Public
/home/mass/ifilesets/ULG/f041985/anaconda2/envs/cytomine_itk/bin/python /home/mass/ifilesets/ULG/f041985/algo/sitk_cv_time.py

