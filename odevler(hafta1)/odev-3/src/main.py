# ODEV 3: Kuantalama (Quantization)
from pathlib import Path

import cv2
import numpy as np

project_root = Path(__file__).resolve().parents[1]
input_path = project_root / 'input' / 'image1.jpeg'
output_dir = project_root / 'output'
output_dir.mkdir(exist_ok=True)

resim = cv2.imread(str(input_path), 0)
if resim is None:
    raise FileNotFoundError(f'Goruntu bulunamadi: {input_path}')

satir, sutun = resim.shape
cikis = np.zeros((satir, sutun), dtype=np.uint8)

for i in range(satir):
    for j in range(sutun):
        cikis[i, j] = int(resim[i, j] // 4) * 4

cv2.imwrite(str(output_dir / 'kuantalama_sonuc.png'), cikis)
