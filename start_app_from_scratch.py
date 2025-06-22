import logging
import os
import subprocess
import sys

import requests

from src.package_wielkate.main.commons.constants import DATABASE_NAME, CLOTHES_MATCHING_API

program1 = 'src/package_wielkate/main/scripts/prepare_colors.py'
program2 = 'src/package_wielkate/main/scripts/prepare_combinations.py'
program3 = 'src/package_wielkate/main/__main__.py'
python = sys.executable

GREY_LIGHT = '\033[37m'
WHITE = '\033[97m'
GREEN = '\033[92m'
CYAN = '\033[36m'

logging.basicConfig(
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    format=f"{CYAN}%(asctime)s  {GREY_LIGHT}%(name)s  {GREEN}[%(levelname)s]: {WHITE}%(message)s"
)
logger = logging.getLogger(__name__)


def clear_bucket():
    requests.delete(f'{CLOTHES_MATCHING_API}/delete')


def run_programs():
    if os.path.exists(DATABASE_NAME):
        os.remove(DATABASE_NAME)
        logger.info('Remove database')
    else:
        logger.info('Database file not found, skipping removal')
    clear_bucket()
    logger.info('Delete all images from the bucket')
    subprocess.run([python, program1])
    logger.info('Prepare colors table')
    subprocess.run([python, program2])
    logger.info('Prepare combinations table')
    subprocess.run([python, program3])
    logger.info('Start application from the scratch')


run_programs()
