import pytest
import os
import requests

@pytest.fixture(scope = "session")
def file_dir():
    return os.path.join(os.path.dirname(__file__),"tests", "test_files")


@pytest.fixture
def sample_file(file_dir):
    return os.path.join(file_dir, "sample.txt")

@pytest.fixture
def large_file(file_dir):
    return os.path.join(file_dir, "large_file.txt")


