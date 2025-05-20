import logging
import os
import shutil
import subprocess
import sys

from constants import DATABASE_NAME, IMAGES_DIRECTORY

program1 = 'prepare_colors.py'
program2 = 'prepare_combinations.py'
program3 = 'main.py'
python = sys.executable

logging.basicConfig(
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    format="%(asctime)s  %(name)s  [%(levelname)s]: %(message)s"
)
logger = logging.getLogger(__name__)


def run_programs():
    os.remove(DATABASE_NAME)
    logger.info('Remove database')
    shutil.rmtree(IMAGES_DIRECTORY)
    logger.info('Remove image directory')
    subprocess.run([python, program1])
    logger.info('Prepare colors table')
    subprocess.run([python, program2])
    logger.info('Prepare combinations table')
    subprocess.run([python, program3])
    logger.info('Start application from the scratch')


run_programs()
