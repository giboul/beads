# Simulation numérique d'un court canal à billes

1. Effacer les simulations

```bash
./Allclean
```

2. Effacer les simulations

```bash
./Allrun
```

ou en parallèle

```bash
./Allrun_parallel
```

# Fonctionnement

- Les conditions de bord sont dans `0.orig`
- Les conditions initiales sont dans `system/setFieldsDict`
- Le mesh est controlé par `system/snappeHexMeshDict`, fichier formaté par le script `system/format_snappyHexMeshDict.py` à partir de la liste de centres dans `centers.txt`.
> Attention : le mesh ne se met pas toujours à jour si une des sphères déborde du domaine.

> Si vous avez arrêté une simulation en parallèle en cours, il est possible de la lire en relançant `./Allrun_parallel` qui sautera la simulation et reconstituera le mesh (si `./Allclean` n'a pas été exécuté).

> Pour juste observer le mesh : `./Allclean && ./Allrun_mesh`

L'analyse des résultats restera visuelle pour l'instant.
