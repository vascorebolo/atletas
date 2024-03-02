names = ["Maria", "João", "Ana", "Pedro", "Sofia"]
ages = [25, 32, 19, 45, 28]
sexes = ['F', 'M', 'F', 'M', 'F']
heights = [1.75, 1.62, 1.80, 1.68, 1.90]
weights = [68.5, 72.3, 65.8, 78.1, 70.2]
run_times = [12, 11, 13, 10, 12]
impulsions = [40, 33, 45, 32, 44]
arrays = [names, ages, sexes, heights, run_times, impulsions]

def printLine(num_times=60, char='–'):
  line = char * num_times
  print(line)

def waitInput():
  input("Prima qualquer tecla para continuar...")

def invalidOption():
  print("Opção inválida")
  waitInput()

def listNames():
  printLine()
  for index, name in enumerate(names):
    print(f"[{index + 1}]: {name}")
  printLine()

def askForIndex():
  try:
    number = int(input("número do atleta: "))

    if  0 < number <= len(names):
      return number - 1
    else:
      invalidOption()
  except ValueError:
    invalidOption()


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

def removeAthlete():
  listNames()

  try:
    index = askForIndex()

    if (index is not None):
      name = names[index]
      sex = sexes[index]

      for array in arrays:
        del array[index]

      printLine()
      print(f"Atleta {name} {'removido' if sex == 'M' else 'removida'}.")
      waitInput()
  except ValueError:
    invalidOption()

def displayAthleteData():
  listNames()

  try:
    index = askForIndex()
    printLine()
    print(index)
    printLine()
    if (index is not None):
      print(f"Nome: {names[index]} | Idade: {ages[index]} | : Género: {sexes[index]} | Altura: {heights[index]}")
      waitInput()
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
      if 1 <= choice <= 6:
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
      removeAthlete()
    elif user_choice == 3:
      print("Opção 3.")
      displayAthleteData()
    elif user_choice == 4:
      print("Opção 4.")
      # Add your code for Option 4 here
    elif user_choice == 5:
      print("Adeus.")
      break
    elif user_choice == 6:
      for array in arrays:
        for value in array:
          printLine()
          print(value)

if __name__ == "__main__":
  main()
