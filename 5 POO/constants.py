import os
from pathlib import Path

# CUR_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(CUR_DIR, "data")
CUIR_DIR = Path(__file__).parent
DATA_DIR = CUIR_DIR / "data"

print("DOSSIER COURANT: ", CUIR_DIR)
print("DOSSIER DONNEES: ", DATA_DIR)
