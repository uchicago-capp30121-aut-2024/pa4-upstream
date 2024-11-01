'''
Polling places: test code for simulate_election_day
'''

import pytest
import json

# DO NOT REMOVE THESE LINES OF CODE
# pylint: disable-msg= invalid-name, missing-docstring, too-many-arguments, line-too-long
# pylint: disable-msg= missing-docstring, too-many-locals, unused-argument


precinct_files = [("precinct-0.json"),
                  ("precinct-1.json"),
                  ("precinct-2.json"),
                  ("precinct-3.json"),
                  ("precinct-4.json"),
                  ("precinct-5.json")]

ACTUAL = "./data/"
EXPECTED = "./test-data/"

def do_test_process_data(precinct_num):
    e = open(EXPECTED + "precinct-" + precinct_num + ".json")
    a = open(ACTUAL + "precinct-" + precinct_num + ".json")

    expected = json.load(e)
    actual = json.load(a)

    e.close()
    a.close()

    msg = "Expected JSON: " + str(expected) + "\n"
    msg += "Actual JSON: " + str(actual)

    for key in expected:
        assert key in actual, "Key missing from JSON: " + key + "\n" + msg
        assert type(expected[key]) == type(actual[key]), "Incorrect type in JSON: " + key + "\n" + msg
        assert expected[key] == actual[key], "Incorrect value in JSON: " + key + "\n" + msg

    for key in actual:
        assert key in expected, "Extra key in JSON: " + key + "\n" + msg

def test_process_data_0():
    do_test_process_data("0")

def test_process_data_1():
    do_test_process_data("1")

def test_process_data_2():
    do_test_process_data("2")

def test_process_data_3():
    do_test_process_data("3")

def test_process_data_4():
    do_test_process_data("4")

def test_process_data_5():
    do_test_process_data("5")

def test_process_data_6():
    do_test_process_data("6")