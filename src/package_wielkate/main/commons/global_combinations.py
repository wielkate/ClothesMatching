import logging

from endpoints.endpoints import load_combinations
from models.Mode import Mode

logger = logging.getLogger(__name__)

global_monochrome = load_combinations(Mode.MONOCHROME.value)
global_complementary = load_combinations(Mode.COMPLEMENTARY.value)
global_analogous = load_combinations(Mode.ANALOGOUS.value)
