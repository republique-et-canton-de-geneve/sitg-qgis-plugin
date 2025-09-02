# Plugin QGIS SITG

Plugin QGIS permettant de distribuer des resources pour le SITG.

![screenshot](screenshot.png)

Pour le moment, le plugin permet la configuration pour les endpoints vector.sitg.ge.ch, raster.sitg.ge.ch, thematique.sitg.ge.ch (avec et sans authentification OAuth2) et les tuiles vectorielles.

## Installer

Le plugin est installable via un dépôt dédié sur le NAS (en attendant release dans le dépôt d'extension officiel).

1. Dans le gestionnaire d'extensions, onglet paramètre, ajouter le dépot `https://ge.ch/sitg/geodata/SITG/QGIS/plugins.xml`
2. Rechercher le plugin `qsitg` et l'installer

Si l'installation a fonctionné, un nouveau sous-menu devraît être apparu dans le menu `Extensions`.

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

Pour faire une nouvelle version, éditer `metadata.txt` avec la nouvelle version, puis recompiler les resources (icons, fichiers ui...) puis zipper comme cela:

```ps1
# hors proxy

# recompiler les resources
uv run --with PyQt5 pyrcc5 -o qsitg/resources.py qsitg/resources.qrc

# créer le zip
python -c "import shutil; shutil.make_archive('qsitg', 'zip', '.', 'qsitg')"
```

Copier le zip vers `V:\Donnees_Applicatives\GEOMATIQUE\INTERNET\SITG\QGIS\qsitg.zip` puis modifier la version dans `plugins.xml` (du même dossier) avec la même version que dans `metadata.txt`.

`plugins.xml` est un dépôt de plugins personalisé, un exemple de fichier est disponible [ici](https://gis.stackexchange.com/a/486204/8512).
