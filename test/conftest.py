from urllib.parse import urljoin
import os

import pytest


def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="http://localhost:5000")


@pytest.fixture(scope="session")
def host(request):
    return request.config.getoption("--host")


@pytest.fixture(scope="session")
def api_v1_host(host):
    # return urljoin(host, "api", "v1")
    return "/".join([host, "api", "v1"])
