# ODEV 1: Cozunurluk yariya ve ceyrege indirme
from pathlib import Path

import cv2

project_root = Path(__file__).resolve().parents[1]
input_path = project_root / 'input' / 'image1.jpeg'
output_dir = project_root / 'output'
output_dir.mkdir(exist_ok=True)

resim = cv2.imread(str(input_path), 0)
if resim is None:
    raise FileNotFoundError(f'Goruntu bulunamadi: {input_path}')

h, w = resim.shape

yari = cv2.resize(resim, (int(w / 2), int(h / 2)))
ceyrek = cv2.resize(resim, (int(w / 4), int(h / 4)))

cv2.imwrite(str(output_dir / 'yari_boyut.png'), yari)
cv2.imwrite(str(output_dir / 'ceyrek_boyut.png'), ceyrek)
