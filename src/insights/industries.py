from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    list_unique = set(a["industry"] for a in data if a["industry"] != "")
    return list(list_unique)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list_filtered_industry = [i for i in jobs if i["industry"] == industry]
    return list_filtered_industry
