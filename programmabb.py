import random

tut_wopros = "J"


def naczalo():
    print("Привет,приветствую в игре про математику. Что ты хочешь из этого?")
    print("1 = калькулятор")
    print("2 = вычислить факториал числа")
    print("3 = сыграть в игру")
    print("4 = пасхалки")
    

naczalo()

o = input("Введите номер программы:")

def multiply_numbers_until(z):
    result_6 = 1
    for j in range(1, z + 1):
        result_6 *= j
    return result_6

if o in ["2", "Вычислить факториал числа", "вычислить факториал числа"]:
    print("Напиши число, у которого хочешь узнать факториал")

    try:
        number = int(input("Введите число:"))
        result_6 = multiply_numbers_until(number)
        print("Факториал числа", number, "равен", result_6)
    except ValueError:
        print("Вводи только числа!")


def plus():
    print("Заполните места ввода")
    try:
        l = int(input())
        print("прибавить")
        n = int(input())
        result = l + n
        print("Сумма чисел", l, "и", n, "равна", result)
        hh = input("Что нибудь ещё? 1 = вернуться в меню, 2 = продолжить:")
        if hh in ["1"]:
            naczalo()
            o = input("Введи номер требуемой программы:        ")
            if o in ["1"]:
                kalkulator()
            elif o in ["2"]:
                tut_wopros
            elif o in ["3"]:
                print("Давай поиграем!")
                print("Выбери сложность")
                print("1 уровень")
                print("2 уровень")
                print("3 уровень")
                nn = input("Выбери сложность:")
                if nn == ("1"):
                    lev_1()
                elif nn == ("2"):
                    lev_2()
                elif nn == ("3"):
                    lev_3()
                else:
                    print("Вы некорректно ввели номер программы")
            elif o in ["4"]:
                pashalki()
            else:
                print("Вы неправильно ввели номер программы")
        elif hh in ["2"]:
            kalkulator()
        else:
            print("Вы неправильно указали номер программы")
    except ValueError:
        print("Вводи только цифры!")


def minus():
    print("Заполните места ввода")
    try:
        g = int(input())
        print("отнять")
        y = int(input())
        result_2 = g - y
        print("Разница чисел", g, "и", y, "равна", result_2)
        hh = input("Что нибудь ещё? 1 = вернуться в меню, 2 = продолжить:")
        if hh in ["1"]:
            naczalo()
            o = input("Введи номер требуемой программы:        ")
            if o in ["1"]:
                kalkulator()
            elif o in ["2"]:
                tut_wopros
            elif o in ["3"]:
                print("Давай поиграем!")
                print("Выбери сложность")
                print("1 уровень")
                print("2 уровень")
                print("3 уровень")
                nn = input("Выбери сложность:")
                if nn == ("1"):
                    lev_1()
                elif nn == ("2"):
                    lev_2()
                elif nn == ("3"):
                    lev_3()
                else:
                    print("Вы некорректно ввели номер программы")
            elif o in ["4"]:
                pashalki()
            else:
                print("Вы неправильно ввели номер программы")
        elif hh in ["2"]:
            kalkulator()
        else:
            print("Вы неправильно указали номер программы")
    except ValueError:
        print("Вводи только цифры!")


def umnozenie():
    print("Заполните места ввода")
    try:
        f = int(input())
        print("умножить на")
        m = int(input())
        result_3 = f * m
        print("Произвидение чисел", f, "и", m, "равно", result_3)
        hh = input("Что нибудь ещё? 1 = вернуться в меню, 2 = продолжить:")
        if hh in ["1"]:
            naczalo()
            o = input("Введи номер требуемой программы:        ")
            if o in ["1"]:
                kalkulator()
            elif o in ["2"]:
                tut_wopros
            elif o in ["3"]:
                print("Давай поиграем!")
                print("Выбери сложность")
                print("1 уровень")
                print("2 уровень")
                print("3 уровень")
                nn = input("Выбери сложность:")
                if nn == ("1"):
                    lev_1()
                elif nn == ("2"):
                    lev_2()
                elif nn == ("3"):
                    lev_3()
                else:
                    print("Вы некорректно ввели номер программы")
            elif o in ["4"]:
                pashalki()
            else:
                print("Вы неправильно ввели номер программы")
        elif hh in ["2"]:
            kalkulator()
        else:
            print("Вы неправильно указали номер программы")
    except ValueError:
        print("Вводи только цифры!")


def delenie():
    print("Заполните места ввода")
    try:
        s = int(input())
        print("разделить на")
        v = int(input())
        result_4 = s / v
        print("Деление чисел", s, "и", v, "равно", result_4)
        hh = input("Что нибудь ещё? 1 = вернуться в меню, 2 = продолжить:")
        if hh in ["1"]:
            naczalo()
            o = input("Введи номер требуемой программы:        ")
            if o in ["1"]:
                kalkulator()
            elif o in ["2"]:
                tut_wopros
            elif o in ["3"]:
                print("Давай поиграем!")
                print("Выбери сложность")
                print("1 уровень")
                print("2 уровень")
                print("3 уровень")
                nn = input("Выбери сложность:")
                if nn == ("1"):
                    lev_1()
                elif nn == ("2"):
                    lev_2()
                elif nn == ("3"):
                    lev_3()
                else:
                    print("Вы некорректно ввели номер программы")
            elif o in ["4"]:
                pashalki()
            else:
                print("Вы неправильно ввели номер программы")
        elif hh in ["2"]:
            kalkulator()
        else:
            print("Вы неправильно указали номер программы")
    except ValueError:
        print("Вводи только числа!")


def stepen():
    print("Заполните места ввода")
    try:
        d = int(input("Напиши число,которое хочешь возвести в степень:"))
        result_5 = d * d
        print("Степень числа", d, "равно", result_5)
        hh = input("Что нибудь ещё? 1 = вернуться в меню, 2 = продолжить:")
        if hh in ["1"]:
            naczalo()
            o = input("Введи номер требуемой программы:        ")
            if o in ["1"]:
                kalkulator()
            elif o in ["2"]:
                tut_wopros
            elif o in ["3"]:
                print("Давай поиграем!")
                print("Выбери сложность")
                print("1 уровень")
                print("2 уровень")
                print("3 уровень")
                nn = input("Выбери сложность:")
                if nn == ("1"):
                    lev_1()
                elif nn == ("2"):
                    lev_2()
                elif nn == ("3"):
                    lev_3()
                else:
                    print("Вы некорректно ввели номер программы")
            elif o in ["4"]:
                pashalki()
            else:
                print("Вы неправильно ввели номер программы")
        elif hh in ["2"]:
            kalkulator()
        else:
            print("Вы неправильно указали номер программы")
    except ValueError:
        print("Вводи только числа!")


def kalkulator():
    print("1 = сложение")
    print("2 = вычитание")
    print("3 = умножение")
    print("4 = деление")
    print("5 = степень числа")
    p = input("Что вам из этого надо?:")
    p = p.lower()
    if p in ["1", "сложение"]:
        plus()
    elif p in ["2", "вычитание"]:
        minus()
    elif p in ["3", "умножение"]:
        umnozenie()
    elif p in ["4", "деление"]:
        delenie()
    elif p in ["5", "степень числа"]:
        stepen()
    else:
        print("Вы неправильно указали номер программы")


def konec():
    print(
        "Молодец! Пасхалка активирована! Найдено 7/7. Поздравляю! Вы нашли все пасхалки! Теперь ты можешь выбрать, какую программу написать дальше в этом приложении!"
    )
    print("1 = Камень, ножницы, бумага")
    print("2 = Казино")
    print("3 = Игра в города")
    print("4 = Предсказатель")
    yy = input("Что из этого ты хочешь?: ")
    if yy in ["1", "2", "3", "4"]:
        print("Отличный выбор! Спасибо, что прошли все пасхалки!")
    else:
        print("Не пиши ерунды, выбери программу")


def pashalki():
    print("Введите пасхалку")
    print("Чтобы получить больше информации, напиши 'help'")
    t = input("Пасхалка:")
    if t in ["18 апреля", "18.04", "18.04.10", "18 Апреля", "Апреля 18"]:
        print(
            "Молодец! Пасхалка активирована! Найдено 1/7. Следующая пасхалка связанна с популярным аниме."
        )
    elif t in ["Саске", "саске"]:
        print(
            "Молодец! Пасхалка активирована! Найдено 2/7. Следующая пасхалка связанна со спортом."
        )
    elif t in ["Гандболл", "гандболл", "гандбол", "Гандбол"]:
        print(
            "Молодец! Пасхалка активирована! Найдено 3/7.Следующая пасхалка связанна с популярной компьютерной игрой."
        )
    elif t in ["Minecraft", "minecraft", "Маинкрафт", "маинкрафт"]:
        print(
            "Молодец! Пасхалка активирована! Найдено 4/7.Следующая пасхалка это год в котором я взял свой первый кубок по карате."
        )
    elif t in ["8", "Восемь", "восемь"]:
        print(
            "Молодец! Пасхалка активирована! Найдено 5/7.Следующая пасхалка связанна с очень известной фразой. Я бы назвал эту фразу 'фраза бытия'. Обрати внимание на слово 'бытия'. Фраза взята из классической литературы."
        )
    elif t in [
        "Быть или не быть",
        "Быть или не быть. Вот в чём вопрос",
        "быть или не быть",
        "Быть или не быть вот в чём вопрос",
    ]:
        print(
            "Молодец! Пасхалка активирована! Найдено 6/7.Следующая пасхалка это вратарь, который совершил больше всего сейвов в лиге чемпионов."
        )
    elif t in ["Икер Касильяс", "икер касильяс", "Касильяс", "касильяс"]:
        konec()
    elif t in ["help", "Help", "HELP"]:
        print(
            "Пасхалки это просто отсылки на какие-то очень популярные вещи,события или фразы. Так же тут могут присутствовать кое какие даты со мной. Это подсказка на первую пасхалку. Обращайте внимание на правильность написания! Удачи!"
        )
    else:
        print(
            "Пасхалка не найдена :(. Проверь написание или попробуй что-нибудь другое"
        )


def menu():
    hh = input("Что нибудь ещё? 1 = вернуться в меню, 2 = продолжить:")
    if hh in ["1"]:
        naczalo()
        o = input("Введи номер требуемой программы:        ")
        if o in ["1"]:
            kalkulator()
        elif o in ["2"]:
            tut_wopros
        elif o in ["3"]:
            print("Давай поиграем!")
            print("Выбери сложность")
            print("1 уровень")
            print("2 уровень")
            print("3 уровень")
            nn = input("Выбери сложность:")
            if nn == ("1"):
                lev_1()
            elif nn == ("2"):
                lev_2()
            elif nn == ("3"):
                lev_3()
            else:
                print("Вы некорректно ввели номер программы")
        elif o in ["4"]:
            pashalki()
        else:
            print("Вы неправильно ввели номер программы")
    elif hh in ["2"]:
        print("Выбери уровень")
        print("1 уровень")
        print("2 уровень")
        print("3 уровень")
        nn = input("Выбери сложность:")
        if nn == ("1"):
            lev_1()
        elif nn == ("2"):
            lev_2()
        elif nn == ("3"):
            lev_3()
        else:
            print("Вы некорректно ввели номер программы")
    else:
        print("Вы неправильно указали номер программы")


def lev_1():
    level_1 = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
    ]
    l_1 = random.choice(level_1)
    if l_1 in ["1"]:
        print("2+4")
        AA = int(input("Ответ:"))
        if AA == 6:
            print("Молодец!")
            menu()
        elif AA != 6:
            print("Неправильно,ты проиграл")
            menu()
    elif l_1 in ["2"]:
        print("8+1")
        AA = int(input("Ответ:"))
        if AA == 9:
            print("Молодец!")
            menu()
        elif AA != 9:
            print("Неправильно,ты проиграл")
            menu()
    elif l_1 in ["3"]:
        print("4+10")
        AA = int(input("Ответ:"))
        if AA == 14:
            print("Молодец!")
            menu()
        elif AA != 14:
            print("Неправильно,ты проиграл")
            menu()
    elif l_1 in ["4"]:
        print("2+9")
        AA = int(input("Ответ:"))
        if AA == 11:
            print("Молодец!")
            menu()
        elif AA != 11:
            print("Неправильно,ты проиграл")
            menu()
    elif l_1 in ["5"]:
        print("5+8")
        AA = int(input("Ответ:"))
        if AA == 13:
            print("Молодец!")
            menu()
        elif AA != 13:
            print("Неправильно,ты проиграл")
            menu()
    elif l_1 in ["6"]:
        print("10-6")
        AA = int(input("Ответ:"))
        if AA == 4:
            print("Молодец!")
            menu()
        elif AA != 4:
            print("Неправильно,ты проиграл")
            menu()
    elif l_1 in ["7"]:
        print("3-1")
        AA = int(input("Ответ:"))
        if AA == 2:
            print("Молодец!")
            menu()
        elif AA != 2:
            print("Неправильно,ты проиграл")
            menu()
    elif l_1 in ["8"]:
        print("12-4")
        AA = int(input("Ответ:"))
        if AA == 8:
            print("Молодец!")
            menu()
        elif AA != 8:
            print("Неправильно,ты проиграл")
            menu()
    elif l_1 in ["9"]:
        print("9-5")
        AA = int(input("Ответ:"))
        if AA == 4:
            print("Молодец!")
            menu()
        elif AA != 4:
            print("Неправильно,ты проиграл")
            menu()
    elif l_1 in ["10"]:
        print("7-6")
        AA = int(input("Ответ:"))
        if AA == 1:
            print("Молодец!")
            menu()
        elif AA != 1:
            print("Неправильно,ты проиграл")
            menu()


def lev_2():
    level_2 = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
    ]
    l_2 = random.choice(level_2)
    if l_2 in ["1"]:
        print("14+15")
        AA = int(input("Ответ:"))
        if AA == 29:
            print("Молодец!")
        elif AA != 29:
            print("Неправильно, ты проиграл")
            menu()
    elif l_2 in ["2"]:
        print("16+20")
        AA = int(input("Ответ:"))
        if AA == 36:
            print("Молодец!")
        elif AA != 36:
            print("Неправильно,ты проиграл")
    elif l_2 in ["3"]:
        print("17+21")
        AA = int(input("Ответ:"))
        if AA == 38:
            print("Молодец!")
        elif AA != 38:
            print("Неправильно,ты проиграл")
    elif l_2 in ["4"]:
        print("14+30")
        AA = int(input("Ответ:"))
        if AA == 44:
            print("Молодец!")
        elif AA != 44:
            print("Неправильно,ты проиграл")
    elif l_2 in ["5"]:
        print("11+90")
        AA = int(input("Ответ:"))
        if AA == 101:
            print("Молодец!")
        elif AA != 101:
            print("Неправильно,ты проиграл")
    elif l_2 in ["6"]:
        print("31-17")
        AA = int(input("Ответ:"))
        if AA == 14:
            print("Молодец!")
        elif AA != 14:
            print("Неправильно,ты проиграл")
    elif l_2 in ["7"]:
        print("28-14")
        AA = int(input("Ответ:"))
        if AA == 14:
            print("Молодец!")
        elif AA != 14:
            print("Неправильно,ты проиграл")
    elif l_2 in ["8"]:
        print("37-11")
        AA = int(input("Ответ:"))
        if AA == 26:
            print("Молодец!")
        elif AA != 26:
            print("Неправильно,ты проиграл")
    elif l_2 in ["9"]:
        print("70-35")
        AA = int(input("Ответ:"))
        if AA == 35:
            print("Молодец!")
        elif AA != 35:
            print("Неправильно,ты проиграл")
    elif l_2 in ["10"]:
        print("66-22")
        AA = int(input("Ответ:"))
        if AA == 44:
            print("Молодец!")
        elif AA != 44:
            print("Неправильно,ты проиграл")
    elif l_2 in ["11"]:
        print("6*11")
        AA = int(input("Ответ:"))
        if AA == 66:
            print("Молодец!")
        elif AA != 66:
            print("Неправильно,ты проиграл")
    elif l_2 in ["12"]:
        print("14*10")
        AA = int(input("Ответ:"))
        if AA == 140:
            print("Молодец!")
        elif AA != 140:
            print("Неправильно,ты проиграл")
    elif l_2 in ["13"]:
        print("5*9")
        AA = int(input("Ответ:"))
        if AA == 45:
            print("Молодец!")
        elif AA != 45:
            print("Неправильно,ты проиграл")
    elif l_2 in ["14"]:
        print("9*12")
        AA = int(input("Ответ:"))
        if AA == 108:
            print("Молодец!")
        elif AA != 108:
            print("Неправильно,ты проиграл")
    elif l_2 in ["15"]:
        print("7*6")
        AA = int(input("Ответ:"))
        if AA == 42:
            print("Молодец!")
        elif AA != 42:
            print("Неправильно,ты проиграл")


def lev_3():
    level_3 = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
    ]
    l_3 = random.choice(level_3)
    if l_3 in ("1"):
        print("124+67")
        AA = int(input("Ответ:"))
        if AA == 191:
            print("Молодец!")
        if AA != 191:
            print("Неправильно,ты проиграл")
    elif l_3 in ["2"]:
        print("47+365")
        AA = int(input("Ответ:"))
        if AA == 412:
            print("Молодец!")
        elif AA != 412:
            print("Неправильно,ты проиграл")
    elif l_3 in ["3"]:
        print("712+402")
        AA = int(input("Ответ:"))
        if AA == 1114:
            print("Молодец!")
        elif AA != 1114:
            print("Неправильно,ты проиграл")
    elif l_3 in ["4"]:
        print("209+957")
        AA = int(input("Ответ:"))
        if AA == 1166:
            print("Молодец!")
        elif AA != 1166:
            print("Неправильно,ты проиграл")
    elif l_3 in ["5"]:
        print("111+763")
        AA = int(input("Ответ:"))
        if AA == 874:
            print("Молодец!")
        elif AA != 874:
            print("Неправильно,ты проиграл")
    elif l_3 in ["6"]:
        print("387-290")
        AA = int(input("Ответ:"))
        if AA == 97:
            print("Молодец!")
        elif AA != 97:
            print("Неправильно,ты проиграл")
    elif l_3 in ["7"]:
        print("675-142")
        AA = int(input("Ответ:"))
        if AA == 533:
            print("Молодец!")
        elif AA != 533:
            print("Неправильно,ты проиграл")
    elif l_3 in ["8"]:
        print("524-197")
        AA = int(input("Ответ:"))
        if AA == 327:
            print("Молодец!")
        elif AA != 327:
            print("Неправильно,ты проиграл")
    elif l_3 in ["9"]:
        print("887-164")
        AA = int(input("Ответ:"))
        if AA == 723:
            print("Молодец!")
        elif AA != 723:
            print("Неправильно,ты проиграл")
    elif l_3 in ["10"]:
        print("475-222")
        AA = int(input("Ответ:"))
        if AA == 253:
            print("Молодец!")
        elif AA != 253:
            print("Неправильно,ты проиграл")
    elif l_3 in ["11"]:
        print("14*15")
        AA = int(input("Ответ:"))
        if AA == 210:
            print("Молодец!")
        elif AA != 210:
            print("Неправильно,ты проиграл")
    elif l_3 in ["12"]:
        print("17*13")
        AA = int(input("Ответ:"))
        if AA == 221:
            print("Молодец!")
        elif AA != 221:
            print("Неправильно,ты проиграл")
    elif l_3 in ["13"]:
        print("9*16")
        AA = int(input("Ответ:"))
        if AA == 144:
            print("Молодец!")
        elif AA != 144:
            print("Неправильно,ты проиграл")
    elif l_3 in ["14"]:
        print("30*31")
        AA = int(input("Ответ:"))
        if AA == 930:
            print("Молодец!")
        elif AA != 930:
            print("Неправильно,ты проиграл")
    elif l_3 in ["15"]:
        print("20*25")
        AA = int(input("Ответ:"))
        if AA == 500:
            print("Молодец!")
        elif AA != 500:
            print("Неправильно,ты проиграл")
    elif l_3 in ["16"]:
        print("Степень 21")
        AA = int(input("Ответ:"))
        if AA == 441:
            print("Молодец!")
        elif AA != 441:
            print("Неправильно,ты проиграл")
    elif l_3 in ["17"]:
        print("Степень 14")
        AA = int(input("Ответ:"))
        if AA == 196:
            print("Молодец!")
        elif AA != 196:
            print("Неправильно,ты проиграл")
    elif l_3 in ["18"]:
        print("Степень 55")
        AA = int(input("Ответ:"))
        if AA == 3025:
            print("Молодец!")
        elif AA != 3025:
            print("Неправильно,ты проиграл")
    elif l_3 in ["19"]:
        print("Степень 16")
        AA = int(input("Ответ:"))
        if AA == 256:
            print("Молодец!")
        elif AA != 256:
            print("Неправильно,ты проиграл")
    elif l_3 in ["20"]:
        print("Степень 13")
        AA = int(input("Ответ:"))
        if AA == 169:
            print("Молодец!")
        elif AA != 169:
            print("Неправильно,ты проиграл")

def game():
    if o in ["3", "Сыграть в игру", "сыграть в игру", "Игра", "игра"]:
        print("Давай поиграем!")
        print("Выбери сложность")
        print("1 уровень")
        print("2 уровень")
        print("3 уровень")
        nn = input("Выбери сложность:")
        if nn == ("1"):
            lev_1()
        elif nn == ("2"):
            lev_2()
        elif nn == ("3"):
            lev_3()
        else:
            print("Вы некорректно ввели номер программы")
    elif o in ["1", "Калькулятор", "калькулятор"]:
        kalkulator()
    elif o in ["4", "Пасхалки", "пасхалки"]:
        pashalki()
    else:
        print("Вы некорректно ввели число программы")


game()