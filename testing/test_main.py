import unittest

from qgis.PyQt.QtCore import QModelIndex
from qgis.PyQt.QtWidgets import QDockWidget, QTreeView
from qgis.utils import iface, plugins

from qsitg.qsitg import Qsitg


class SmokeTests(unittest.TestCase):
    def test_plugin_loads(self):
        """Smoketest to ensure the plugin correctly loads."""
        self.assertCountEqual(plugins.keys(), ["qsitg", "db_manager", "MetaSearch", "processing", "grassprovider"])


class MainTests(unittest.TestCase):
    def test_reconfigure_populates_browser(self) -> None:
        """Testing that reconfiguring geoservices correctly populates the browser."""
        qsitg: Qsitg = plugins["qsitg"]

        browser = iface.mainWindow().findChild(QDockWidget, "Browser")
        browser.show()
        treeview = browser.findChild(QTreeView)
        model = treeview.model()

        def _visit_browser_items(parent_index=None, path="", result=None):
            if parent_index is None:
                parent_index = QModelIndex()
            if result is None:
                result = []
            for row in range(model.rowCount(parent_index)):
                index = model.index(row, 0, parent_index)
                name = index.data()
                current = f"{path}/{name}" if path else str(name)
                result.append(current)
                _visit_browser_items(index, current, result)
            return result

        original_list = _visit_browser_items()

        # reconfiguring correctly populates the browser
        qsitg.do_reset_geoservices(with_auth=False)
        self.assertCountEqual(
            _visit_browser_items(),
            [
                *original_list,
                "Vector Tiles/SITG - Plan SITG (clair)",
                "Vector Tiles/SITG - Plan SITG (défaut)",
                "Vector Tiles/SITG - Plan SITG (gris)",
                "Vector Tiles/SITG - Plan SITG (sombre)",
                "ArcGIS REST Servers/SITG - raster.sitg.ge.ch",
                "ArcGIS REST Servers/SITG - thematic.sitg.ge.ch",
                "ArcGIS REST Servers/SITG - vector.sitg.ge.ch",
            ],
        )

        # reconfiguring again this time with auth updates the browser
        qsitg.do_reset_geoservices(with_auth=True)
        self.assertCountEqual(
            _visit_browser_items(),
            [
                *original_list,
                "Vector Tiles/SITG - Plan SITG (clair)",
                "Vector Tiles/SITG - Plan SITG (défaut)",
                "Vector Tiles/SITG - Plan SITG (gris)",
                "Vector Tiles/SITG - Plan SITG (sombre)",
                "ArcGIS REST Servers/SITG - raster.sitg.ge.ch - [auth]",
                "ArcGIS REST Servers/SITG - thematic.sitg.ge.ch - [auth]",
                "ArcGIS REST Servers/SITG - vector.sitg.ge.ch - [auth]",
            ],
        )
