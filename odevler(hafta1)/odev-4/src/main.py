# ODEV 4: 1024x768 Boyutlandirma
from pathlib import Path

import cv2

project_root = Path(__file__).resolve().parents[1]
input_path = project_root / 'input' / 'image1.jpeg'
output_dir = project_root / 'output'
output_dir.mkdir(exist_ok=True)

resim = cv2.imread(str(input_path))
if resim is None:
    raise FileNotFoundError(f'Goruntu bulunamadi: {input_path}')

boyut = cv2.resize(resim, (1024, 768))
cv2.imwrite(str(output_dir / 'gorsel_1024x768.png'), boyut)
