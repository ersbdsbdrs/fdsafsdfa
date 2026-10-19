import requests


class APIPeriodical:

  def all_respone(self):
    response_all = requests.get('https://api.periodictableofelements.org/elements/')
    elements = response_all.json()

    return elements

  def quiz_response(self):
    response_quiz = requests.get('https://api.periodictableofelements.org/elements/quiz/')
    quizly = response_quiz.json()

    return quizly

  def daily_element(self):
    response_daily = requests.get('https://api.periodictableofelements.org/elements/element-of-the-day/')
    day_element = response_daily.json()

    return day_element



def quiz():
  api = APIPeriodical()
  elements = api.all_respone()
  quizly = api.quiz_response()

  print("Начинаю квест...")
  storage = []
  question = quizly["question"]
  choices = quizly["choices"]
  answer = quizly["answer"]
  if question == "Which element am I?":
    clues = quizly["clues"]
    print(clues)

  print(question)
  print(choices)

  approx_answer = 0
  for element in elements:
    if element["atomic_number"] == answer:
      atomic_numbera = element["atomic_number"]
      symbol_numbera = element["symbol"]
      name_numbera = element["name"]
      storage.append(name_numbera)
      storage.append(symbol_numbera)
      storage.append(atomic_numbera)
      approx_answer = answer
      break
  print("Подсказка:Если не нужен атомный номер, пишите Value вашего ответа.")
  if approx_answer > 0:
    trying_to_answer = int(input("Введите атомный номер вашего ответа: "))
  else:
    trying_to_answer = input("Введите ваш ответ: ")
  if approx_answer == trying_to_answer:
    print("Поздравляю, вы победили! Это действительно был", storage)
  else:
    print("К сожалению нет, правильный ответ был", answer)


def daily():
  api = APIPeriodical
  day_element = api.daily_element()
  print("Попытка вывести элемент...")

  storage = []            # Сохраняем все нужные описания элемента.

  name_of_element = day_element["name"]
  storage.append(name_of_element)
  symbol_of_element = day_element["symbol"]
  storage.append(symbol_of_element)
  atomic_number_of_element = day_element["atomic_number"]
  storage.append(atomic_number_of_element)

  print(storage)            # Выводим элемент.
  print("День текущего элемента: ")

  print(day_element["date"])


def element_finder():
  response_all = requests.get('https://api.periodictableofelements.org/elements/')
  elements = response_all.json()
  print("Если поиск ничего не найдет, вас вернет на главный экран.")
  elementsts = int(input("Введите атомный номер: "))
  for element in elements:
    if element["atomic_number"] == elementsts:
      sasa = element
      print(sasa)



while True:
  print("1 = Квест по элементам.")
  print("2 = Текущий дневной элемент.")
  print("3 = Поиск элемента по атомному числу.")
  print("Чтобы выйти нажмите любую другую цифру.")
  abbbc = int(input("Введите цифру:"))
  if abbbc == 1:
    quiz()
  elif abbbc == 2:
    daily()
  elif abbbc == 3:
    element_finder()
  else:
    print("Выхожу..")
    break



