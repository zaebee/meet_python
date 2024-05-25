import csv

import time

import os


PATH_PREFIX = os.path.dirname(os.path.abspath(__file__))

#def plus_klient():
 #   os.system('cls')
  #  d_u = input("Выберите опцию: d = добавить клинета, u = удалить клиента:")
   # d_u = d_u.lower().strip()
    #if d_u in  ["d"]:
     #   print ("Напишите имя клиента, с которым он будет внесён в базу данных")
      #  konec_csv(balansy)
def writer_csv(filename, fieldnames, data, mode='a+'):
    filename_path = os.path.join(PATH_PREFIX, filename)
    with open(filename_path, mode) as fp:
        writer = csv.DictWriter(fp, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
def update_user(name, name_2, amount):
    data = reader_csv('balancy.csv')
    for ww in data:
        if ww['1'] == name:
            ww['2'] = int(ww['2']) + int(amount if amount else 0)
        elif ww ['1'] == name_2:
            ww['2'] = int(ww['2']) - int(amount if amount else 0)    
    writer_csv('balancy.csv', ['1', '2'], data, 'w')

def konec_csv(file_name, new_row):
    with open(file_name, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(new_row)
    column1 = input("Введите имя")
    
def kara():
    print ("Кто выплачивает штраф?")
    #именна
    print ("names")
    kara = input("Ввод тут:")

    #программа по снятию денег со счёта

def cycl():
    print ("Нажмите x чтобы вернуться в главное меню")
    x = input("Ввод:")
    x = x.lower().strip()
    if x in ["x"]:
        start()
    else:
        start()

def timer(seconds):
    pass


def wlożenie():
    os.system('cls')
    print ("Введите имя клиента")
    reader = list(csv.DictReader(open('names.csv', 'r')))
    names = [row['name']for row in reader]
    for row in reader:
        print (f"{row['name']}")
    name = input("Ввод тут:")
    if not name in names:
        print ("Клиент не обнаружен!")
    
    

def tr():
    os.system('cls')
    try:
        print ("Выбери отправителя и получателя. Пишите в точности как показано!")
        reader = list(csv.DictReader(open('names.csv', 'r')))
        names = [row["name"] for row in reader]
        for row in reader:
            print (f"{row['name']}")
        sender = input("Введите отправителя:")
        if not sender in names:
            print("Клиент не обнаружен!")
            cycl()
        reciver = input("Введите получателя:")
        if not reciver in names:
            print("Клиент не обнаружен!")
            cycl()
        if sender == reciver:
            print ("Невозможная транзакция!")
            cycl()
        summa = int(input("Введите сумму:"))
        os.system('cls')
        print (f"""                ТРАНЗАКЦИЯ
                 MNS банк  
               Отправитель: {sender}
               Получатель: {reciver}
               Сумма: {summa}
               """)
        czek = input("Вы потверждаете перевод?:")
        czek = czek.lower().strip()
        if czek in ["да","потдверждаю"]:
            print ("Производиться транзакция...")
            time.sleep(4)
            os.system('cls')
            update_user(sender, reciver, summa)
            print (f"""       ТРАНЗАКЦИЯ
        MNS банк
    Транзакция проведена успешно!
    Отправитель: {sender}
    Получатель: {reciver}                               
    Сумма: {summa}
        """)
            cycl()
        elif czek in ["нет","не потверждаю"]:
            return tr()  
    except ValueError:
        print ("Вы неправильно указали сумму!")

def names(filename):
    reader = csv.DictReader(open(filename, 'r'))
    for row in reader:
        name = row.get('name')
        msg = f"{name}"
        print (msg)

def reader_csv(filename):
    os.system('cls')
    prefix = 'C:\\python_programs\\programma_sayt\\wallet\\'
    with open(prefix + filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if filename == 'stat.csv':
                for key, value in row.items():
                    print (f"{key}:{value}")
            else:
                name = row.get("1")
                balance = row.get("2")
                msg = f"{name}: {balance}"
                print (msg)

def start():
    os.system('cls')
    print ("Здравствуйте, это программа банка MNS")
    print ("Выберите функции")
    print ("1 = балансы клиентов")
    print ("2 = транзакции")
    print ("3 = история штрафов")
    print ("4 = статистика банка")
    print ("5 = задолженности")
    print ("6 = добавить информацию")
    enter = input("Место ввода здесь: ")
    enter = enter.lower().strip()
    if enter in ["1","балансы","балансы клиентов","баланс"]:
        reader_csv('balancy.csv')
        cycl()
    elif enter in ["2","транзакции"]:
        tranzation()
    elif enter in ["3","штрафы","история штрафов"]:
        reader_csv('sztrafy.csv')
        cycl()
    elif enter in ["4","статистика","статистика банка"]:
        reader_csv('stat.csv')
        cycl()
    elif enter in ["5","задолженности","долги"]:
        reader_csv('zadolżenosci.csv')
        cycl()
    elif enter in ["6","информация","добавить информацию"]:
        pass
    else:
        print ("Вы неправильно ввели номер программы!")
        cycl()

def tranzation():
    os.system('cls')
    print ("Выберите вариант транзакции")
    print ("1 = снятие/вложение денег на счёт")
    print ("2 = межособовая транзакция")
    print ("3 = штраф")
    choose = input("Ввод тут:")
    choose = choose.lower().strip()
    if choose in ["1", "снятие/вложение","снятие/вложение денег","снятие/вложение денег на счёт"]:
        wlożenie()
    elif choose in ["2","транзакция","межособовая транзакция","межособовая"]:
        tr()
    elif choose in ["3","штраф"]:
        kara()
    elif choose in ["x"]:
        return start()
    else:
        print ("Вы неправильно ввели номер программы!")
        cycl()

start()