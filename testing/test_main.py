from qgis.utils import plugins


def test_plugin_loads():
    """Smoketest to ensure the plugin correctly loads."""
    assert set(plugins.keys()) == {"qsitg", "db_manager", "MetaSearch", "processing", "grassprovider"}
