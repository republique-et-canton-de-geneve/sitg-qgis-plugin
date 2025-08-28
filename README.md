# Plugin QGIS SITG

Ce repo pour démontrer un plugin custom pour le SITG, qui pourrait p. ex. packager des configs par défaut pour les serveurs, des styles, un accès au catalogue web, etc...

## Environnement de développement

Pré-requis: UV et QGIS.

```sh
# créer un environnement virtuel préconfiguré pour QGIS grâce à https://github.com/GispoCoding/qgis-venv-creator
uvx --from qgis-venv-creator create-qgis-venv.exe --venv-name .venv

# installer l'outillage de développement
uv pip install -r requirements-dev.txt

# installer l'auto-formatteur
# FIXME: désactivé car ça marche pas avec l'envionnment créé par qgis-venv-creator on dirait...
# à la place on peut lancer manuellement `uvx run pre-commit run --all-files`
# uv run pre-commit install
```

Puis dans VSCode, s'assurer d'activer l'environnement `.env` avec la commande `Python: Selec interpreter`.


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
