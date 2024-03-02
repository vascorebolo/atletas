def display_menu():
  print("Menu:")
  print("1. inserir dados de atleta")
  print("2. eliminar dados de atleta")
  print("3. listar dados de atleta")
  print("4. Dados Estatísticos")
  print("5. Sair")

def get_user_choice():
  while True:
    try:
      choice = int(input("Escolha opção (1-5): "))
      if 1 <= choice <= 5:
        return choice
      else:
        print("Opção inválida. Introduza um valor entre 1-5.")
    except ValueError:
      print("Erro: Introduza um número válido.")

def main():
  while True:
    display_menu()
    user_choice = get_user_choice()

    if user_choice == 1:
      print("Opção 1.")
      # Add your code for Option 1 here
    elif user_choice == 2:
      print("Opção 2.")
      # Add your code for Option 2 here
    elif user_choice == 3:
      print("Opção 3.")
      # Add your code for Option 3 here
    elif user_choice == 4:
      print("Opção 4.")
      # Add your code for Option 4 here
    elif user_choice == 5:
      print("Adeus.")
      break

if __name__ == "__main__":
  main()
