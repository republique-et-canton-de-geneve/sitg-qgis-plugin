# Plugin QGIS SITG

Ce repo pour démontrer un plugin custom pour le SITG, qui pourrait p. ex. packager des configs par défaut pour les serveurs, des styles, un accès au catalogue web, etc...

## Packager

TODO: faire ça dans une CI.

En attendant, recompiler les resources (icons, fichiers ui...) puis zipper
```ps1
# hors proxy

# recompiler les resources
uv run --with PyQt5 pyrcc5 -o qsitg/resources.py qsitg/resources.qrc

# créer le zip
python -c "import shutil; shutil.make_archive('qsitg', 'zip', '.', 'qsitg')"
```

## Ajouter au repo interne

Un repo interne peut être hébergé sur le NAS.

Ajouter un XML sur le NAS sous
`V:\Donnees_Applicatives\GEOMATIQUE\INTERNET\SITG\QGIS\plugins.xml` (voir https://gis.stackexchange.com/a/486204/8512 pour un exemple)

Ajouter le repo dans QGIS:
`https://ge.ch/sitg/geodata/SITG/QGIS/plugins.xml`
