#!/bin/bash
#SBATCH --job-name=vessiere_thomas_test_itk
#SBATCH --output=vessiere_thomas_test_itk_logs_16res.txt
#SBATCH --ntasks=1
#SBATCH --time=200:00:00
#SBATCH --mem=200G
#SBATCH --partition=Public
/home/mass/ifilesets/ULG/f041985/anaconda2/envs/cytomine_itk/bin/python /home/mass/ifilesets/ULG/f041985/algo/sitk_cv.py
