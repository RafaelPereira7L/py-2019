import time
import idk
def linha():
    print ("\n\n    \033[0;37m    ******************************")
linha()
print ("\n\n    \033[0;31m   *            ÁREAS            *")
linha()
time.sleep(0.5)
print("\n\n      *      DEVELOPED BY  \033[0;31mcxxlt.xyz   \033[0;37m  *")
time.sleep(0.5)
linha()
time.sleep(0.5)
print ("\n\033[0;34mQ - QUADRADO.    ▀")
time.sleep(0.5)
print ("\n\033[0;36mR - RETÂNGULO.   ▬")
time.sleep(0.5)
print ("\n\033[0;38mT - TRIÂNGULO.   ∆	")
time.sleep(0.5)
print ("\n\033[0;33mTR - TRAPÉZIO.   π")
time.sleep(0.5)
linha()
v=str(input("\n\nESCOLHA UMA OPÇÃO: ")) .upper()
if v== 'Q':
    lado = float(input("\nDIGITE O TAMANHO DO LADO: "))
    AREAQ = lado * lado
    linha()
    if AREAQ > 0:
        print ("\n \nÁREA DO QUADRADO >> ", AREAQ, "m²")
    if AREAQ <= 0:
        print ("\n\n ERRO! NÃO É POSSÍVEL CALCULAR A ÁREA DO QUADRADO.")
    linha()
    
if v==  'R':
    base = float(input("\nDIGITE O TAMANHO DA BASE: "))
    altura = float(input("\nDIGITE O TAMANHO DA ALTURA: "))
    AREARET = base * altura
    linha()
    if AREARET > 0:
        print ("\n \nÁREA DO RETÂNGULO >> ", AREARET, "m²")
    if AREARET <= 0:
        print ("\n\n ERRO! NÃO É POSSÍVEL CALCULAR A ÁREA DO RETÂNGULO.")
    linha()
if v== 'T':
    baset = float(input("\nDIGITE O TAMANHO DA BASE:" ))
    alturat = float(input("\nDIGITE O TAMANHO DA ALTURA: "))
    AREAT = baset * alturat /2
    linha()
    if AREAT > 0:
        print ("\n\nÁREA DO TRIÂNGULO >> ", AREAT, "m²")
        linha()
    if AREAT <= 0:
            print ("\n\n ERRO! NÃO É POSSÍVEL CALCULAR A ÁREA DO TRIÂNGULO.")
            linha()
            
if v== 'TR':
    basemaior = float(input("\nDIGITE O TAMANHO DA BASE MAIOR: "))
    basemenor = float(input("\nDIGITE O TAMANHO DA BASE MENOR: "))
    alturatr = float(input("\nDIGITE O TAMANHO DA ALTURA: "))
    AREATR = ((basemaior + basemenor) * alturatr)/2
    linha()
    if AREATR > 0:
        print ("\n\n ÁREA DO TRAPÉZIO >> ", AREATR, "m²")
        linha()
    if AREATR <= 0:
        print ("\n\n ERRO! NÃO É POSSÍVEL CALCULAR A ÁREA DO QUADRADO.")
        linha()