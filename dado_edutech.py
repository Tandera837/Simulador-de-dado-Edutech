from random import randint

while True:
    sn = input('\033[32;40mQuer rodar o dado? S/N:\033[m ').strip().upper()
    if sn in 'N':
        break
    elif sn in 'S':
        print('\033[33;40mVocê rodou o número ' , randint(1, 6), '\033[m')
    else:
        print('\033[31;40mNão sabe escrever "S" ou "N" não?\033[m')
print('\033[31;40mVocê parou de rodar o dado\033[m')

