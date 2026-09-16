from qgis.core import Qgis, QgsMessageLog


def log(message, level=Qgis.MessageLevel.Info):
    """Push log message with level."""
    QgsMessageLog.logMessage(message, "qsitg", level)
