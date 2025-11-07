import random

list1 = [7, 6, 4, 3, 2, 1]
print(random.choice(list1))


r1 = random.randint(5, 15)
print(r1)

r2 = random.random()
print(r2)

name = "Curso Python"
r2 = random.choice(name)
print(r2)

print(random.sample(list1, 2))
print(random.sample(list1, 3))

random.shuffle(list1)
print(list1)

done = False
while not done:
    print("O que você deseja fazer?")
    print("1 - Adivinha o número")
    print("2 - Sair")
    
    choice = int(input("> "))
    if choice == 1:
        number = int(input("Digite um número: "))
        result = random.randint(1, 10)
        
        if number == result:
            print("Parabens. Você acertou!")
            done = True
        else:
            print(f"Tente novamento o número sorteado foi {result}")
    elif(choice == 2):
        done = True
    else:
        print("Opção inválida, escolha 1 ou 2")