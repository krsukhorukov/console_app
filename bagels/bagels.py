import random

helper = bool

class Bagels:
    def __init__(self, num_dig = 3, max_popitok = 10):
        self.num_dig = num_dig
        self.max_popitok = max_popitok

    def HIDE_NUMBER_PLUS(self, num_dig):
        all_digits = list(range(10))
        random.shuffle(all_digits)
        hidden_number = ''
        for i in range(num_dig):
            hidden_number += str(all_digits[i])
        return hidden_number


    def Game_Processing(self, PLAYERS_ANS, hidden_number):
        global helper
        if PLAYERS_ANS == hidden_number:
            helper = True
            return "Вы выиграли, угадав мое слово! Паразительно!"
        podskazki = []
        for i in range(len(PLAYERS_ANS)):
            if PLAYERS_ANS[i] == hidden_number[i]:
                podskazki.append("Ферми ")
            elif PLAYERS_ANS[i] in hidden_number:
                podskazki.append("Пико ")
        if len(podskazki) == 0:
            return "Бейглз "
        return " ".join(podskazki)


    def IS_DIGIT(self, num):
        if num == "":
            return False
        for i in num:
            if i not in "0 1 2 3 4 5 6 7 8 9 ".split():
                return False
            return True


    def one_more_time(self):
        print("Не желаете ли повторить? (1 или 2)")
        return input("1 - да.\n2 - нет.").startswith('1')


    def run(self):

        print("""                   Project Bagels
            Сыграйте в Бейглс!
            Бейглс - дедуктивная логическая игра.
            Данная игра была разработана величайшим программистом.

            Условия таковы:
            Я загадываю трехзначное число, ваша же задача - отгадать мое число. У вас 10 попыток.
            Когда я говорю:      Это значит:

            Пико                  Вы угадали правильную цифру на неправильной позиции!
            Ферми                 В вашем ответе есть правильная цифра на правильном месте!
            Бейглз                Если в вашей догадке не содержится правильных цифр!
            Я уже загадал число. Отгадайте его. Удачи!

            Данные для входа: ТОЛЬКО ТРЕХЗНАЧНЫЕ ЧИСЛА. Число может начинаться на 0. Например: 054, 012, 063 и тд.
            НЕ вводить буквы и символы. Например: /bh, .da, /12, ,67, , @#* и тд. При не соблюдении правил,
            к вам выедет пояснительная бригада, дабы обьяснить, что правила разработчиков лучше не нарушать.
            Надеюсь правила ясны:)
            Да будет веселье!
            """)
        
        while True:

            hidden_number = self.HIDE_NUMBER_PLUS(self.num_dig)
            print("Тайное число загадано.У вас есть 10 попыток.Удачи в разгадке!")

            nomer_popitki = 1
            while nomer_popitki <= self.max_popitok:
                PLAYERS_ANS = ""
                while len(PLAYERS_ANS) != self.num_dig or not self.IS_DIGIT(PLAYERS_ANS):
                    print(f"Попытка №{nomer_popitki}.Введите число.")
                    PLAYERS_ANS = input(": ")
                    podskazki = self.Game_Processing(PLAYERS_ANS, hidden_number)
                    print(podskazki)
                    if helper == True:
                        break
                    nomer_popitki += 1
            if PLAYERS_ANS == hidden_number:
                break
            if nomer_popitki > self.max_popitok:
                print("Вы проиграли. По причине превышения дозволенного количества использованных попыток.")
                print(f"Число, которое я загадал - {hidden_number}")
            if not self.one_more_time():
                print("""
                    Спасибо большое за игру!
                    Был рад ассестировать вам, в попытке угадать загаданное число!
                    Жду вас снова, до скорых встреч!
                                        ТИТРЫ:
                                        ....
                                        ....
                                        ....
                                        ....
                                        ....
                                        ....
                                Продолжение следует...
                    """)
                break
#   ДА НАЧНУТСЯ ТЕСТИРОВАНИЯ И ОБНОВЛЕНИЯ ИГРЫ!
# import random
# def HIDE_NUMBER_PLUS(NUM_DIG):
#     all_digits = list(range(10))
#     random.shuffle(all_digits)
#     hidden_number = ''

#     for i in range(NUM_DIG):

#         hidden_number += str(all_digits[i])

#     return hidden_number


# def Game_Processing(PLAYERS_ANS, hidden_number):
#     if PLAYERS_ANS == hidden_number:
        
#         return "You have won!"
#     podskazki = []

#     for i in range(len(PLAYERS_ANS)):
#         if PLAYERS_ANS[i] == hidden_number[i]:
            
#             podskazki.append("Fermi ")
            
#         elif PLAYERS_ANS[i] in hidden_number:
#             podskazki.append("Pico ")

#     if len(PLAYERS_ANS) == 0:
#         return "Bagels!"

#     return podskazki


# def IS_DIGIT(num):

#     if num == "":
#         return False

#     for i in num:
#         if i not in "0 1 2 3 4 5 6 7 8 9 ".split():
#             return False

#         return True
    
# def one_more_time():

#     print("Не желаете ли повторить? (1 или 0)")

#     return input("1 - да.\n2 - нет.").startswith('1')

# NUM_DIG = 3
# max_popitok = 10


# print("""
#       Сыграйте в Бейглс!
#       Бейглс - дедуктивная логическая игра.
#       Данная игра была разработана величайшим программистом.

#       Условия таковы: 
#       Я загадываю трехзначное число, ваша же задача - отгадать мое число. У вас 10 попыток.
#       Когда я говорю:      Это значит:

#       Pico                  Вы угадали правильную цифру на неправильной позиции!
#       Fermi                 В вашем ответе есть правильная цифра на правильном месте!
#       Bagels                Если в вашей догадке не содержится правильных цифр!
#       Я уже загадал число. Отгадайте его. Удачи!      
#       """)

# while True:
#     hidden_number = HIDE_NUMBER_PLUS(NUM_DIG)
#     print("Тайное число загадано. У вас есть 10 попыток. Удачи в разгадке!")

#     nomer_popitki = 1
#     while nomer_popitki <= max_popitok:
#         PLAYERS_ANS = ""
#         while len(PLAYERS_ANS) !=  NUM_DIG or not IS_DIGIT(PLAYERS_ANS):

#             print(f"Попытка №{nomer_popitki}. Введите число. ")
#             PLAYERS_ANS = input(": ")

#             podskazki = Game_Processing(PLAYERS_ANS, hidden_number)
#             print(podskazki)

#             nomer_popitki += 1


#     if PLAYERS_ANS == hidden_number:
#         break
#     if nomer_popitki > max_popitok:
#         print("Вы проиграли. По причине превышения дозволенного количества использованных попыток.")
#         print(f"Число, которое я загадал - {hidden_number}")

#     if not one_more_time():
#         print(""" 
#               Спасибо большое за игру!
#               Был рад ассестировать вам, в попытке угадать загаданное число!
#               Жду вас снова, до скорых встреч!
#                                 ТИТРЫ:
#                                 ....
#                                 ....
#                                 ....
#                                 ....
#                                 ....
#                                 ....
#                         Продолжение следует...
#               """)
#         break

