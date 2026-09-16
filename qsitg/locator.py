import json

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


class QsitgGeocoderInterface(QgsGeocoderInterface):
    def geocodeString(self, string: str | None, _context, _feedback=None) -> list[QgsGeocoderResult]:
        if not string or len(string) < 3:
            return []

        query = QUrlQuery()
        query.addQueryItem("q", string)
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
        for hit in data["hits"]:
            result = QgsGeocoderResult(
                identifier=f"{hit['streetName']}, {hit['houseNumber']}",
                geometry=QgsGeometry.fromPoint(QgsPoint(hit["longitude"], hit["latitude"])),
                crs=QgsCoordinateReferenceSystem("EPSG:4326"),
            )
            result.setDescription(f"{hit['postalCode']} {hit['locality']} [{hit['administrativeDivision']}]")
            # result.setIcon(...) # not exposed by API and workaround is too cumbersome
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
            displayName="SITG",
            prefix="sitg",
            geocoder=self.geocoder,
            canvas=iface.mapCanvas(),
            boundingBox=QgsRectangle(),
        )
