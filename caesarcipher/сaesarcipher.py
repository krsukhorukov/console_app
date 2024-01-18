from string import ascii_uppercase

class CaesarCipher:
  def main(self):
    try:
      import pyperclip
    except ImportError:
      pass

    alphabet = ascii_uppercase
    answer = ''

    print(
      """
      Шифр Цезаря — древний алгоритм шифрования, использовавшийся
      Юлием Цезарем. Буквы в нем шифруютсяпутем сдвига
      их на определенное количество позиций в алфавите.
      Дистанция сдвига называется ключом.
      Например, если ключ равен 3, то A превращается в D, B — в E, C — в F и т. д.
      """
    )

    while True:
      print("Выберите действие: зашифровать или дишифровать?")
      choise = input("> ").lower()
      if choise.startswith('з'):
        operating_mode = 'зашифровать'
        break
      elif choise.startswith('д'):
        operating_mode = 'дишифровать'
        break
      print("Пожалуйста введите ваше действие, букву 'з' или 'д'.")

    while True:
      max_key_value = len(alphabet)
      print(f"Введите ключ - значение от 0 до {max_key_value}:")
      response = input("> ").upper()
      if not response.isdecimal():
        continue
      if 0 <= int(response) < max_key_value:
        key = int(response)
        break

    print(f"Введите сообщение для того, что бы его {operating_mode}.")
    gamers_message = input("> ")

    gamers_message = gamers_message.upper()

    for symbol in gamers_message:
      if symbol in alphabet:
        num = alphabet.find(symbol)

        if operating_mode == 'зашифровать':
          num += key
        elif operating_mode == 'дишифровать':
          num -= key

        if num >= len(alphabet):
          num = num - len(alphabet)
        elif num < 0:
          num = num + len(alphabet)

        answer = answer + alphabet[num]
      else:
        answer = answer + symbol

    print(f'Ваше сообщение: {answer}')
    while True:
      print("Хотите скопировать его в буфер обмена?(да/нет - д/н)")
      is_copy = input("> ")
      if is_copy.startswith('д'):
        pyperclip.copy(answer)
        print("Ваше сообщение скопировано с буфер обмена.")
        break
      elif is_copy.startswith('н'):
        print("Спасибо за использование нашего сервиса. С любовью(нет), разработчики!")
        print("До скорых встреч!")
        break
