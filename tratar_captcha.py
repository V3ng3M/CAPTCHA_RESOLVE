import cv2
import os
import glob
from PIL import Image    
import numpy as np
import cv2

def tratar_imagens(pasta_origem, pasta_destino='arquivos_ok'):
    arquivos = glob.glob(f"{pasta_origem}/*")
    for arquivo in arquivos:
        Image = cv2.imread(arquivo)
        Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
        _,Image = cv2.threshold(Image, 127, 255, cv2.THRESH_BINARY)
        Image2 = np.array(Image, copy=True)
        Image3 = np.array(Image, copy=True)
        Image4 = np.array(Image, copy=True)
        white_px = np.asarray([255, 255, 255])
        black_px = np.asarray([0  , 0  , 0  ])
        medio = np.asarray([99,99,99])
        (row, col, _) = Image.shape
        for r in np.arange(row):
            for c in np.arange(col):
                px = Image[r][c]
            # print(px)
                if all(px < medio):
                    Image2[r][c] = black_px
                px2 = Image2[r][c]
                if all(px2 > black_px):
                    Image3[r][c] = white_px
                px3 = Image3[r][c]
                if all(px3 <= white_px):
                    Image4[r][c] = black_px
        nome_arquivo = os.path.basename(arquivo)
        cv2.imwrite(f"{pasta_destino}/{nome_arquivo}", Image3)

if __name__ == "__main__":
    tratar_imagens("bdcaptcha")