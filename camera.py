import numpy as np

# Instalar a biblioteca cv2 pode ser um pouco demorado. Não deixe para ultima hora!
import cv2 as cv


def criar_indices(min_i, max_i, min_j, max_j):
    import itertools
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack( (idx_i, idx_j) )
    return idx

def run():
    # Essa função abre a câmera. Depois desta linha, a luz de câmera (se seu computador tiver) deve ligar.
    cap = cv.VideoCapture(0)

    # Aqui, defino a largura e a altura da imagem com a qual quero trabalhar.
    # Dica: imagens menores precisam de menos processamento!!!
    width = 320
    height = 240

    # Talvez o programa não consiga abrir a câmera. Verifique se há outros dispositivos acessando sua câmera!
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()


    #Criação do seno e cosseno de 15 e criação das matrizes de transformação e rotação.
    cos15 = (np.sqrt(6)+np.sqrt(2))/4
    sin15 = (np.sqrt(6)-np.sqrt(2))/4
    R = np.array([[cos15, -sin15, 0], [sin15, cos15, 0], [0, 0,1]])
    R_left = np.array([[cos15, sin15, 0], [-sin15, cos15, 0], [0, 0,1]])
    m = np.array([[0.95,0,0],[0,1,0],[0,0,1]])
    M = np.array([[1.05,0,0],[0,1,0],[0,0,1]])
    rotation = np.array([[1,0,0],[0,1,0],[0,0,1]])

    T = np.array([[1, 0, -height/2], [0, 1, -width/2], [0, 0, 1]])

    
    # Esse loop é igual a um loop de jogo: ele encerra quando apertamos 'q' no teclado.
    while True:
        # Captura um frame da câmera
        ret, frame = cap.read()

        # A variável `ret` indica se conseguimos capturar um frame
        if not ret:
            print("Não consegui capturar frame!")
            break

        # Mudo o tamanho do meu frame para reduzir o processamento necessário
        # nas próximas etapas
        frame = cv.resize(frame, (width,height), interpolation =cv.INTER_AREA)

        # A variável image é um np.array com shape=(width, height, colors)
        image = np.array(frame).astype(float)/255


        #Aqui criamos um array com o shape da variavel image mas com zero em todas as posições para poder plotar nossa imagem final.
        image_ = np.zeros_like(image)

        #Aqui criamos os destinos dos pontos que desejamos, fazemos isso para ajudar posteriormente a fazer a operação inversa e eliminar os glitchs da imagem final.
        Xd = criar_indices(0, height, 0, width)
        Xd = np.vstack ( (Xd, np.ones( Xd.shape[1]) ) )

        # Aqui criamos uma matriz concatenando algumas transformações: translação para centralizar a imagem no eixo 0,0 para assim realizar a rotação e depois trasladar a imagem para a posição inicial. 
        C = np.linalg.inv(T) @ rotation @ T


        #Aqui selecionamos os pixels da origem da nossa imagem final realizando a operação inversa anteriomente comentada.
        X = np.linalg.inv(C) @ Xd


        #Aplicamos um filtro para eliminar os pixels que eventualmente saiam do quadro da nossa imagem.
        filtro = (X[0,:] >= 0) & (X[0,:] < image_.shape[0]-1) & (X[1,:] >= 0) & (X[1,:] < image_.shape[1]-1)
        Xd = Xd[:, filtro]
        X = X[:,filtro]   

        # Transformamos os resultados em inteiros já que estamos trabalhando com intervalos discretos, não eciste meio pixel.      
        Xd = Xd.astype(int)
        X = X.astype(int)


        #Aqui fazemos a "transposição" dos pixels que selecionamos da iamgem de origem para a imagem de destino. 
        image_[Xd[0,:], Xd[1,:], :] = image[X[0,:], X[1,:], :]

        #Agora, mostrar a imagem na tela!
        cv.imshow('Minha Imagem!', image_)

        #caso uma waitkey seja apertada
        wk = cv.waitKey(33)

        #executa a função de determinada tecla
        if wk:
            #rotação no sentido antihorário
            if wk == ord('d'):
                rotation = R @ rotation
            #rotação sentido horário
            elif wk == ord('a'):
                rotation = R_left @ rotation
            #expansão 
            elif wk == ord('w'):
                rotation = M @ rotation
            #contração
            elif wk == ord('s'):
                rotation = m @ rotation
            #voltar para a imagem original
            elif wk == ord('v'):
                rotation = np.array([[1,0,0],[0,1,0],[0,0,1]])
            # Se aperto 'q', encerro o loop
            elif wk == ord('q'):
                break
    
    # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
    cap.release()
    cv.destroyAllWindows()

run()
