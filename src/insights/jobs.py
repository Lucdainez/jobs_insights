from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    list = []
    with open(path, "r") as file:
        result = csv.DictReader(file)
        for job in result:
            list.append(job)
    return list


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    list_unique = set()
    for a in data:
        list_unique.add(a["job_type"])
    return list_unique


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    list_filtered_job_types = []
    for i in jobs:
        if i["job_type"] == job_type:
            list_filtered_job_types.append(i)
    return list_filtered_job_types
