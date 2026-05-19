# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Qsitg class from file Qsitg.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qsitg import Qsitg

    return Qsitg(iface)
