"""Starts the test suite from within QGIS.

It should be run with the --code command line argument
"""

import os
import sys

import pytest
from pyplugin_installer.installer import loadPlugin

print("Starting tests...")
sys.stdout.flush()

# Enable the plugin
print("Enabling the plugin...")
loadPlugin("qsitg")

# Run the tests
exit_code = pytest.main(["/testing/", "-vv"])

# Exit with code
print(f"Finished tests. Exit code: {exit_code}")
os._exit(exit_code)
