import random
import sys


class BlackJack:
    chervi = chr(9829)
    piki = chr(9824)
    bubna = chr(9830)
    kresti = chr(9827)

    rubaha = "rubaha"

    def main(self):
        print(
            """
          Сыграйте в Двадцать одно!

          Правила:
          Попробуйте набрать максимально близкое количество очков к 21, но не более.
          Наберете больше чем 21 - проиграете!
          Карты картинки приравниваются к 10 очкам(Валет, Дама, Король).
          Тузы приравниваются к 1 или 11 очкам.
          Все числовые карты (2, 3, 4,... 10) равны своему значению, не смотря на масть!
          Игра будет вас спрашивать ваших о действиях, в скобочках будет указано что нажимать.
          возможны 3 действия:
          (1) - получить еще карту.
          (2) - достаточно карт!
          (3) - чтобы увеличить ставку. но сделать это можно только один раз.
          Если будет ничья, т.е кол-во очков равное, то твоя ставка будет возвращена тебе 1 к 1!
          Диллер прекращает получать карты когда его очки равны или больше 17.
          В случае победы - твой выигрыш три к двум(пр: ставка 10, выигрышь 15!).

          Думаю правила ясны.
          Удачи, пупсик!
          Задонить автору можно по следующим реквизитам: 8600
      """
        )

        start_money = int(input("Стартовый капитал будет: "))
        while True:
            if start_money <= 1:
                print(
                    """
              Вы обанкрочены!
              Лох получаеца...
              Спасибо за игру! ББ!
              """
                )
                sys.exit()

            print("Ваш баланс:", start_money)
            bet = self.GetBet(start_money)

            kolodec_yobani = self.DeckGenering()
            dillera_ruka = [kolodec_yobani.pop(), kolodec_yobani.pop()]
            igroka_ruka = [kolodec_yobani.pop(), kolodec_yobani.pop()]

            print("Ставка:", bet)
            while True:
                self.CheckHands(igroka_ruka, dillera_ruka, False)
                print()

                if self.Num_kolvo(igroka_ruka) > 21:
                    break

                hod = self.Hodunok(igroka_ruka, start_money - bet)

                if hod == "3":
                    dop_stavka = self.GetBet(min(bet, (start_money - bet)))
                    bet += dop_stavka
                    print(f"Ставка была увеличена до {bet}.")
                    print("Ставка:", bet)

                if hod in ("1", "3"):
                    newCard = kolodec_yobani.pop()
                    level, mast = newCard
                    print(f"Вы получили новую карту {level}{mast}.")
                    igroka_ruka.append(newCard)

                    if self.Num_kolvo(igroka_ruka) > 21:
                        continue

                if hod in ("2", "3"):
                    break

            if self.Num_kolvo(dillera_ruka) <= 21:
                while self.Num_kolvo(dillera_ruka) < 17:
                    print("Диллер получает карту...")
                    dillera_ruka.append(kolodec_yobani.pop())
                    self.CheckHands(igroka_ruka, dillera_ruka, False)

                    if self.Num_kolvo(dillera_ruka) > 21:
                        break
                    input("Нажмите любую кнопку чтобы продолжить...")
                    print("\n\n")

            self.CheckHands(igroka_ruka, dillera_ruka, True)

            itogIgroka = self.Num_kolvo(igroka_ruka)
            itogDillera = self.Num_kolvo(dillera_ruka)

            if itogDillera > 21:
                print(f"Диллер в пролете! Вы выигрываете {bet*1.5}$!")
                start_money += bet * 1.5
            elif itogIgroka > 21 or itogIgroka < itogDillera:
                print("Вы проиграли!")
                start_money -= bet
            elif itogIgroka > itogDillera:
                print(f"Вы выиграли {bet*1.5}$!")
                start_money += bet * 1.5
            elif itogIgroka == itogDillera:
                print("Наблюдаю ничью, ставка была возвращена!")

            input("Нажмите любую кнопку чтобы продолжить...")
            print("\n\n")

    def DeckGenering(self):
        """Генерирует игральную колоду из 52 карт."""
        kolodec_yobani = []
        for mast in (self.chervi, self.piki, self.bubna, self.kresti):
            for level in ("В", "Д", "К", "Т"):
                kolodec_yobani.append((level, mast))
            for level in range(2, 10 + 1):
                kolodec_yobani.append((str(level), mast))
        random.shuffle(kolodec_yobani)
        return kolodec_yobani

    def GetBet(self, maxCost):
        """Функция для получения у игрока ставки."""
        while True:
            print(
                f"Ваша ставка? (1<=х<={maxCost}, или введите 'бб' для того чтоб покинуть игру.)"
            )
            bet = input("> ")

            if bet == "бб":
                print("Спасибо за игру! До встречи!")
                sys.exit()

            if not bet.isdecimal():
                continue

            bet = int(bet)
            if 1 <= bet <= maxCost:
                return bet

    def CheckHands(self, igroka_ruka, dillera_ruka, showDealerHand):
        """Вывод на экран карты игрока и диллера. Скрываем первую карту диллера,
        showDealerHand равно False"""
        print()
        if showDealerHand:
            print("Диллер:", self.Num_kolvo(dillera_ruka))
            self.CardOut(dillera_ruka)
        else:
            print("Диллер: Неизвестно")
            self.CardOut([self.rubaha] + dillera_ruka[1:])

        print("Игрок:", self.Num_kolvo(igroka_ruka))
        self.CardOut(igroka_ruka)

    def Num_kolvo(self, cards):
        """Возвращается общее количество очков в руке играющего."""
        kolvo = 0
        tuzi = 0

        for card in cards:
            level = card[0]
            if level == "Т":
                tuzi += 1
            elif level in ("В", "Д", "К"):
                kolvo += 10
            else:
                kolvo += int(level)

        kolvo += tuzi
        for i in range(tuzi):
            if kolvo + 10 <= 21:
                kolvo += 10

        return kolvo

    def CardOut(self, cards):
        """Вывод на экран всех карт"""
        karta = [
            "",
            "",
            "",
            "",
        ]

        for i, card in enumerate(cards):
            karta[0] += " ___ "
            if card == self.rubaha:
                karta[1] += r"|\#/| "
                karta[2] += r"|#X#| "
                karta[3] += r"|/#\| "
            else:
                level, mast = card
                karta[1] += f"|{level}  | "
                karta[2] += f"| {mast} | "
                karta[3] += f"|__{level}| "

        for stroka in karta:
            print(stroka)

    def Hodunok(self, ruka, money):
        """Идет запрос у игрока, какой ход он хочет сделать, далее возвращаем
        (1) если он хочет взять еще карту.
        (2) если ему хватит.
        (3) если он удваивает ставку.
        """
        while True:
            hodi = ["(1) - еще карту", "(2) - достаточно"]

            if len(ruka) == 2 and money > 0:
                hodi.append("(3) - удвоить ставку")

            hodosms = ", ".join(hodi) + "> "
            hod = input(hodosms).upper()
            if hod in ("1", "2"):
                return hod

            if hod == "3" and "(3) - удвоить ставку" in hodi:
                return hod
