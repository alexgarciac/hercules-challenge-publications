import logging
import os
import sys

# set up module paths for imports
module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)
src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

# start logging system and set logging level
logger = logging.getLogger()
logger.setLevel(logging.WARN)
logging.info("Starting logger")

DATA_DIR = os.path.join(module_path, 'data')
RESULTS_DIR = os.path.join(module_path, 'results')