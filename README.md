# fidgetspinner
![Fidgetspinner (1)](https://user-images.githubusercontent.com/105286051/226206072-7c5bc9c4-0bad-497e-92ae-743de80fc841.gif)



### Utilização :

1. Clone o repositório 
2. Abra um novo terminal e instale os requisitos com 'pip install -r requirements.txt'

#### No arquivo demo.py é possível ter acesso as funcionalidades. Ao executar o arquivo a câmera será aberta em seu computador e as operações poderam ser realizadas:

- Ao pressionar o botão 'd' a câmera é rotacionada a direita.
- Ao pressionar o botão 'a' a câmera é rotacionada a esquerda.
- Ao pressionar o botão 'w' a câmera é expandida em altura.
- Ao pressionar o botão 's' a câmera é contraída em altura.
- Ao pressionar o botão 'v' a câmera é voltada a seu estado inicial.
- Ao pressionar o botão 'q' a câmera é finalizada.

### Contamos ainda com um arquivo exemplo.py que quando executado demonstra com exemplos de curta duração, cada uma das transformações desenvolvidas.

### Modelo matemático :

Para fazer as transformações apresentadas no programa utilizamos de alguns conceitos de trasformação de matrizes que serão explicitados a seguir:


#### Rotação :

para realizar a rotação, utilizamos uma matriz rotação de θ° que possui sua forma canônica :

$$
R = 
\begin{bmatrix}
    \cos(\theta) & -\sin(\theta) \\
    \cos(\theta) & \sin(\theta)  \\
\end{bmatrix}
$$

que gira a imagem para o sentido anti horário. Já para fazer a rotação para o sentido horário utilizamos a matriz inversa dessa, que realiza a mesma operação mas no sentido contrário. 




#### Translação : 

Para realizar essa transformação como uma multiplicação de matrizes foi nescessário adicionar mais uma linha e coluna em nossas matrizes de transformação e mais uma linha contendo 1 em nossa matriz de resultado. Ficando com a seguinte estrutura : 


$$
\begin{bmatrix}
    a & b\\
    c & d
\end{bmatrix}
\begin{bmatrix}
    x \\
    y
\end{bmatrix}
+
\begin{bmatrix}
    \Delta x \\
    \Delta y
\end{bmatrix}
=
\begin{bmatrix}
    p \\
    q
\end{bmatrix}
$$


Dessa forma, todas as transformações poderiam ficar em forma de multiplicação de matrizes o que permitiria concatenar diversas operações em uma matriz só, o que facilita muito ma hora de representar.




#### Expansão : 

Para realizar essa transformação, utilizamos a matriz de expansão no eixo x de forma canônica :

$$
\begin{bmatrix}
    a & 0\\
    0 & 1
\end{bmatrix}
$$

sendo assim, 'a' representa quanto a mais deve ser expandido no eixo x para essa transformação ser realizada na imagem.