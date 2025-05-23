import logging
import os
import shutil
import subprocess
import sys

from commons.constants import DATABASE_NAME, IMAGES_DIRECTORY

program1 = 'service/prepare_colors.py'
program2 = 'service/prepare_combinations.py'
program3 = 'main.py'
python = sys.executable

logging.basicConfig(
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    format="%(asctime)s  %(name)s  [%(levelname)s]: %(message)s"
)
logger = logging.getLogger(__name__)


def run_programs():
    if os.path.exists(DATABASE_NAME):
        os.remove(DATABASE_NAME)
        logger.info("Removed database")
    else:
        logger.info("Database file not found, skipping removal")

    if os.path.exists(IMAGES_DIRECTORY):
        shutil.rmtree(IMAGES_DIRECTORY)
        logger.info("Removed image directory")
    else:
        logger.info("Image directory not found, skipping removal")

    logger.info('Prepared colors table')
    subprocess.run([python, program2])
    logger.info('Prepared combinations table')
    subprocess.run([python, program3])
    logger.info('Started application from the scratch')


run_programs()
