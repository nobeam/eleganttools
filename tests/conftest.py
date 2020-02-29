import pytest
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
DATA_PATH = BASE_PATH / "data"
DEMO_SDDS = DATA_PATH / "demo.sdds"


@pytest.fixture
def base_path():
    return BASE_PATH


@pytest.fixture
def data_path():
    return DATA_PATH


@pytest.fixture
def demo_sdds():
    return DEMO_SDDS
