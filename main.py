numero = 7
permitido = 3
tentativa = 0

while tentativa < permitido:
    palpite = int(input("digite o número que você acredita ser o correto:"))
    tentativa +=1
    if palpite == numero:
        print("Parabéns! Você acertou.")
        break
else:
    print("Você perdeu. Tente Novamente, e acredite na sua intuição.")

