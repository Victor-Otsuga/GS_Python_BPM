import time

idade = input("Digite sua idade: ")
i = 0
j = 0
med = [0,0,0,0,0]
bpm = 0
msg = ""

def alarm(extra):
    resp = input(f"Seu batimento cárdiaco está {extra} BPM's a cima\n"
          f"da média, está tudo bem? (Y) sim ou (N) não")
    if resp == 'n':
        print("Estamos ligando para seu contato de emergência!")
        exit()
def Frequency(media):
    freq = 0
    for i in range(len(media)):
        freq += media[i]
    freq = freq * 12
    return freq

def Verify(ppm):
    if int(idade) < 4:
        min = 120
        max = 140
    elif int(idade) < 13:
        min = 75
        max = 118
    elif int(idade) < 18:
        min = 80
        max = 100
    elif int(idade) < 40:
        min = 70
        max = 80
    else:
        min = 50
        max = 60

    if int(ppm) > (max+40):
        alarm(ppm-max)

    if int(ppm) < min:
        return("Seu batimento cárdiaco está a baixo da média")
    elif int(ppm) >max:
        return ("Seu batimento cárdiaco está a cima da média")
    else:
        return ("Seu batimento cárdiaco está OK")

while not idade.isnumeric():
    idade = input("Digite sua idade: ")

card = [1,2,1,2,3,2,1,2,1,2,1,2,3,1,2,3,1,2,1,2,1,2,1,1,2,5,5,5,5,5,3,1,1,2,1,2,1,2,1,2,3,2,1,2,1,2,1,2,3,1,2,3,1,2,1,2,1,2,1,1,2,3,1,1,2,1,2,1,2,1,2,3,2,1,2,1,2,1,2,3,1,2,3,1,2,1,2,1,2,1,1,2,3,1,1,2,1,2,1,2,1,2,3,2,1,2,1,2,1,2,3,1,2,3,1,2,1,2,1,2,1,1,2,3,1,1,2,1,2]

while i < len(card):
    if j >= 5:
        j = 0

    med[j] = card[i]
    print(med)
    time.sleep(1)
    i += 1
    j += 1
    if i>4:
        bpm = Frequency(med)
        print(f"A frequencia cárdiaca é de {bpm}BPM")
        msg = Verify(bpm)
        print(msg)
