import logging
from collections import defaultdict

import requests

from commons.constants import CLOTHES_MATCHING_API
from models.Mode import Mode

logger = logging.getLogger(__name__)


def load_combinations(mode):
    response = requests.get(f'{CLOTHES_MATCHING_API}/get_combinations/{mode}')
    grouped = defaultdict(list)
    for item in response.json():
        base_color = item['color']
        related_color = item['related_color']
        grouped[base_color].append(related_color)

    logging.info(f'Load {len(grouped)} {mode.lower()} combinations from database')
    return grouped


global_monochrome = load_combinations(Mode.MONOCHROME.value)
global_complementary = load_combinations(Mode.COMPLEMENTARY.value)
global_analogous = load_combinations(Mode.ANALOGOUS.value)
