import os
import cv2
import glob

arquivos = glob.glob('arquivos_ok/*')
for arquivo in arquivos:
    imagem = cv2.imread(arquivo)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    _, nova_imagem = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY_INV)

    contornos, _ = cv2.findContours(nova_imagem,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    regiao_letras = []

    #Filtro Contorno das Letras
    for contorno in contornos:
        (x,y,l,a) = cv2.boundingRect(contorno)
        area = cv2.contourArea(contorno)
        if area > 115:
            regiao_letras.append((x,y,l,a))

    #Caso a quantidade seja menor que 5 descarta a img
    if len(regiao_letras) !=5:
         continue

    #Desenhar os contronos e separar letras
    imagem_final = cv2.merge([imagem]*3) 
    i = 1
    for retangulo in regiao_letras:        
        x, y, l, a = retangulo
        imagem_letra = imagem[y-2:y+a+2 , x-2:x+l+2]
        nome_arquivo = os.path.basename(arquivo).replace("png",f"letra{i}.png")
        i = i+1
        cv2.imwrite(f'letras/{nome_arquivo}',imagem_letra)
        cv2.rectangle(imagem_final,(x-2, y-2),(x+l+2,y+a+2),(0,0,255),(2) )

    nome_arquivo = os.path.basename(arquivo)
    cv2.imwrite(f"identificados/{nome_arquivo}", imagem_final)    