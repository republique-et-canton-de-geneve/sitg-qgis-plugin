import json
import re

from qgis.core import (
    Qgis,
    QgsBlockingNetworkRequest,
    QgsCoordinateReferenceSystem,
    QgsGeocoderInterface,
    QgsGeocoderResult,
    QgsGeometry,
    QgsPoint,
    QgsRectangle,
)
from qgis.gui import QgsGeocoderLocatorFilter
from qgis.PyQt.QtCore import QUrl, QUrlQuery
from qgis.PyQt.QtNetwork import QNetworkRequest
from qgis.utils import iface

from .utils import log

EGID_EGRID_PATTERN = r"^(?:CH)?\d+$"


class QsitgGeocoderInterface(QgsGeocoderInterface):
    def geocodeString(self, string: str | None, _context, _feedback=None) -> list[QgsGeocoderResult]:
        if not string or len(string) < 3:
            return []

        query = QUrlQuery()
        query.addQueryItem("q", string)
        if not re.match(EGID_EGRID_PATTERN, string):
            query.addQueryItem("suggest", "true")
        url = QUrl("https://geocodage.sitg-lab.ch/api/v2/search")
        url.setQuery(query)
        request = QNetworkRequest(url)
        network = QgsBlockingNetworkRequest()

        error = network.get(request)
        if error != QgsBlockingNetworkRequest.NoError:
            log(f"{network.errorMessage()}", Qgis.MessageLevel.Error)
            return []

        reply = network.reply()
        data = json.loads(bytes(reply.content()))

        results = []
        for i, hit in enumerate(data["hits"]):
            # The locator sorts results alphabetically (see https://github.com/qgis/QGIS/issues/67497).
            # Until this is fixed, we prepend a zero-width character to keep ordering.
            _order = "\u200b" * (len(data) - i)
            result = QgsGeocoderResult(
                identifier=f"{_order}{hit['streetName']}, {hit['houseNumber']}",
                geometry=QgsGeometry.fromPoint(QgsPoint(hit["longitude"], hit["latitude"])),
                crs=QgsCoordinateReferenceSystem("EPSG:4326"),
            )
            result.setDescription(f"{hit['postalCode']} {hit['locality']} [{hit['administrativeDivision']}]")
            # Icons aren't supported yet (see https://github.com/qgis/QGIS/issues/67498)
            # result.setIcon(...)
            results.append(result)

        return results

    def wkbType(self) -> Qgis.WkbType:
        return Qgis.WkbType.Point

    def flags(self):
        return QgsGeocoderInterface.Flag.GeocodesStrings


class QsitgGeocoderLocatorFilter(QgsGeocoderLocatorFilter):
    def __init__(self):
        self.geocoder = QsitgGeocoderInterface()
        super().__init__(
            name="SITG",
            displayName="SITG - Service de géocodage",
            prefix="sitg",
            geocoder=self.geocoder,
            canvas=iface.mapCanvas(),
            boundingBox=QgsRectangle(),
        )
