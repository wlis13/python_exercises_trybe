import pytest
from typing import List


@pytest.fixture
def my_list() -> List[int]:
    return [1, 2, 3]
