import os
import pytest


@pytest.fixture(scope="session")
def base_url():
    return os.getenv(
        "PARABANK_BASE_URL",
        "https://parabank.parasoft.com/parabank"
    )


@pytest.fixture(scope="session")
def test_username():
    return os.getenv("PARABANK_USERNAME", "")


@pytest.fixture(scope="session")
def test_password():
    return os.getenv("PARABANK_PASSWORD", "")
