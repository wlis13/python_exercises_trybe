import pytest
from typing import List


@pytest.fixture
def my_list() -> List[int]:
    return [1, 2, 3]


@pytest.fixture
def high_list() -> List[int]:
    return [1, 2, 3, 4, 5]


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow")
