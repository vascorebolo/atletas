names = ["Maria", "João", "Ana", "Pedro", "Sofia"]
ages = [25, 32, 19, 45, 28]
sexes = ['F', 'M', 'F', 'M', 'F']
heights = [1.75, 1.62, 1.80, 1.68, 1.90]
weights = [68.5, 72.3, 65.8, 78.1, 70.2]
run_times = [12, 11, 13, 10, 12]
impulsions = [40, 33, 45, 32, 44]
lists = [names, ages, sexes, heights, run_times, impulsions]

def print_line(char='▄', num_times=60):
  line = char * num_times
  print(line)

def wait_for_input():
  input("Prima enter para continuar...")

def invalid_option():
  print("Opção inválida")
  wait_for_input()

def list_names():
  print_line()
  for index, name in enumerate(names):
    print(f"[{index + 1}]: {name}")
  print_line()

def ask_for_index():
  try:
    number = int(input("número do atleta: "))

    if  0 < number <= len(names):
      return number - 1
    else:
      invalid_option()
  except ValueError:
    invalid_option()


def add_athlete():
  print("Inserir Dados")
  try:
    name = str(input("nome: "))
    age = int(input("idade: "))
    sex = str(input("género (m/f): "))
    height = float(input("altura (m): "))
    weight = float(input("peso (kg): "))
    runtime = int(input("tempo de corrida 100m (s): "))
    impulsion = int(input("impulsão (cm): "))

    names.append(name)
    ages.append(age)
    sexes.append(sex)
    heights.append(height)
    weights.append(weight)
    run_times.append(runtime)
    impulsions.append(impulsion)

    index = len(names) - 1
    print_line()
    print(f"Nome: {names[index]} | Idade: {ages[index]} | : Género: {sexes[index]} | Altura: {heights[index]}")
    print_line()
    wait_for_input()
  except ValueError:
    print("Erro: dados introduzidos inválidos")
    wait_for_input()

def remove_athlete():
  list_names()

  try:
    index = ask_for_index()

    if (index is not None):
      name = names[index]
      sex = sexes[index]

      for list in lists:
        del list[index]

      print_line()
      print(f"Atleta {name} {'removido' if sex == 'M' else 'removida'}.")
      wait_for_input()
  except ValueError:
    invalid_option()

def display_athletes_data():
  list_names()

  try:
    index = ask_for_index()

    if (index is not None):
      print(f"Nome: {names[index]} | Idade: {ages[index]} | : Género: {sexes[index]} | Altura: {heights[index]}")
      wait_for_input()
  except ValueError:
    invalid_option()

def display_menu():
  print_line()
  print("Menu Principal:")
  print("1. Inserir dados de atleta")
  print("2. Eliminar dados de atleta")
  print("3. Listar dados de atleta")
  print("4. Dados Estatísticos")
  print("5. Sair")
  print_line()

def get_menu_option():
  while True:
    try:
      choice = int(input("Escolha opção (1-5): "))
      if 1 <= choice <= 6:
        return choice
      else:
        print("Opção inválida. Introduza um valor entre 1-5.")
    except ValueError:
      invalid_option()

def display_stats_menu():
  print_line()
  print("Menu Estatísticas:")
  print("1. Média de alturas")
  print("2. Média de idades")
  print("3. Média de tempos de corrida")
  print("4. Sair")
  print_line()

def calcAgesAvg():
  total = 0
  agesTotalM = 0
  nrOfM = 0
  agesTotalF = 0
  nrOfF = 0

  for index, age in enumerate(ages):
    total += age

    if sexes[index] == 'M':
      agesTotalM += age
      nrOfM += 1
    else:
      agesTotalF += age
      nrOfF += 1

  print(f'A média de idades é {total / len(ages)}')
  print(f'A média de idades dos homens é {agesTotalM / nrOfM}')
  print(f'A média de idades das mulheres é {agesTotalF / nrOfF}')
  print_line('▒')
  wait_for_input()

def calcHeightAvg():
  total = 0
  for height in heights:
    total += height

  print(f'A média de alturas é {total / len(heights)}')
  print_line('▒')
  wait_for_input()

def display_stats():
  while True:
    display_stats_menu()
    choice = int(input('Escolha opção (1-4): '))

    match choice:
      case 1:
        calcHeightAvg()
      case 2:
        calcAgesAvg()
      case _:
        break

def main():
  while True:
    display_menu()
    user_choice = get_menu_option()

    match user_choice:
      case 1:
        add_athlete()
      case 2:
        remove_athlete()
      case 3:
        display_athletes_data()
      case 4:
        display_stats()
      case 5:
        print('Adeus.')
        break
      case 6:
        for list in lists:
          for value in list:
            print_line()
            print(value)

if __name__ == "__main__":
  main()
