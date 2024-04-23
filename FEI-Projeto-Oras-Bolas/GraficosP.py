import matplotlib.pyplot as plt
import numpy as np
import unicodedata
from math import sqrt


def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")


tragetoria_bola = open("Ora_bolas-trajetoria_bola_oficial.txt", "r")
dados = tragetoria_bola.readlines()
tragetoria_bola.close()


#-------------------------------Formatação de dados da bola-------------------
dados_formatados = []
for linha in dados:
    linha = remove_control_characters(linha)
    if linha == "":
        continue
    dados_formatados.append(linha)
dados_formatados.pop(0)

#Separar os dados da bola em listas
T_bola = []
X_bola = []
Y_bola = []
for linha in dados_formatados:
    counter = 0
    tipo = 0
    dado = ""
    for char in linha:
        if(counter > 0):
            dado+=char
            if counter == 2 and tipo == 0:
                T_bola.append(float(dado))
                tipo = 1
                dado = ""
                counter = 0
            elif counter == 3 and tipo == 1:
                X_bola.append(float(dado))
                tipo = 2
                dado = ""
                counter = 0
            elif counter == 3 and tipo == 2:
                Y_bola.append(float(dado))
                tipo = 0
                dado = ""
                counter = 0
            if counter > 0:
                counter += 1
        elif (char == ","):
            dado += "."
            counter = 1
        else:
            dado += char

tragetoria_robo = open("trajetoria_robo.txt", "r")
dados = tragetoria_robo.readlines()
tragetoria_robo.close()

#-------------------------------Formatação de dados do robo-------------------
T_robo = []
X_robo = []
Y_robo = []
dados.pop(0)
for linha in dados:
  linha = linha.split(" ")
  X_robo.append(float(linha[0]))
  Y_robo.append(float(linha[1]))
  T_robo.append(float(linha[2]))

#-------------------------------Formatação de dados do contato-------------------

contador = 0
T_bola_contato = []
X_contato = []
Y_contato = []
for i in range(len(T_bola)):
  contador += 1
  if T_bola[i] > T_robo[-1]:
    break
for i in range(contador):
  X_contato.append(X_bola[i])
  Y_contato.append(Y_bola[i])
  T_bola_contato.append(T_bola[i])

#-------------------------------Formatação da vel/acl -------------------
vel_robo = []
vel_robo_X = []
vel_robo_Y = []
T_gasto_robo = []
acl_robo = []
acl_robo_X = []
acl_robo_Y = []
for i in range(1,len(X_robo)):
    dist = sqrt((X_robo[i]-X_robo[i-1])**2+(Y_robo[i]-Y_robo[i-1])**2)
    dist_X = sqrt((X_robo[i]-X_robo[i-1])**2)
    dist_Y = sqrt((Y_robo[i]-Y_robo[i-1])**2)
    Tempo_gasto = float(T_robo[i]) - float(T_robo[i-1])
    velocidade = dist/Tempo_gasto
    velocidade_X = dist_X/Tempo_gasto
    velocidade_Y = dist_Y/Tempo_gasto
    
    T_gasto_robo.append(float(Tempo_gasto))
    vel_robo.append(float(velocidade))
    vel_robo_X.append(float(velocidade_X))
    vel_robo_Y.append(float(velocidade_Y))
    

for i in range(1,len(vel_robo)):
    vel_rel = vel_robo[i] - vel_robo[i-1]
    vel_rel_X = vel_robo_X[i] - vel_robo_X[i-1]
    vel_rel_Y = vel_robo_Y[i] - vel_robo_Y[i-1]
    aceleracao = vel_rel/T_gasto_robo[i]
    aceleracao_X = vel_rel_X/T_gasto_robo[i]
    aceleracao_Y = vel_rel_Y/T_gasto_robo[i]
    
    
    acl_robo.append(float(aceleracao))
    acl_robo_X.append(float(aceleracao))
    acl_robo_Y.append(float(aceleracao))



vel_bola = []
vel_bola_X = []
vel_bola_Y = []
acl_bola = []
acl_bola_X = []
acl_bola_Y = []  
T_gasto_bola = []
for i in range(1,len(X_contato)):
    dist = sqrt((X_contato[i]-X_contato[i-1])**2+(Y_contato[i]-Y_contato[i-1])**2)
    dist_X = sqrt((X_contato[i]-X_contato[i-1])**2)
    dist_Y = sqrt((Y_contato[i]-Y_contato[i-1])**2)
    Tempo_gasto = float(T_bola_contato[i]) - float(T_bola_contato[i-1])
    velocidade = dist/Tempo_gasto
    velocidade_X = dist_X/Tempo_gasto
    velocidade_Y = dist_Y/Tempo_gasto
    
    T_gasto_bola.append(float(Tempo_gasto))
    vel_bola.append(float(velocidade))
    vel_bola_X.append(float(velocidade_X))
    # vel_bola_X.append(0.5)
    vel_bola_Y.append(float(velocidade_Y))
    # vel_bola_Y.append(0.5)
    
    
for i in range(1,len(vel_bola)):
    vel_rel = vel_bola[i] - vel_bola[i-1]
    vel_rel_X = vel_bola_X[i] - vel_bola_X[i-1]
    vel_rel_Y = vel_bola_Y[i] - vel_bola_Y[i-1]
    aceleracao = vel_rel/T_gasto_bola[i]
    aceleracao_X = vel_rel_X/T_gasto_bola[i]
    aceleracao_Y = vel_rel_Y/T_gasto_bola[i]
    
    
    acl_bola.append(float(aceleracao))
    # acl_bola.append(0)
    acl_bola_X.append(float(aceleracao))
    # acl_bola_X.append(0)
    acl_bola_Y.append(float(aceleracao))
    # acl_bola_Y.append(0)

#-----------------------------Formatação da Distancia relativa -------------------
dist_relativa = []
for i in range(len(X_robo)):
    dist = sqrt((X_robo[i]-X_bola[i-1])**2+(Y_robo[i]-Y_bola[i-1])**2)
    dist_relativa.append(dist)


# Plot 1

  
xbola_inicial = np.array(X_bola)
ybola_inicial = np.array(Y_bola)
xcontato = np.array(X_contato)
ycontato = np.array(Y_contato)
xrobo = np.array(X_robo)
yrobo = np.array(Y_robo)

plt.subplot(3, 4, 1)
plt.plot(xrobo, yrobo,color = 'CornflowerBlue')
plt.plot(xbola_inicial, ybola_inicial, ls = '--', color = 'Grey')
plt.plot(xcontato, ycontato,color = 'DarkOrange')

plt.title("Interceptação Robo x Bola")
plt.xlabel("Posição em X")
plt.ylabel("Posição em Y")
plt.legend(["Robo","Futuro","bola"])
plt.grid()

# Plot 2.1

xcontato = np.array(X_contato)
tcontato = np.array(T_bola_contato)
xrobo = np.array(X_robo)
trobo = np.array(T_robo)

plt.subplot(3, 4, 2)
plt.plot(trobo, xrobo,color = 'CornflowerBlue')
plt.plot(tcontato, xcontato,color = 'DarkOrange')

plt.title("Interceptação Robo x Bola em X")
plt.xlabel("Tempo")
plt.ylabel("Posição x")
plt.grid()

# Plot 2.2

ycontato = np.array(Y_contato)
tcontato = np.array(T_bola_contato)
yrobo = np.array(Y_robo)
trobo = np.array(T_robo)

plt.subplot(3, 4, 3)
plt.plot(trobo, yrobo,color = 'CornflowerBlue')
plt.plot(tcontato,ycontato,color = 'DarkOrange')

plt.title("Interceptação Robo x Bola em Y")
plt.xlabel("Tempo")
plt.ylabel("Posição Y")
plt.grid()


T_robo.pop(0)
vel_bola.pop(-1)
vel_bola.pop(-1)
vel_bola_X.pop(-1)
vel_bola_X.pop(-1)
vel_bola_Y.pop(-1)
vel_bola_Y.pop(-1)
acl_bola.pop(-1)
acl_bola.pop(-1)
acl_bola_X.pop(-1)
acl_bola_X.pop(-1)
acl_bola_Y.pop(-1)
acl_bola_Y.pop(-1)
dist_relativa.pop(-1)
dist_relativa.pop(-1)

# Plot 3.1
velrobo = np.array(vel_robo)
velbola = np.array(vel_bola)
trobo = np.array(T_robo)

plt.subplot(3, 4, 4)
plt.plot(trobo, velrobo,color = 'CornflowerBlue')
plt.plot(trobo, velbola,color = 'DarkOrange')

plt.title("Velocidade Robo x Bola")
plt.xlabel("Tempo")
plt.ylabel("Velocidade")
plt.grid()

# Plot 3.2

velroboX = np.array(vel_robo_X)
velbolaX = np.array(vel_bola_X)
trobo = np.array(T_robo)

plt.subplot(3, 4, 5)
plt.plot(trobo, velroboX,color = 'CornflowerBlue')
plt.plot(trobo,velbolaX,color = 'DarkOrange')

plt.title("Velocidade Robo x Bola em X")
plt.xlabel("Tempo")
plt.ylabel("Velocidade X")
plt.grid()

# Plot 3.3

velroboY = np.array(vel_robo_Y)
velbolaY = np.array(vel_bola_Y)
trobo = np.array(T_robo)

plt.subplot(3, 4, 6)
plt.plot(trobo, velroboY,color = 'CornflowerBlue')
plt.plot(trobo,velbolaY,color = 'DarkOrange')

plt.title("Velocidade Robo x Bola em Y")
plt.xlabel("Tempo")
plt.ylabel("Velocidade Y")
plt.grid()

# Plot 4.1

T_robo.pop(-1)
aclrobo = np.array(acl_robo)
aclbola = np.array(acl_bola)
trobo = np.array(T_robo)

plt.subplot(3, 4, 7)
plt.plot(trobo, aclrobo,color = 'CornflowerBlue')
plt.plot(trobo, aclbola,color = 'DarkOrange')

plt.title("Aceleração Robo x Bola")
plt.xlabel("Tempo")
plt.ylabel("Aceleração")
plt.grid()

# Plot 4.2

aclroboX = np.array(acl_robo_X)
aclbolaX = np.array(acl_bola_X)
trobo = np.array(T_robo)

plt.subplot(3, 4, 8)
plt.plot(trobo, aclroboX,color = 'CornflowerBlue')
plt.plot(trobo,aclbolaX,color = 'DarkOrange')

plt.title("Aceleração Robo x Bola em X")
plt.xlabel("Tempo")
plt.ylabel("Aceleração X")
plt.grid()

# Plot 4.3

aclroboY = np.array(acl_robo_Y)
aclbolaY = np.array(acl_bola_Y)
trobo = np.array(T_robo)

plt.subplot(3, 4, 9)
plt.plot(trobo, aclroboY,color = 'CornflowerBlue')
plt.plot(trobo,aclbolaY,color = 'DarkOrange')

plt.title("Aceleração Robo x Bola em Y")
plt.xlabel("Tempo")
plt.ylabel("Aceleração Y")
plt.grid()

# Plot 5
DistRel = np.array(dist_relativa)
trobo = np.array(T_robo)

plt.subplot(3, 4, 10)
plt.plot(trobo, DistRel,color = 'Brown',label='Distância')

plt.title("Ditância Relativa Robo x Bola")
plt.xlabel("Tempo")
plt.ylabel("Distância Relativa")
plt.grid()


plt.tight_layout()
manager = plt.get_current_fig_manager()
# manager.full_screen_toggle()
plt.suptitle("Oras Bolas")
plt.show()
