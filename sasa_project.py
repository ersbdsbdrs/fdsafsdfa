import requests

def quiz():
  response_all = requests.get('https://api.periodictableofelements.org/elements/')
  elements = response_all.json()
  response = requests.get('https://api.periodictableofelements.org/elements/quiz/')
  quizly = response.json()
  print(f'Успешно загрузил {len(elements)} элементов.')
  print(f'Успешно загрузил {len(quizly)} приблизительных ответов.')
  print("Начинаю квест...")

  symbol = quizly["type"]
  question = quizly["question"]
  choices = quizly["choices"]
  print(question)
  print(choices)

  answer = quizly["answer"]
  for element in elements:
    elements_atomic = element["atomic_number"]
    # (dodelat otvet)
  full_answer = []
  if answer == elements:
    full_answer = answer
  trying_to_answer = int(input("Введите атомную массу вашего ответа:"))
  if answer == trying_to_answer:
    print("Поздравляю, вы победили! Это действительно был", full_answer)
  else:
    print("К сожалению нет, правильный ответ был", answer)


def daily():
  response = requests.get('https://api.periodictableofelements.org/elements/element-of-the-day/')   # Запрашиваем дневной элемент.
  day_element = response.json()
  print(f'Загружено {len(day_element)} описаний элемента.')
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

while True:
  print("1 = Квест по элементам.")
  print("2 = Текущий дневной элемент.")
  print("Чтобы выйти нажмите любую другую цифру.")
  abbbc = int(input("Введите цифру:"))
  if abbbc == 1:
    quiz()
  elif abbbc == 2:
    daily()
  else:
    print("Выхожу..")
    break