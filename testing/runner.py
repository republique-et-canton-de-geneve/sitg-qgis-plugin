"""Starts the test suite from within QGIS.

It should be run with the --code command line argument
"""

import os
import sys

import pytest
from qgis.core import QgsApplication
from qgis.utils import loadPlugin, startPlugin

print("Starting tests...")
sys.stdout.flush()

# Prevent master password prompt for popping up
QgsApplication.authManager().setMasterPassword("1234", verify=False)

# Enable the plugin
print("Enabling the plugin...")
loadPlugin("qsitg")
startPlugin("qsitg")

# Run the tests
exit_code = pytest.main(["/testing/", "-vv"])

# Exit with code
print(f"Finished tests. Exit code: {exit_code}")
os._exit(exit_code)
