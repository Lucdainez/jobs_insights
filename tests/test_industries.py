import pytest

from src.insights.industries import (
    filter_by_industry,
    get_unique_industries,
)


INDUSTRIES = {
    "Health Care": {"jobs": 232},
    "Arts, Entertainment & Recreation": {"jobs": 2},
    "Biotech & Pharmaceuticals": {"jobs": 317},
    "Agriculture & Forestry": {"jobs": 1},
    "Consumer Services": {"jobs": 7},
    "Accounting & Legal": {"jobs": 29},
    "Insurance": {"jobs": 29},
    "Restaurants, Bars & Food Services": {"jobs": 3},
    "Non-Profit": {"jobs": 10},
    "Transportation & Logistics": {"jobs": 8},
    "Business Services": {"jobs": 583},
    "Retail": {"jobs": 63},
    "Aerospace & Defense": {"jobs": 144},
    "Construction, Repair & Maintenance": {"jobs": 66},
    "Media": {"jobs": 29},
    "Real Estate": {"jobs": 5},
    "Finance": {"jobs": 223},
    "Information Technology": {"jobs": 679},
    "Education": {"jobs": 60},
    "Telecommunications": {"jobs": 35},
    "Manufacturing": {"jobs": 42},
    "Government": {"jobs": 105},
    "Oil, Gas, Energy & Utilities": {"jobs": 28},
}
UNINFORMED_INDUSTRIES = 624
TOTAL_JOBS = 3324
TOTAL_JOBS_WITH_SPECIFIED_SALARY = 2232
MAX_SALARY = 383416
MIN_SALARY = 19857


def test_total_jobs_in_industries():
    assert TOTAL_JOBS - UNINFORMED_INDUSTRIES == sum(
        [industry["jobs"] for industry in INDUSTRIES.values()]
    )


def test_get_unique_industries():
    result = get_unique_industries("data/jobs.csv")

    assert len(result) == len(INDUSTRIES)

    for industry in INDUSTRIES:
        assert industry in result

    # * Mock
    result = get_unique_industries("tests/mocks/jobs_with_industries.csv")
    assert len(result) == 2
    assert "agriculture" in result
    assert "solar energy" in result


@pytest.fixture()
def jobs_for_filter_by_industry():
    return [
        {"id": 1, "industry": "agriculture"},
        {"id": 2, "industry": "agriculture"},
        {"id": 3, "industry": "solar energy"},
        {"id": 4, "industry": "solar energy"},
        {"id": 5, "industry": "bank"},
        {"id": 6, "industry": "bank"},
        {"id": 7, "industry": "mechanical engineering"},
        {"id": 8, "industry": "mechanical engineering"},
        {"id": 9, "industry": "translation"},
        {"id": 10, "industry": "translation"},
        {"id": 11, "industry": "finances"},
        {"id": 12, "industry": "finances"},
    ]


def test_filter_by_industry(jobs_for_filter_by_industry):
    industries = [
        "agriculture",
        "solar energy",
        "bank",
        "mechanical engineering",
        "translation",
        "finances",
    ]
    id_ = 1
    for industry in industries:
        jobs = filter_by_industry(jobs_for_filter_by_industry, industry)
        assert len(jobs) == 2
        assert jobs[0]["id"] == id_
        assert jobs[1]["id"] == id_ + 1
        id_ += 2
    jobs = filter_by_industry(jobs_for_filter_by_industry, "")
    assert len(jobs) == 0
