# RDR2_supression_cache
un programme python permettant de supprimer les fichers cache de Red Dead Redemption 2


# 🎮 RDR2 — Nettoyeur de Cache D3D12

Script Python qui supprime automatiquement les fichiers de cache pipeline D3D12 de **Red Dead Redemption 2** pour éviter les problèmes de chargement liés à ces fichiers corrompus ou obsolètes.

---

##  Prérequis

- Python 3.7+
- Windows 10/11
- Red Dead Redemption 2 installé via Rockstar Games Launcher, sur steam ou encore cracké (tant que vous avez le jeu et le fichier rockstar game dans documents)

---

##  Fichiers supprimés

Le script cible les fichiers suivants dans le dossier `Settings` de RDR2 :

| Fichier | Description |
|--------|-------------|
| `sga_win32_60_final_init.d3d12PipelineCacheWindows` | Cache principal du pipeline D3D12 |
| `sga_win32_60_final_init.d3d12WarmupCacheWindows` | Cache de préchauffage D3D12 |
| `sga_win32_60_final_init.pipelineMarkerFile` | Marqueur de pipeline |

---

##  Utilisation

1. **Lancer le script avant ou pendant une session de jeu :**

```bash
python cleaner.py
```

2. Le script tourne en boucle et supprime les fichiers **toutes les 9 minutes**.

3. Il s'arrête automatiquement si les fichiers sont **absents depuis 5 cycles consécutifs** (soit ~45 minutes).

4. Pour arrêter manuellement : `Ctrl + C`

---

##  Exemple de sortie console

```
[14:32:01] Le fichier sga_win32_60_final_init.d3d12PipelineCacheWindows a été supprimé.
[14:32:01] Le fichier sga_win32_60_final_init.d3d12WarmupCacheWindows a été supprimé.
[14:32:01] Le fichier sga_win32_60_final_init.pipelineMarkerFile n'existe pas. 1
[14:32:01] attente de 9 min...
```

---

##  Configuration

Le chemin du dossier est défini en haut du script :

```python
dossier = Path(r"C:\Users\ALIENWARE\Documents\Rockstar Games\Red Dead Redemption 2\Settings")
```

>  **Modifie ce chemin** si ton profil Windows a un nom d'utilisateur différent.

---

##  Comportement en cas d'erreur

| Situation | Comportement |
|-----------|-------------|
| Fichier inexistant | Message informatif + incrémentation du compteur |
| Fichier verrouillé par un processus | Message d'avertissement, passage au suivant |
| Autre erreur | Affichage du message d'erreur complet |
| 5 cycles sans fichiers | Arrêt automatique du script |

---

##  Notes

- Le script est **non destructif** pour les sauvegardes ou paramètres du jeu.
- Les fichiers supprimés sont **régénérés automatiquement** par RDR2 au prochain lancement.
- Il est conseillé de le lancer **avant de démarrer** le jeu pour un nettoyage propre.

