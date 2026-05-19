import os
from typing import Any

from qgis.PyQt import QtWidgets, uic

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS: Any
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "qsitg_dialog_base.ui"))


class QsitgDialog(QtWidgets.QDialog, FORM_CLASS):
    """Main dialog window for the QSITG plugin."""

    def __init__(self, parent=None) -> None:
        """Initialize the dialog and load the Qt Designer interface."""
        super(QsitgDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
