import pytest
from src.pre_built.sorting import sort_by

# from tests.brazilian.test_brazilian_jobs import return_of_list_of_dict


@pytest.fixture
def jobs():
    return [
        {
            "id": 1,
            "title": "Job 1",
            "min_salary": 3000,
            "max_salary": 4000,
            "date_posted": "2022-02-01",
        },
        {
            "id": 2,
            "title": "Job 2",
            "min_salary": 2000,
            "max_salary": 5000,
            "date_posted": "2022-03-01",
        },
    ]


@pytest.fixture
def jobs_order_by_min_salary():
    return [
        {
            "id": 2,
            "title": "Job 2",
            "min_salary": 2000,
            "max_salary": 5000,
            "date_posted": "2022-03-01",
        },
        {
            "id": 1,
            "title": "Job 1",
            "min_salary": 3000,
            "max_salary": 4000,
            "date_posted": "2022-02-01",
        },
    ]


def test_sort_by_criteria(jobs, jobs_order_by_min_salary):

    sort_by(jobs, "min_salary")
    assert jobs == jobs_order_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == jobs

    sort_by(jobs, "date_posted")
    assert jobs == jobs

    with pytest.raises(
        ValueError, match="invalid sorting criteria: invalid_criteria"
    ):
        sort_by(jobs, "invalid_criteria")
