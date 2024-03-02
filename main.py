names = ["Maria", "João", "Ana", "Pedro", "Sofia"]
ages = [25, 32, 19, 45, 28]
sexes = ['F', 'M', 'F', 'M', 'F']
heights = [1.75, 1.62, 1.80, 1.68, 1.90]
weights = [68.5, 72.3, 65.8, 78.1, 70.2]
run_times = [12, 11, 13, 10, 12]
impulsions = [40, 33, 45, 32, 44]

def printLine(num_times=60, char='–'):
  line = char * num_times
  print(line)

def waitInput():
  input("Prima qualquer tecla para continuar...")

def invalidOption():
  print("Opção inválida")
  waitInput()

def addAthlete():
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
    printLine()
    print(f"Nome: {names[index]} | Idade: {ages[index]} | : Género: {sexes[index]} | Altura: {heights[index]}")
    printLine()
    waitInput()
  except ValueError:
    print("Erro: dados introduzidos inválidos")

def displayAthleteData():
  printLine()

  for index, name in enumerate(names):
    print(f"[{index + 1}]: {name}")

  printLine()
  try:
    number = int(input("número do atleta a consultar: "))
    if  0 < number <= len(names):
      index = number - 1
      print(f"Nome: {names[index]} | Idade: {ages[index]} | : Género: {sexes[index]} | Altura: {heights[index]}")
      waitInput()
    else:
      invalidOption()
  except ValueError:
    invalidOption()

def displayMenu():
  printLine()
  print("Menu:")
  print("1. Inserir dados de atleta")
  print("2. Eliminar dados de atleta")
  print("3. Listar dados de atleta")
  print("4. Dados Estatísticos")
  print("5. Sair")
  printLine()

def getMenuOption():
  while True:
    try:
      choice = int(input("Escolha opção (1-5): "))
      if 1 <= choice <= 5:
        return choice
      else:
        print("Opção inválida. Introduza um valor entre 1-5.")
    except ValueError:
      invalidOption()

def main():
  while True:
    displayMenu()
    user_choice = getMenuOption()

    if user_choice == 1:
      print("Opção 1.")
      addAthlete()
    elif user_choice == 2:
      print("Opção 2.")
      # Add your code for Option 2 here
    elif user_choice == 3:
      print("Opção 3.")
      displayAthleteData()
    elif user_choice == 4:
      print("Opção 4.")
      # Add your code for Option 4 here
    elif user_choice == 5:
      print("Adeus.")
      break

if __name__ == "__main__":
  main()
