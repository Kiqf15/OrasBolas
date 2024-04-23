from random import uniform
import unicodedata
import math
import os

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
finalizar = 0
print("\n" * 130)
os.system("start chrome http://localhost:8080/")
while(finalizar == 0 or finalizar == 2):
    if(finalizar == 2):
        print("\n" * 130)
        os.system("start Graficos.exe")
        print("-------------------Dados-------------------")
        print("Ponto de inicio Robo: X {}, Y {}".format(round(Xr/100,4),round(Yr/100,4)))
        print("Ponto de encontro: X {}, Y {}".format(round(Xfinal/100,4),round(Yfinal/100,4)))
        print("Tempo de encontro: {}s".format(Tfinal))
        print("Tempo Robo: {}s".format(round(Tr,4)))
        print("Distancia Percorrida: {}m".format(round(dist_robo_bola/100,4)))
        print("-------------------------------------------")
        print()
    while(True):
        print("-------------------Opções-------------------")
        print("1 - Gerar pontos aleatórios")
        print("2 - Escolher pontos manualmente")
        print("3 - Finalizar programa")
        print("--------------------------------------------")
        escolha = int(input(""))
        if(escolha != 1 and escolha!= 2 and escolha!= 3):
            print("\n" *130)
            print("Input invalido, por favor digite novamente.\n")
        else:
            break
    
    if(escolha == 3):
        finalizar = 1
    else:
        print()
        #-----------------------------Calculo do ponto de encontro--------------------
        dist_centro = 101
        Yr = -1
        while(True):
            print("-------------------Opções-------------------")
            print("1 - Obedecer limites")
            print("2 - Ignorar limites")
            print("--------------------------------------------")
            regras = int(input(""))
            os.system("taskkill /f /im Graficos.exe")
            if(regras != 1 and regras!= 2):
                print("\n" *130)
                print("Input invalido, por favor digite novamente.\n")
            else:
                break

        if(escolha == 1):
            if(regras == 1):
                while((dist_centro > 91 or dist_centro < -109 or Yr < 9)):
                    Xr = uniform(0.09,1.91)
                    Yr = uniform(0.09,1.41)
                    
                    # Adequação ao padrão canvas
                    Xr = Xr*100
                    Yr = Yr*100
                    Xbi = 1 * 100
                    Ybi = 0.5 * 100
                    
                    dist_centro = math.sqrt((Xbi-Xr)**2+(Ybi-Yr)**2)
            elif(regras == 2):
                Xr = uniform(0.09,8.91)
                Yr = uniform(0.09,5.91)
                
                # Adequação ao padrão canvas
                Xr = Xr*100
                Yr = Yr*100
                
        #----------------------------------PONTO FIXO------------------------
        elif(escolha == 2):
            if(regras == 1):
                print("\n"*130)
                while((dist_centro > 91 or dist_centro < -109 or Yr < 9)):
                    Xr = float(input("Escolha o ponto X: "))
                    Yr = float(input("Escolha o ponto Y: "))
                    
                    # Adequação ao padrão canvas
                    Xr = Xr*100
                    Yr = Yr*100
                    Xbi = 1 * 100
                    Ybi = 0.5 * 100
                    
                    dist_centro = math.sqrt((Xbi-Xr)**2+(Ybi-Yr)**2)
                    if((dist_centro > 91 or dist_centro < -109 or Yr < 9)):
                        print("\n"*130)
                        print("Escolha invalida! Lembre-se dos limites de 1m de distância da bola.")
            elif(regras == 2):
                print("\n"*130)
                while(True):
                    Xr = float(input("Escolha o ponto X: "))
                    Yr = float(input("Escolha o ponto Y: "))
                    
                    if((Xr < 0.09 or Xr > 8.91) or (Yr < 0.09 or Yr > 5.91)):
                        print("\n"*130)
                        print("Escolha invalida, lembre-se dos limites do campo (9x6 m)\n")
                    else:
                        break
                
                # Adequação ao padrão canvas
                Xr = Xr*100
                Yr = Yr*100
                
        for i in range(len(X_bola)):
            X_bola_teste = X_bola[i] * 100
            Y_bola_teste = Y_bola[i] * 100
            
            
            dist_robo_bola = math.sqrt((X_bola_teste-Xr)**2+(Y_bola_teste-Yr)**2)
            # ??????????????????????????????  Raio de interceptação   ????????????????????????
            # raio_interceptação = 0.15 * 100
            # dist_robo_bola -= 11.15 + raio_interceptação
            
            
            velocidade_robo = 280
            if (dist_robo_bola >= 140):
                Tr = ((dist_robo_bola-140) / velocidade_robo) + 1
            else:
                Tr = math.sqrt(dist_robo_bola*2/velocidade_robo)
                

            if(T_bola[i] >= Tr):
                Xfinal = X_bola_teste
                Yfinal = Y_bola_teste
                Tfinal = T_bola[i]
                finalizar = 2
                break
            
            if(i == 1000):
                print("Ponto de encontro inexistente!")


        #-----------------------------Tranferindo ponto de encontro para txt---------------

        # Verificando se ja existe um arquivo se sim apagar
        try:
            with open('ponto_de_encontro.txt', 'r') as f:
                f.close()
                os.remove('ponto_de_encontro.txt')
                arquivo = open("ponto_de_encontro.txt", "w");
        except IOError:
            arquivo = open("ponto_de_encontro.txt", "w");
            
        arquivo.write("{} {} {} {}".format(Xr,Yr, X_bola_teste, Y_bola_teste))

        arquivo.close()
        # -----------------Gera os pontos em que o robo passa para chegar na bola----------------
        
        X_robo = []
        Y_robo = []
        T_robo = []
        cronometro = 0.00
        velocidade_pontual = 0
        aceleracao = 280
        sen = (Yfinal - Yr)/dist_robo_bola
        cos = (Xfinal - Xr)/dist_robo_bola
        for i in range(int(Tfinal/0.02)):
            cronometro += 0.02
            if(cronometro >= Tfinal):
                break
            # cronometro = round(cronometro,2)
            if (cronometro < 1):
                dist_ponto = (aceleracao*(cronometro**2))/2
            else:
                dist_ponto = (velocidade_robo * (cronometro-1)) + 140
            
            X_robo.append((cos*dist_ponto) + Xr)
            Y_robo.append((sen*dist_ponto) + Yr)
            T_robo.append(cronometro)
        
        # Verificando se ja existe um arquivo se sim apagar
        try:
            with open('trajetoria_robo.txt', 'r') as f:
                os.remove('trajetoria_robo.txt')
                arquivo = open("trajetoria_robo.txt", "w");
        except IOError:
            arquivo = open("trajetoria_robo.txt", "w");
        
        # Gera o arquivo com a tragetória do robo
        arquivo.write("x/m y/m t/s\n")
        for i in range(len(X_robo)):
            arquivo.write("{} {} {}\n".format(round(X_robo[i]/100,4),round(Y_robo[i]/100,4),round(T_robo[i],4)))
        arquivo.close()
        
        # -----------------Gera os pontos em que a bola passa para chegar no gol----------------
        
        X_chute = []
        Y_chute = []
        T_chute = []
        cronometro = 0.00
        X_inicial_chute = ((X_robo[-1]/100) * 10) + 4
        Y_inicial_chute = ((Y_robo[-1]/100) * 10) + 2
        print(X_inicial_chute)
        print(Y_inicial_chute)
        velocidade_chute = 28
        X_gol = 85
        Y_gol = 30
        dist_bola_gol = math.sqrt((X_gol-X_inicial_chute)**2+(Y_gol-Y_inicial_chute)**2)
        print("Distancia até o gol: " + str(dist_bola_gol))
        Tempo = dist_bola_gol/velocidade_chute
        print("Tempo até o gol: " + str(Tempo))
        
        cos = (X_gol - X_inicial_chute)/dist_bola_gol
        sen = (Y_gol - Y_inicial_chute)/dist_bola_gol
        print(int(Tempo/0.02))
        for i in range(int(Tempo/0.02)):
            
            dist_ponto = velocidade_robo * cronometro
            
            X_chute.append((cos*dist_ponto) + X_inicial_chute)
            Y_chute.append((sen*dist_ponto) + Y_inicial_chute)
            T_chute.append(cronometro)
            if(X_chute[-1] >= X_gol and Y_chute[-1] >= Y_gol):
                X_chute.append((cos*dist_ponto) + X_inicial_chute)
                Y_chute.append((sen*dist_ponto) + Y_inicial_chute)
                T_chute.append(cronometro)
                break
        
            cronometro += 0.02
        # Verificando se ja existe um arquivo se sim apagar
        try:
            with open('trajetoria_chute.txt', 'r') as f:
                os.remove('trajetoria_chute.txt')
                arquivo = open("trajetoria_chute.txt", "w");
        except IOError:
            arquivo = open("trajetoria_chute.txt", "w");
        
        # Gera o arquivo com a tragetória do robo
        arquivo.write("x/m y/m t/s\n")
        for i in range(len(X_chute)):
            arquivo.write("{} {} {}\n".format(round(X_chute[i],4),round(Y_chute[i],4),round(T_chute[i],4)))
        arquivo.close()
        
os.system("taskkill /f /im server.exe")