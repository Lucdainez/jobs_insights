from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    list_of_max_salaries = []
    for i in data:
        if i["max_salary"]:
            try:
                number = int(i["max_salary"])
                list_of_max_salaries.append(number)
            except ValueError:
                pass
    return max(list_of_max_salaries)


def get_min_salary(path: str) -> int:
    data = read(path)
    list_of_min_salaries = []
    for i in data:
        if i["min_salary"]:
            try:
                number = int(i["min_salary"])
                list_of_min_salaries.append(number)
            except ValueError:
                pass
    return min(list_of_min_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        maximun_salary = int(job["max_salary"])
        minimun_salary = int(job["min_salary"])
        salary_parameter = int(salary)

    except TypeError:
        raise ValueError(
            "salary, maximun_salary e minimun_salary devem ser numéricos"
        )

    except KeyError:
        raise ValueError("chave inexistente")

    if minimun_salary > maximun_salary:
        raise ValueError("min_salary é maior que o max_salary")

    return minimun_salary <= salary_parameter <= maximun_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    list_of_salaries = []

    for i in jobs:
        try:
            if matches_salary_range(i, salary):
                list_of_salaries.append(i)
        except ValueError:
            pass
    return list_of_salaries
