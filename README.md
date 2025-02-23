# Générateur d'Images SVG pour Échiquiers

Ce projet contient un script Python qui génère des images SVG à partir de notations FEN d'échecs. Chaque image représente une position spécifique sur un échiquier et est sauvegardée dans un fichier SVG.

## Dépendances

Ce script utilise les bibliothèques `chess` et `os`. Pour installer la bibliothèque `chess`, qui est la seule dépendance externe, vous pouvez utiliser pip :

```bash
pip install chess
```

## Utilisation

Pour générer une image SVG à partir d'une notation FEN, vous pouvez exécuter le script `fentosvg.py` après avoir modifié la variable `fen` dans le script. Il est possible de mettre une liste de FENs dans la variable `fens` pour générer plusieurs images.

```bash
python fentosvg.py 
```

