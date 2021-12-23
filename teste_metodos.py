# from PIL import Image
# import PIL.ImageOps    
# import numpy as np
# import cv2

# metodos = [
#     cv2.THRESH_BINARY,
#     cv2.THRESH_BINARY_INV,
#     cv2.THRESH_TRUNC,
#     cv2.THRESH_TOZERO,
#     cv2.THRESH_TOZERO_INV
# ]

# ### Transformar Imagem em escala de cinza
# imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
# ###
# # for i in metodos:
        
   
# #     cv2.imwrite(f'testesmetodos/imagem_tratada_{i}.png', imagem_tratada)
# _, imagem_tratada_bina =  cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY) 
# _, imagem_tratada_trunc =  cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_TRUNC)  
# #imagem2 = cv2.imread(r'C:\DEV\Python\CAPTCHA\testesmetodos\imagem_tratada_2.png') 
# # cv2.imshow('original',imagem)
# # cv2.imshow('preta_branca_tras',imagem_tratada_trunc)
# # cv2.imshow('preta_branca_binary',imagem_tratada_bina)

# (linha, colunas) = imagem_tratada_trunc.shape

# for l in range(linha):
#     for c in range(colunas):
#         cor_pixel = imagem_tratada_trunc((l,c))
#         print(l,c,'==>',cor_pixel)



# cv2.waitKey(10000)
# cv2.destroyAllWindows()


from PIL import Image
import PIL.ImageOps    
import numpy as np
import cv2

imagem = cv2.imread(r"C:\DEV\Python\CAPTCHA\bdcaptcha\telanova0.png")
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
Image2 = np.array(imagem, copy=True)

white_px = np.asarray([255, 255, 255])
black_px = np.asarray([0  , 0  , 0  ])

(row, col) = imagem_cinza.shape

for r in range(row):
    for c in range(col):
        px = imagem_cinza[r][c]
        if all(px == white_px):
            Image2[r][c] = black_px

i = 1

cv2.imwrite('testesmetodos/imagem_tratada_1.png',Image2)
