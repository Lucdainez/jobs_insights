# import pytest
from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "JOB") == 3454
    assert count_ocurrences("data/jobs.csv", "job") == 3454
    assert count_ocurrences("data/jobs.csv", "business") == 4709
    assert count_ocurrences("data/jobs.csv", "business") != 47
