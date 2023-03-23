import pytest
from src.insights.jobs import (
    read,
    filter_by_job_type,
    get_unique_job_types,
)


JOB_TYPES = {
    "PART_TIME": {"jobs": 172},
    "OTHER": {"jobs": 39},
    "FULL_TIME": {"jobs": 3078},
    "CONTRACTOR": {"jobs": 14},
    "TEMPORARY": {"jobs": 2},
    "INTERN": {"jobs": 19},
}
TOTAL_JOBS = 3324


def test_read_jobs():
    results = read("data/jobs.csv")

    assert type(results) == list
    assert len(results) == 3324
    for result in results:
        assert type(result) == dict

    results = read("tests/mocks/jobs.csv")

    assert type(results) == list
    assert len(results) == 3
    expected_list = [
        {"title": "Front end developer", "salary": "2000", "type": "trainee"},
        {"title": "Back end developer", "salary": "3000", "type": "full time"},
        {
            "title": "Full stack end developer",
            "salary": "4000",
            "type": "full time",
        },
    ]
    for result, expected in zip(results, expected_list):
        assert result == expected


def test_total_jobs_in_job_types():
    assert TOTAL_JOBS == sum([type_["jobs"] for type_ in JOB_TYPES.values()])


def test_get_unique_job_types():
    result = get_unique_job_types("data/jobs.csv")
    assert len(result) == 6

    for type_ in JOB_TYPES.keys():
        assert type_ in result

    result = get_unique_job_types("tests/mocks/jobs_with_types.csv")
    assert len(result) == 2
    assert "full time" in result
    assert "trainee" in result


@pytest.fixture()
def jobs_for_filter_by_job_type():
    return [
        {"id": 1, "job_type": "PART_TIME"},
        {"id": 2, "job_type": "PART_TIME"},
        {"id": 3, "job_type": "OTHER"},
        {"id": 4, "job_type": "OTHER"},
        {"id": 5, "job_type": "FULL_TIME"},
        {"id": 6, "job_type": "FULL_TIME"},
        {"id": 7, "job_type": "CONTRACTOR"},
        {"id": 8, "job_type": "CONTRACTOR"},
        {"id": 9, "job_type": "TEMPORARY"},
        {"id": 10, "job_type": "TEMPORARY"},
        {"id": 11, "job_type": "INTERN"},
        {"id": 12, "job_type": "INTERN"},
    ]


def test_filter_by_job_type(jobs_for_filter_by_job_type):
    types = [
        "PART_TIME",
        "OTHER",
        "FULL_TIME",
        "CONTRACTOR",
        "TEMPORARY",
        "INTERN",
    ]
    id_ = 1
    for type_ in types:
        jobs = filter_by_job_type(jobs_for_filter_by_job_type, type_)
        assert len(jobs) == 2
        assert jobs[0]["id"] == id_
        assert jobs[1]["id"] == id_ + 1
        id_ += 2
    jobs = filter_by_job_type(jobs_for_filter_by_job_type, "")
    assert len(jobs) == 0
