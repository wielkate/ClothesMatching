import os
import shutil
import sys
import subprocess

from src.package_wielkate.main.commons.constants import DATABASE_NAME, IMAGES_DIRECTORY

program1 = 'src/package_wielkate/main/scripts/prepare_colors.py'
program2 = 'src/package_wielkate/main/scripts/prepare_combinations.py'
program3 = 'src/package_wielkate/main/__main__.py'
python = sys.executable

def run_programs():
    os.remove(DATABASE_NAME)
    print('Remove database')
    shutil.rmtree(IMAGES_DIRECTORY)
    print('Remove image directory')
    subprocess.run([python, program1])
    print('Prepare colors table')
    subprocess.run([python, program2])
    print('Prepare combinations table')
    subprocess.run([python, program3])
    print('Start application from the scratch')

run_programs()