import json
import re

from qgis.core import (
    Qgis,
    QgsBlockingNetworkRequest,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsDistanceArea,
    QgsGeocoderContext,
    QgsGeocoderInterface,
    QgsGeocoderResult,
    QgsGeometry,
    QgsPoint,
    QgsPointXY,
    QgsProject,
    QgsRectangle,
)
from qgis.gui import QgsGeocoderLocatorFilter
from qgis.PyQt.QtCore import QUrl, QUrlQuery
from qgis.PyQt.QtNetwork import QNetworkRequest
from qgis.utils import iface

EGID_EGRID_PATTERN = r"^(?:CH)?\d+$"
EPSG_4326 = QgsCoordinateReferenceSystem("EPSG:4326")


class QsitgGeocoderInterface(QgsGeocoderInterface):
    def geocodeString(self, string: str | None, context: QgsGeocoderContext, _feedback=None) -> list[QgsGeocoderResult]:
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
            # error is already logged by QgsBlockingNetworkRequest
            return []

        reply = network.reply()
        data = json.loads(bytes(reply.content()))

        # Until sorting by focus point is implemented by the API we do it here
        # (see https://gitlab.com/sitg-lab/geocoding/sitg-geocoder/-/work_items/32)
        tfx = QgsCoordinateTransform(context.areaOfInterestCrs(), EPSG_4326, QgsProject.instance())
        focus = tfx.transform(context.areaOfInterest().centroid().asPoint())
        d = QgsDistanceArea()
        d.setEllipsoid("WGS84")
        sorted_hits = sorted(
            data["hits"],
            key=lambda hit: (-hit["score"], d.measureLine(focus, QgsPointXY(hit["longitude"], hit["latitude"]))),
        )

        results = []
        for i, hit in enumerate(sorted_hits):
            # The locator sorts results alphabetically (see https://github.com/qgis/QGIS/issues/67497).
            if Qgis.versionInt() >= 40000:
                # until fixed, we prepend a zero-width character to keep ordering
                _order = "\u200b" * (len(data["hits"]) - i)
            else:
                # under QGIS 3.x \u200b doesn't affect the order, let's show a number...
                _order = f"{i + 1:2d}. "
            result = QgsGeocoderResult(
                identifier=f"{_order}{hit['streetName']}, {hit['houseNumber']}",
                geometry=QgsGeometry.fromPoint(QgsPoint(hit["longitude"], hit["latitude"])),
                crs=EPSG_4326,
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
