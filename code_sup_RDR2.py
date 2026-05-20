import time
from pathlib import Path
from datetime import datetime

compteur= 0
dossier= Path(r"C:\Users\ALIENWARE\Documents\Rockstar Games\Red Dead Redemption 2\Settings")

fichiers = [
    "sga_win32_60_final_init.d3d12PipelineCacheWindows",
    "sga_win32_60_final_init.d3d12WarmupCacheWindows",
    "sga_win32_60_final_init.pipelineMarkerFile",
]

while True:
    for nom_fichier in fichiers:
        chemin_fichier = dossier / nom_fichier
        if chemin_fichier.exists():
            try:
                chemin_fichier.unlink()
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Le fichier {nom_fichier} a été supprimé.")
            except PermissionError:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Le fichier {nom_fichier} est actuellement utilisé par un autre processus et ne peut pas être supprimé.")
            except Exception as erreur:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] erreur avec le fichier {nom_fichier}: {erreur}")
        else:
            compteur= compteur+1
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Le fichier {nom_fichier} n'existe pas. {compteur}")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] attente de 9 min...")
    time.sleep(540)
    if compteur >=5:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Le fichier n'existe pas depuis 5 itérations, arrêt du script.")
        break
    
    