import random
import time

vida_boss = 500
pokemons = {"1": 100, "2": 100, "3": 100}
energia = {"charmander": 100, "squirtle": 100, "bulbassauro": 100}

print("Esse jogo é um RPG de turnos baseado em pokémon")
time.sleep(3)
print("Você precisa derrotar o boss, ele tem 500 de vida")
time.sleep(3)
print("Cada pokémon seu tem vida e energia, 100 pra cada status")
time.sleep(3)
print("Cada ataque tira um pouco de energia de seu pokémon")
time.sleep(3)
print("Bom, agora que você já leu a introdução, boa batalha!!!")
time.sleep(3)

while True:   
    escolha = input("\nQual pokémon você escolhe? (charmander = 1 | squirtle = 2 | bulbasaur = 3) ")
    
    if escolha == "1":
        if "1" not in pokemons:
            print("Charmander foi derrotado, ele não pode mais batalhar!")
            time.sleep(2)
            continue
            
        time.sleep(1)

        opc_ataque = input("Qual ataque você quer escolher?\n(1: Sopro Flamejante [Dano 50, Energia 40] | 2: Chamas [Dano 35, Energia 10] | 3: Descansar) -> ")
        
        if opc_ataque == "1":
            if energia["charmander"] >= 40:
                energia["charmander"] -= 40
                time.sleep(0.5)
                print("Você escolheu Sopro flamejante!!")
                vida_boss -= 50
            else:
                print("Sem energia suficiente! Você perdeu o turno tentando atacar.")
                time.sleep(1)
                continue

        elif opc_ataque == "2":
            if energia["charmander"] >= 10:
                energia["charmander"] -= 10
                time.sleep(0.5)
                print("Você escolheu chamas!!")
                vida_boss -= 35
            else:
                print("Sem energia suficiente! Você perdeu o turno tentando atacar.")
                time.sleep(1)
                continue

        elif opc_ataque == "3":
            time.sleep(0.5)
            energia["charmander"] = min(100, energia["charmander"] + 50)
            print(f"Charmander descansou, agora sua energia é {energia['charmander']}/100")
        else:
            print("Ataque inválido! Você perdeu a vez.")
            time.sleep(1)
            continue
            
        time.sleep(1)
        print(f"A vida do boss agora é {max(0, vida_boss)}/500!!")
        time.sleep(1)

    elif escolha == "2":
        if "2" not in pokemons:
            print("Squirtle foi derrotado, ele não pode mais batalhar!")
            time.sleep(2)
            continue
            
        time.sleep(1)
        opc_ataque = input("Qual ataque você quer escolher?\n(1: Jato de Água [Dano 50, Energia 40] | 2: Bolha [Dano 35, Energia 10] | 3: Descansar) -> ")
        
        if opc_ataque == "1":
            if energia["squirtle"] >= 40:
                energia["squirtle"] -= 40
                time.sleep(0.5)
                print("Você escolheu Jato de água!!")
                vida_boss -= 50
            else:
                print("Sem energia suficiente! Você perdeu o turno tentando atacar.")
                time.sleep(1)
                continue

        elif opc_ataque == "2":
            if energia["squirtle"] >= 10:
                energia["squirtle"] -= 10
                time.sleep(0.5)
                print("Você escolheu Bolha!!")
                vida_boss -= 35
            else:
                print("Sem energia suficiente! Você perdeu o turno tentando atacar.")
                time.sleep(1)
                continue

        elif opc_ataque == "3":
            time.sleep(0.5)
            energia["squirtle"] = min(100, energia["squirtle"] + 50)
            print(f"Squirtle descansou, agora sua energia é {energia['squirtle']}/100")
        else:
            print("Ataque inválido! Você perdeu a vez.")
            time.sleep(1)
            continue
            
        time.sleep(1)
        print(f"A vida do boss agora é {max(0, vida_boss)}/500!!")
        time.sleep(1)

    elif escolha == "3":
        if "3" not in pokemons:
            print("Bulbasaur foi derrotado, ele não pode mais batalhar!")
            time.sleep(2)
            continue    
            
        time.sleep(1)
        opc_ataque = input("Qual ataque você quer escolher?\n(1: Raio de Sol [Dano 50, Energia 40] | 2: Folha Cortante [Dano 35, Energia 10] | 3: Descansar) -> ")
        
        if opc_ataque == "1":
            if energia["bulbassauro"] >= 40:
                energia["bulbassauro"] -= 40
                time.sleep(0.5)   
                print("Você escolheu Raio de Sol!!")         
                vida_boss -= 50
            else:
                print("Sem energia suficiente! Você perdeu o turno tentando atacar.")
                time.sleep(1)
                continue

        elif opc_ataque == "2":
            if energia["bulbassauro"] >= 10:
                energia["bulbassauro"] -= 10
                time.sleep(0.5)
                print("Você escolheu Folha cortante!!")
                vida_boss -= 35
            else:
                print("Sem energia suficiente! Você perdeu o turno tentando atacar.")
                time.sleep(1)
                continue

        elif opc_ataque == "3":
            time.sleep(0.5)
            energia["bulbassauro"] = min(100, energia["bulbassauro"] + 50)
            print(f"Bulbasaur descansou, agora sua energia é {energia['bulbassauro']}/100")
        else:
            print("Ataque inválido! Você perdeu a vez.")
            time.sleep(1)
            continue
            
        time.sleep(1)
        print(f"A vida do boss agora é {max(0, vida_boss)}/500!!")
        time.sleep(1)

    else:
        print("Digite um pokémon válido!")
        time.sleep(2)
        continue

    if vida_boss <= 0:
        print("\n🏆 Parabéns!! Você venceu a batalha pokémon!")
        break

    print("\nAgora é o turno do boss!!")
    time.sleep(1)

    if escolha == "1":
        print("O boss ataca Charmander!")
        time.sleep(1)
        pokemons["1"] -= 20
        print(f"A vida de Charmander agora é {max(0, pokemons['1'])}/100")
        if pokemons["1"] <= 0:
            print(" Charmander foi derrotado e não pode mais participar!")
            del pokemons["1"]
        time.sleep(2)

    elif escolha == "2":
        print("O boss ataca Squirtle!")
        time.sleep(1)
        pokemons["2"] -= 20
        print(f"A vida de Squirtle agora é {max(0, pokemons['2'])}/100")
        if pokemons["2"] <= 0:
            print(" Squirtle foi derrotado e não pode mais participar!")
            del pokemons["2"]
        time.sleep(2)

    elif escolha == "3":
        print("O boss ataca Bulbasaur!")
        time.sleep(1)
        pokemons["3"] -= 20
        print(f"A vida de Bulbasaur agora é {max(0, pokemons['3'])}/100")
        if pokemons["3"] <= 0:
            print("Bulbasaur foi derrotado e não pode mais participar!")
            del pokemons["3"]
        time.sleep(2)

    if len(pokemons) == 0:
        print("\n Todos os seus pokémons foram derrotados. Você perdeu!")
        break

    print("Agora é seu turno")
    time.sleep(1)
