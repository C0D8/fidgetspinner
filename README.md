# fidgetspinner
![Fidgetspinner (1)](https://user-images.githubusercontent.com/105286051/226206072-7c5bc9c4-0bad-497e-92ae-743de80fc841.gif)



### Utilização :

1. Clone o repositório 
2. Abra um novo terminal e instale os requisitos com 'pip install -r requirements.txt'

#### No arquivo demo.py é possível ter acesso as funcionalidades. Ao executar o arquivo a câmera será aberta em seu computador e as operações poderam ser realizadas:

- Ao clicar no botão 'd' a câmera começa a rotacionar para direita.
- Ao clicar no botão 'a' a câmera começa a rotacionar para esquerda.
- Ao clicar no botão 'w' a câmera começa a expandir a imagem no eixo y.
- Ao clicar no botão 's' a câmera começa a contrair a imagem no eixo y.
- Ao clicar no botão 'f' a câmera finaliza todos processos de transformação de imagem.
- Ao clicar no botão 'v' a matrix de rotação é voltada a seu estado inicial (caso o botão f tenha sido apertado, a câmera volta ao estado padrão).
- Ao clicar no botão 'q' a câmera é finalizada.

#### Contamos ainda com um arquivo exemplo.py que quando executado demonstra com exemplos de curta duração, cada uma das transformações desenvolvidas.

### Modelo matemático :

Para fazer as transformações apresentadas no programa utilizamos de alguns conceitos de trasformação de matrizes que serão explicitados a seguir:


#### Rotação :

para realizar a rotação, utilizamos uma matriz rotação de θ° que possui sua forma canônica :

$$
R = 
\begin{bmatrix}
    \cos(\theta) & -\sin(\theta) \\
    \sin(\theta) & \cos(\theta)  \\
\end{bmatrix}
$$

que gira a imagem para o sentido anti horário. Já para fazer a rotação para o sentido horário utilizamos a matriz inversa dessa, que realiza a mesma operação mas no sentido contrário. 

#### Expansão : 

Para realizar essa transformação, utilizamos a matriz de expansão no eixo x de forma canônica :

$$
\begin{bmatrix}
    a & 0\\
    0 & 1
\end{bmatrix}
$$

sendo assim, 'a' representa quanto a mais deve ser expandido no eixo x para essa transformação ser realizada na imagem.

#### Translação : 

Para realizar essa transformação como uma multiplicação de matrizes foi nescessário adicionar mais uma linha e coluna em nossas matrizes de transformação e mais uma linha contendo 1 em nossa matriz de resultado. Ficando com a seguinte estrutura : 


$$
\begin{bmatrix}
    a & b & \Delta x\\
    c & d & \Delta y \\
    0 & 0 & 1 \\
\end{bmatrix}
$$


Dessa forma, todas as transformações poderiam ficar em forma de multiplicação de matrizes o que permitiria concatenar diversas operações em uma matriz só, o que facilita muito ma hora de representar.



#### No código :


```
    cos15 = (np.sqrt(6)+np.sqrt(2))/4
    sin15 = (np.sqrt(6)-np.sqrt(2))/4
    R = np.array([[cos15, -sin15, 0], [sin15, cos15, 0], [0, 0,1]])
    R_left = np.array([[cos15, sin15, 0], [-sin15, cos15, 0], [0, 0,1]])
    m = np.array([[0.95,0,0],[0,1,0],[0,0,1]])
    M = np.array([[1.05,0,0],[0,1,0],[0,0,1]])
    rotation = np.array([[1,0,0],[0,1,0],[0,0,1]])

    T = np.array([[1, 0, -height/2], [0, 1, -width/2], [0, 0, 1]]) 
```


As variávies cos15 e sin15 representam o seno e o cosseno de 15° que são utilizados para a criação da matriz de rotação R cuja forma canônica foi explicitada anteriormente. Lembrando que devido a manipulação feita para adicionar a operação de translação foi preciso adicionar mais uma linha e coluna nessa matriz. 

Para fazer a rotação para a esquerda utilizamos a inversa da matriz para direita e armazenamos na variavel R_left. e as outras transformações de expansão e contração estão armazenadas nas variáveis m e M. 

Por último também criamos uma matriz para transladar o centro da imagem para o ponto (0,0) o que irá nos ajudar posteriormente com as operações de rotação.


Mais a frente no código temos  a variável C que armazena todas as transformações transformando tudo em apenas uma matriz, tal vantagem só é permitida devivo a manipulação das matrizes para a adição da operação de translação :


``` 
 C = np.linalg.inv(T) @ rotation @ T

```

Aqui transladamos a imagem para a origem (0,0) do vetor, rotacionamos e depois recolocamos a imagem na sua posição incial. Fazemos isso porque a operação de rotação acontece levando como centro o ponto (0,0).
