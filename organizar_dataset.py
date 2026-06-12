"""
Organiza o dataset fruit quality em data/fresh/ e data/rotten/.
Copia apenas imagens originais (sem prefixo de augmentação),
limitando a N_POR_CLASSE imagens por classe para balanceamento.
"""
import shutil
from pathlib import Path

BASE   = Path(__file__).parent
TRAIN  = BASE / 'data' / 'dataset' / 'train'
FRESH  = BASE / 'data' / 'fresh'
ROTTEN = BASE / 'data' / 'rotten'
N_POR_CLASSE = 100   # altere se quiser mais imagens

FRESH.mkdir(parents=True, exist_ok=True)
ROTTEN.mkdir(parents=True, exist_ok=True)

PREFIXOS_IGNORAR = ('rotated_', 'saltandpepper_', 'translation_', 'vertical_flip_')

def originais(pasta: Path):
    imgs = []
    for f in sorted(pasta.iterdir()):
        if f.suffix.lower() in ('.png', '.jpg', '.jpeg'):
            if not any(f.name.startswith(p) for p in PREFIXOS_IGNORAR):
                imgs.append(f)
    return imgs

# Coleta imagens de todas as frutas
fresh_imgs  = []
rotten_imgs = []

for subpasta in sorted(TRAIN.iterdir()):
    if 'fresh' in subpasta.name.lower():
        fresh_imgs.extend(originais(subpasta))
    elif 'rotten' in subpasta.name.lower():
        rotten_imgs.extend(originais(subpasta))

print(f"Originais encontradas — fresh: {len(fresh_imgs)}, rotten: {len(rotten_imgs)}")

# Balanceia e copia
n = min(N_POR_CLASSE, len(fresh_imgs), len(rotten_imgs))
print(f"Copiando {n} imagens por classe...")

for i, src in enumerate(fresh_imgs[:n]):
    dst = FRESH / f"fresh_{i:04d}{src.suffix}"
    shutil.copy2(src, dst)

for i, src in enumerate(rotten_imgs[:n]):
    dst = ROTTEN / f"rotten_{i:04d}{src.suffix}"
    shutil.copy2(src, dst)

print(f"\nPronto!")
print(f"  data/fresh/  → {len(list(FRESH.iterdir()))} imagens")
print(f"  data/rotten/ → {len(list(ROTTEN.iterdir()))} imagens")
