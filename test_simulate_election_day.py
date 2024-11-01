'''
Polling places: test code for simulate_election_day
'''

import csv
import pytest
from test_utils import run_test

# DO NOT REMOVE THESE LINES OF CODE
# pylint: disable-msg= invalid-name, missing-docstring, too-many-arguments, line-too-long
# pylint: disable-msg= missing-docstring, too-many-locals, unused-argument


precinct_files = [("config-single-precinct-0.json", "Single Precinct"),
                  ("config-single-precinct-1.json", "Single Precinct"),
                  ("config-single-precinct-2.json", "Single Precinct"),
                  ("config-single-precinct-3.json", "Single Precinct"),
                  ("config-single-precinct-4.json", "Single Precinct"),
                  ("config-single-precinct-5.json", "Single Precinct")]


DATA_DIR = "./test-data/"



@pytest.mark.parametrize("config_file,desc", precinct_files)
def test_simulate(config_file, desc):
    run_test(DATA_DIR + config_file, check_start = True)
