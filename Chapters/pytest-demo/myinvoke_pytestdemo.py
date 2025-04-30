# -*- coding: latin-1 -*-

import sys
import pytest

class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")


if __name__ == "__main__":
    #sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))
    exit_code = pytest.main(["test_compare.py"])
    print("Pytest exit code", exit_code)

