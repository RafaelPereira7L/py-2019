import time
import idk
def l():
    print ("\033[0;36m—————————————————————————————————————————————————")
l()
print("\033[0;37m(1) — DISTÂNCIA")
time.sleep(0.5)
print ("\033[0;33m        (1) — CALCULAR DISTÂNCIA EM METROS")
time.sleep(0.2) 
print ("\033[0;33m        (10) — CALCULAR VELOCIDADE EM m/s²")
time.sleep(0.2)
print ("\033[0;33m        (15) — CALCULAR TEMPO EM SEGUNDOS")
time.sleep(.5)








print("\033[0;37m\n(2) — PESO RELATIVO AO PLANETA TERRA")
time.sleep(.2)
print ("\033[0;33m        (2) — CALCULAR PESO")
time.sleep(.2)
print ("\033[0;33m        (25) — CALCULAR MASSA")
time.sleep(0.5)





print("\033[0;37m\n(3) — CONVERTER °C EM FARENHEIT")
time.sleep(0.2)
print("\n(4) — CONVERTER FARENHEIT EM °C")
time.sleep(0.2)
print("\n(5) — VELOCIDADE DE ONDAS")
print ("\033[0;33m        (5) — CALCULAR VELOCIDADE")
print ("\033[0;33m        (50) — CALCULAR COMPRIMENTO")
print ("\033[0;33m        (55) — CALCULAR FREQUÊNCIA")

time.sleep(0.2)
l()


forms= input("\033[0;37m\nESCOLHA QUAL CÁLCULO FÍSICO VOCÊ DESEJA CALCULAR:")
if forms==  '1':
    vel = float(input("\nDIGITE A VELOCIDADE: "))
    tempo = float(input("\nDIGITE O TEMPO: "))
    l()
    D = vel * tempo
    if D > 0:
        print ("\nA DISTÂNCIA É: ", D,)
    elif D < 0:
        print ("\033[0;31m\nERRO! NÃO EXISTE DISTÂNCIA NEGATIVA")
    l()
if forms==  '10':
    D = float(input("\nDIGITE A DISTÂNCIA EM METROS: "))
    tempo = float(input("\nDIGITE O TEMPO EM SEGUNDOS: "))
    l()
    vel = D/tempo
    if D > 0:
        print ("\nA VELOCIDADE É: ", vel, "m/s²")
    elif D < 0:
        print ("\033[0;31m\nERRO! NÃO EXISTE DISTÂNCIA NEGATIVA")
    l()
if forms==  '15':
    vel = float(input("\nDIGITE A VELOCIDADE EM m/s²: "))
    D = float(input("\nDIGITE A DISTÂNCIA EM METROS: "))
    l()
    tempo = D/vel
    if D > 0:
        print ("\nO TEMPO É: ", tempo,)
    elif D < 0:
        print ("\033[0;31m\nERRO! NÃO EXISTE DISTÂNCIA NEGATIVA")
    l()
    
    
    
    
    
    
    
    
    
        
        
        
if forms== '2':
    massa = float(input ("DIGITE A MASSA: "))
    gravidade = 9.8
    l()
    P = massa * gravidade
    if P > 0:
        print ("\nO PESO É: ", P,"N")
    elif P < 0:
        print ("\n\033[0;31mERRO! NÃO EXISTE PESO NEGATIVO")
        
        
if forms== '3':
    l()
    tc = float(input("\n\033[0;36mDIGITE A TEMPERATURA EM CELSIUS: "))
    l()
    tf = (tc/5) * 9 + 32
    if tc > -273:
        print ("\n\033[0;35mA TEMPERATURA EM FARENHEIT É: ", tf,)
        l()
if forms== '4':
    l()
    f = float(input("\n\033[0;35mDIGITE A TEMPERATURA EM FARENHEIT: "))
    l()
    c = ((f - 32)/9) * 5
    if c > -900:
    	    print ("\n\033[0;36mA TEMPERATURA EM °C É:",c,"°C")    
    	    l()    
if forms== '5':
    l()
    comp = float(input("\n\033[0;33mDIGITE O COMPRIMENTO DA ONDA: "))
    freq = float(input("\nDIGITE A FREQUÊNCIA EM HERTZ: "))
    l()
    V= comp * freq
    print ("\nA VELOCIDADE DA ONDA É: ",V, "m/s²")
    l()
    
    
    
    	
