import os
import sys
import time

import numpy as np
import logging
import mne
import warnings


warnings.simplefilter("ignore", DeprecationWarning)
logging.basicConfig(format="%(asctime)s - %(levelname)s — %(funcName)s:%(lineno)d ——— %(message)s",
                    datefmt="%d.%m.%Y-%H:%M:%S",
                    level=logging.DEBUG,
                    handlers=[logging.FileHandler("logs.txt", 'w', encoding='UTF-8')])

logger = logging.getLogger()


def load_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


DATAFOLDER_NAME = "BCICIV_2a_gdf"
EXT = ".gdf"
# noinspection PyTypeChecker
gdf_files = [os.path.join(load_file(DATAFOLDER_NAME), _) for _ in os.listdir(load_file(DATAFOLDER_NAME)) if
             _.endswith(EXT)]
print(gdf_files)

# noinspection PyTypeChecker
for file in gdf_files:
    raw = mne.io.read_raw_gdf(file)
    raw_info = raw.info
    raw_ch_names = raw.ch_names
    print(raw_info, raw_ch_names)
    event = mne.events_from_annotations(raw)
    epoch = mne.Epochs(raw, event[0], event_repeated="merge", preload=True)
    print(epoch.info)
    logger.info(raw_info);logger.info(raw_ch_names);logger.info(epoch.info)

