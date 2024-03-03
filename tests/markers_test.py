import time
import pytest


@pytest.mark.slow
def test_slow_mark():
    time.sleep(4)
