AUTH_SETTING_ID = "sitgOA2"
ARCGISFEATURESERVERS = {
    "vector.sitg.ge.ch": {
        "url": "https://vector.sitg.ge.ch/arcgis/rest/services/Hosted/",
        "authcfg": AUTH_SETTING_ID,
    },
    "raster.sitg.ge.ch": {
        "url": "https://raster.sitg.ge.ch/arcgis/rest/services/",
        "authcfg": AUTH_SETTING_ID,
    },
    "thematic.sitg.ge.ch": {
        "url": "https://thematic.sitg.ge.ch/arcgis/rest/services/",
        "authcfg": AUTH_SETTING_ID,
    },
}
VECTORTILES = {
    "Plan SITG (défaut)": {
        "url": "https://app2.ge.ch/tergeoservices/rest/services/Hosted/PLAN_SITG_EPSG2056/VectorTileServer",
        "styleUrl": "",
        "service-type": "arcgis",
        "zmin": 0,
        "zmax": 14,
    },
    "Plan SITG (clair)": {
        "url": "https://app2.ge.ch/tergeoservices/rest/services/Hosted/PLAN_SITG_EPSG2056/VectorTileServer",
        "styleUrl": "https://app2.ge.ch/tergeoportal/sharing/rest/content/items/00da7582e4c64800805f75cac362306d/resources/styles/root.json",
        "service-type": "arcgis",
        "zmin": 0,
        "zmax": 14,
    },
    "Plan SITG (gris)": {
        "url": "https://app2.ge.ch/tergeoservices/rest/services/Hosted/PLAN_SITG_EPSG2056/VectorTileServer",
        "styleUrl": "https://app2.ge.ch/tergeoportal/sharing/rest/content/items/843a4f8a3b2544b0ba0a25d52daa616a/resources/styles/root.json",
        "service-type": "arcgis",
        "zmin": 0,
        "zmax": 14,
    },
    # Same as "Plan SITG (défaut)"
    # "Plan SITG (contrasté)": {
    #     "url": "https://app2.ge.ch/tergeoservices/rest/services/Hosted/PLAN_SITG_EPSG2056/VectorTileServer",
    #     "styleUrl": "https://app2.ge.ch/tergeoportal/sharing/rest/content/items/434118b9fff344909a7f438fb8f62dde/resources/styles/root.json",
    #     "service-type": "arcgis",
    #     "zmin": 0,
    #     "zmax": 14,
    # },
    "Plan SITG (sombre)": {
        "url": "https://app2.ge.ch/tergeoservices/rest/services/Hosted/PLAN_SITG_EPSG2056/VectorTileServer",
        "styleUrl": "https://app2.ge.ch/tergeoportal/sharing/rest/content/items/753d065ee1ba4d29be9a6de655abd94f/resources/styles/root.json",
        "service-type": "arcgis",
        "zmin": 0,
        "zmax": 14,
    },
}
