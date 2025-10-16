# Plugin QGIS SITG

Plugin QGIS permettant de distribuer des resources pour le SITG.

![screenshot](screenshot.png)

Pour le moment, le plugin permet la configuration pour les endpoints vector.sitg.ge.ch, raster.sitg.ge.ch, thematique.sitg.ge.ch, à chaque fois avec ou sans authentification OAuth2, ainsi que les tuiles vectorielles.

## Installer

En attendant sa mise à disposition via le dépôt d'extension officiel de QGIS, le plus est installable via un dépôt temporaire dédié.

1. Dans le gestionnaire d'extensions, onglet paramètre, ajouter le dépot `https://github.com/republique-et-canton-de-geneve/qgis_plugin_sitg/releases/latest/download/plugins.xml`
2. Rechercher le plugin `qsitg` et l'installer

Si l'installation a fonctionné, un nouveau sous-menu devraît être apparu dans le menu `Extensions`.

## Aide / en cas de problème

N'hésitez pas à ouvrir une issue github pour signaler un problème.

## Contribuer

Les contributions au plugin sont bienvenues sous forme de pull request. Avant de vous lancer dans un développement complexe, prenez contact avec nous en créant une issue afin de discuter de l'idée, pour s'assurer que la contribution puisse être intégrée au plugin officiel.

### Environnement de développement

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

### Packager

Pour déclencher le packaging et la release d'une nouvelle version, créer une release dans github. Le nom de la release doit suivre les conventions de version sémantique. Les pre-releases (p. ex. `1.2.3-alpha1`) seront automatiquement packagées comme expérimentales.
