import pytest
from src.insights.jobs import read


@pytest.fixture(scope="function", autouse=True)
def clear_cache():
    read.cache_clear()
