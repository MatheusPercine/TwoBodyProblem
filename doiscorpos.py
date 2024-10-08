# Nome: Matheus da Cruz Percine Pinto
# DRE: 121068501

import turtle
import math

# Constantes L, G e c
L = pow(10, 5)
G = 6.7 * pow(10, -11)
c = pow(10, 6)

# Função para calcular r
# Função baseada no que foi dito no enunciado:
# "achar a solução do problema reduzido usando o que aprendemos na seção 7 do capítulo 2 da apostila"
def CalcularR(teta, e, p):
    r = p / (1 + e * math.cos(teta))
    return r

# Função para calcular as posições r1 e r2
# Função baseada no que foi dito no enunciado:
# "achar as coordenadas das posições de cada corpo conforme o que aprendemos na seção 4 do capítulo 3 da apostila"
def CacularPosicoes(teta, e, p, m1, m2):
    r = CalcularR(teta, e, p)
    r1 = -(m2 * r) / (m1 + m2)  # Posição da Terra
    r2 = (m1 * r) / (m1 + m2)   # Posição da Lua
    return r1, r2

# Função para desenhar os corpos em cada quadro
def AtualizarPosicoes(teta, e, p, m1, m2, ESCALA, corpo1, corpo2):
    r1, r2 = CacularPosicoes(teta, e, p, m1, m2)

    # Convertendo para coordenadas cartesianas
    # novas coordenadas do corpo1
    x1 = r1 * math.cos(teta) * ESCALA
    y1 = r1 * math.sin(teta) * ESCALA
    # novas coordenadas do corpo2
    x2 = r2 * math.cos(teta) * ESCALA
    y2 = r2 * math.sin(teta) * ESCALA

    #atualização de posições
    corpo1.goto(x1, y1)
    corpo2.goto(x2, y2)


def Animacao1():

    m1 = 5.972 * pow(10, 24)  # Massa da Terra (kg)
    m2 = 7.348 * pow(10, 22)  # Massa da Lua (kg)
    k = G * (m1 + m2)
    p = pow(L, 2) / k
    e = 0.0549  # Excentricidade da órbita da Lua

    # Configuração da tela de animação
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Simulação da Órbita Terra-Lua")

    # Configuração dos corpos em orbita
    terra = turtle.Turtle()
    terra.shape("circle")
    terra.color("blue")
    terra.shapesize(1.5)
    terra.penup()

    lua = turtle.Turtle()
    lua.shape("circle")
    lua.color("gray")
    lua.shapesize(0.6)
    lua.penup()

    # Configuração do centro de massa (fixo no centro da tela)
    cm = turtle.Turtle()
    cm.shape("circle")
    cm.color("white")
    cm.shapesize(0.3)
    cm.penup()
    cm.goto(0, 0)

    # ESCALA aumentada para ampliar a distância visual entre Terra e Lua
    # considerando que distância entre a Terra e a Lua é cerca de 384,400 km
    ESCALA = 3.84 * pow(10, 6)  # 1 unidade na simulação = 100 km

    # Animação
    teta = 0
    while True:
        AtualizarPosicoes(teta, e, p, m1, m2, ESCALA, terra, lua)
        teta += 0.01  # Incremento do ângulo
        if teta > 2 * math.pi:
            teta = 0  # Reinicia o ciclo da órbita caso teta é maior que 2*pi


def Animacao2():

    m1 = 5* pow(10,24)
    m2 = 7* pow(10,23)
    k = G * (m1 + m2)
    p = pow(L, 2) / k
    e = 0.8

    # Configuração da tela de animação
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Simulação 2 corpos")

    # Configuração dos corpos em orbita
    terra = turtle.Turtle()
    terra.shape("circle")
    terra.color("yellow")
    terra.shapesize(1.5)
    terra.penup()

    lua = turtle.Turtle()
    lua.shape("circle")
    lua.color("red")
    lua.shapesize(0.6)
    lua.penup()

    # Configuração do centro de massa (fixo no centro da tela)
    cm = turtle.Turtle()
    cm.shape("circle")
    cm.color("white")
    cm.shapesize(0.3)
    cm.penup()
    cm.goto(0, 0)

    # ESCALA arbitrária para ampliar a distância visual entre corpo1 e corpo2 e facilitar a visualizacao
    ESCALA = 2 * pow(10, 6)

    # Animação
    teta = 0
    while True:
        AtualizarPosicoes(teta, e, p, m1, m2, ESCALA, terra, lua)
        teta += 0.01  # Incremento do ângulo
        if teta > 2 * math.pi:
            teta = 0  # Reinicia o ciclo da órbita caso teta é maior que 2*pi

if __name__ == "__main__":
    print("Digite '1' ou '2' para escolher uma das animações")
    print("animação 1: terra-lua")
    print("animação 2: utilizando os dados do exemplo do enunciado da atividade") 
    # Quanto a opção 2, me refiro exatamente a seguinte parte do enunciado da atividade do classroom:
    # "Na minha versão optei por usar a solução analítica do problema de Kepler dada na seção 7. Na notação da apostila, usei os seguintes dados:
    # L:10^5; G:6.7*10^(-11); c:10^6;
    # m1:5*10^(24);  
    # m2:7*10^(23);
    # k:G*(m1+m2); p:L^2/k; e: 0.8;"

    opcao = int(input())

    if opcao == 1:
        Animacao1()
    
    if opcao == 2:
        Animacao2()