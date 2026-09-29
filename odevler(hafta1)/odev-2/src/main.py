# ODEV 2: Pikselleri donguyle gezme ve (0.75 * piksel + 20) islemi
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
        deger = int(resim[i, j] * 0.75 + 20)
        if deger > 255:
            cikis[i, j] = 255
        elif deger < 0:
            cikis[i, j] = 0
        else:
            cikis[i, j] = deger

cv2.imwrite(str(output_dir / 'parlaklik_sonuc.png'), cikis)
