import sys, random, time

class FunnyLogo():
  try:
      import bext
  except ImportError:
      print("This program requires the bext module, which you")
      print("can install by following the instructions at")
      print("https://pypi.org/project/Bext/")
      sys.exit()

  # Задаем константы:
  WIDTH, HEIGHT = bext.size()
  # В Windows нельзя вывести символ в последний столбец без добавления
  # автоматически символа новой строки, так что уменьшаем ширину на 1:
  WIDTH -= 1

  NUMBER_OF_LOGOS = 5  # (!) Попробуйте заменить на 1 или 100.
  PAUSE_AMOUNT = 0.2  # (!) Попробуйте заменить на 1.0 или 0.0.
  # (!) Попробуйте уменьшить количество цветов в этом списке:
  COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

  UP_RIGHT = "ur"
  UP_LEFT = "ul"
  DOWN_RIGHT = "dr"
  DOWN_LEFT = "dl"
  DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

  # Названия ключей для ассоциативных массивов логотипов:
  COLOR = "color"
  X = "x"
  Y = "y"
  DIR = "direction"


  def main(self):
      self.bext.clear()

      logos = []
      for i in range(self.NUMBER_OF_LOGOS):
          logos.append(
              {
                  self.COLOR: random.choice(self.COLORS),
                  self.X: random.randint(1, self.WIDTH - 4),
                  self.Y: random.randint(1, self.HEIGHT - 4),
                  self.DIR: random.choice(self.DIRECTIONS),
              }
          )
          if logos[-1][self.X] % 2 == 1:
              logos[-1][self.X] -= 1

      cornerBounces = 0  # Считаем, сколько раз логотип столкнулся с углом.
      while True:  # Основной цикл программы.
          for logo in logos:  # Обрабатываем все логотипы в списке логотипов.
              # Очищаем место, где ранее находился логотип:
              self.bext.goto(logo[self.X], logo[self.Y])
              #print(" ", end="")  # (!) Попробуйте закомментировать строку.

              originalDirection = logo[self.DIR]

              # Проверяем, не отскакивает ли логотип от угла:
              if logo[self.X] == 0 and logo[self.Y] == 0:
                  logo[self.DIR] = self.DOWN_RIGHT
                  cornerBounces += 1
              elif logo[self.X] == 0 and logo[self.Y] == self.HEIGHT - 1:
                  logo[self.DIR] = self.UP_RIGHT
                  cornerBounces += 1
              elif logo[self.X] == self.WIDTH - 3 and logo[self.Y] == 0:
                  logo[self.DIR] = self.DOWN_LEFT
                  cornerBounces += 1
              elif logo[self.X] == self.WIDTH - 3 and logo[self.Y] == self.HEIGHT - 1:
                  logo[self.DIR] = self.UP_LEFT
                  cornerBounces += 1

              # Проверяем, не отскакивает ли логотип от левого края:
              elif logo[self.X] == 0 and logo[self.DIR] == self.UP_LEFT:
                  logo[self.DIR] = self.UP_RIGHT
              elif logo[self.X] == 0 and logo[self.DIR] == self.DOWN_LEFT:
                  logo[self.DIR] = self.DOWN_RIGHT

              # Проверяем, не отскакивает ли логотип от правого края:
              # (WIDTH - 3, поскольку 'DVD' состоит из трех букв.)
              elif logo[self.X] == self.WIDTH - 3 and logo[self.DIR] == self.UP_RIGHT:
                  logo[self.DIR] = self.UP_LEFT
              elif logo[self.X] == self.WIDTH - 3 and logo[self.DIR] == self.DOWN_RIGHT:
                  logo[self.DIR] = self.DOWN_LEFT

              # Проверяем, не отскакивает ли логотип от верхнего края:
              elif logo[self.Y] == 0 and logo[self.DIR] == self.UP_LEFT:
                  logo[self.DIR] = self.DOWN_LEFT
              elif logo[self.Y] == 0 and logo[self.DIR] == self.UP_RIGHT:
                  logo[self.DIR] = self.DOWN_RIGHT

              # Проверяем, не отскакивает ли логотип от нижнего края:
              elif logo[self.Y] == self.HEIGHT - 1 and logo[self.DIR] == self.DOWN_LEFT:
                  logo[self.DIR] = self.UP_LEFT
              elif logo[self.Y] == self.HEIGHT - 1 and logo[self.DIR] == self.DOWN_RIGHT:
                  logo[self.DIR] = self.UP_RIGHT

              if logo[self.DIR] != originalDirection:
                  # Меняем цвет при отскакивании логотипа:
                  logo[self.COLOR] = random.choice(self.COLORS)

              # Перемещаем логотип. (Координата X меняется на 2, поскольку
              # в терминале высота символов вдвое превышает ширину.)
              if logo[self.DIR] == self.UP_RIGHT:
                  logo[self.X] += 2
                  logo[self.Y] -= 1
              elif logo[self.DIR] == self.UP_LEFT:
                  logo[self.X] -= 2
                  logo[self.Y] -= 1
              elif logo[self.DIR] == self.DOWN_RIGHT:
                  logo[self.X] += 2
                  logo[self.Y] += 1
              elif logo[self.DIR] == self.DOWN_LEFT:
                  logo[self.X] -= 2
                  logo[self.Y] += 1

          # Отображает количество отскакиваний от углов:
          self.bext.goto(5, 0)
          self.bext.fg("white")
          print("Corner bounces:", cornerBounces, end="")

          for logo in logos:
              self.bext.goto(logo[self.X], logo[self.Y])
              self.bext.fg(logo[self.COLOR])
              print("DVD", end="")

          self.bext.goto(0, 0)

          sys.stdout.flush()  # (Нужно для программ, использующих модуль bext.)
          time.sleep(self.PAUSE_AMOUNT)
