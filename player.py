from vrag import*
from time import sleep
player = {
"hpplayer": 100,
"uronplayer": 15,
"zachitaplayer": 5,
"coin": 100,
"clever": 10
}
name = input("Здорува,5,чил кок тебе звоть(если ты думаешь что это локализация неправильная то нет, просто автор не знает русский язык)ладно шучу веди своё имя: ")
Uznakiname = print("Привет",name, "!")
while True:
    revum = int(input("А теперь выбери куда ты хочешь пойти: 1 = В БОЙ!,  2 = В магазин, 3 = Тренировка(прокачать урон), 4 = узнать информацию о Врагах. 5 = узнать информацию о игроке: "))
    if revum == 1:
        choicevrag = int(input("Выберите врага: 1 = Скала Джонсон, 2 = БУ!,ИСПУГАЛСЯ?, 3 = Тимоха"))
        if choicevrag == 1:
                while True:
                    print(vrag1["text"])
                    vrag1["hp"] > 0
                    print(f"Вы hp: {player['hpplayer']} damage: {player['uronplayer']}")
                    print(f"Враг hp {vrag1['hp']} damage {vrag1['uron']}")
                    vrag1["hp"] -= player["uronplayer"]
                    print("Вы ударили противника, у него осталось",vrag1["hp"],"hp")
                    player["hpplayer"] -= vrag1["uron"]
                    print("Противник ударил вас, у вас осталось",player["hpplayer"],"hp")
                    if player["hpplayer"] < 0:
                        print("Вы проиграли")
                        print(vrag1["lose"])
                    if vrag1["hp"] < 0:
                        print("Вы победили")
                        print("win")

    if revum == 2:
        shop = int(input(f'У тебя {player["coin"]} монет вот товары: 1 = зелье увелечения здоровья 50 монет, 2 = деревянный щит 80 монет, 3 = Меч алмазный 100 коинов: '))
        if shop == 1:   
            pay = input("Хочешь потвердить покупку зелья?: ")
            if pay == "Да" or "да":
                result = player["coin"] - 50
                hpplayer = player["hpplayer"] + 25
                print("У тебя осталось",result, "монет и",hpplayer, "хп")      
        if shop == 2:
            ay = input("Хочешь потвердить покупку Щита?: ")
            if pay == "Да" or "да":
                result2= player["coin"] - 80
                zachitaplayer = player["zachitaplayer"] + 10
                print("У тебя осталось",result2, "монет и",zachitaplayer, "защиты")    
        if shop == 3:
            pay = input("Хочешь потвердить покупку меча?: ")
            if pay == "Да" or "да":
                result3= player["coin"] - 100
                uronplayer = player["uronplayer"] + 20 
                print("У тебя осталось",result3, "монет и",uronplayer, "Урона")
    revum
    if revum == 3:
        tren = input("Вы желаете пройти тренировку?: ")
        if tren == "Да" or "да":
            print("Вы проходите тренировку")
            sleep(4)
            result12 = player["uronplayer"] + 20
            completetren = print("Вы увеличили свои навыки до",result12)  
            revum

 
    if revum == 4:
        infovrag = int(input("О каком враге вы хотите узнать? 1 = Скала Джонсон, 2 = БУ ИСПУГАЛСЯ, 3 = Тимоха"))
        if infovrag == 1:
            skala = print("Хп 150, урон 20, защита 0")
        if infovrag == 2:
            skala = print("Хп 200, урон 30, защита 10")
        if infovrag == 3:
            skala = print("Хп 350, урон 50, защита 25")
    revum

    if revum == 5:
      print(f'хп{player["hpplayer"]}, урон{player["uronplayer"]}, защита{player["zachitaplayer"]}, монеты{player["coin"]}')
    revum
    sleep(180)
    print("Поздравляю вы удачливый! Вот вам 15 монет")
    player["coin"] += 100
    revum
