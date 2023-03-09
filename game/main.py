import random

options = ("PIEDRA", "PAPEL", "TIJERA")
rounds = 1


def choose_options():
  user_option = input("Piedra, papel o tijera: ")
  user_option = user_option.upper()
  #eleccion aleatoria de la opcion del pc
  computer_option = random.choice(options)
  computer_option = computer_option.upper()

  return user_option, computer_option


def print_header():
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)


def ganador_ronda(usuario_opc, computer_opc, user_wins, compute_wins):
  wins_compu = compute_wins
  wins_user = user_wins
  if usuario_opc == computer_opc:
    print("Es un empate")
  elif usuario_opc == "PIEDRA" and computer_opc == "TIJERA":
    wins_user += 1
    print("Gana el usuario")
  elif usuario_opc == "PIEDRA" and computer_opc == "PAPEL":
    wins_compu += 1
    print("Gana la computadora")
  elif usuario_opc == "TIJERA" and computer_opc == "PAPEL":
    wins_user += 1
    print("Gana el usuario")
  elif usuario_opc == "TIJERA" and computer_opc == "PIEDRA":
    wins_compu += 1
    print("Gana la computadora")
  elif usuario_opc == "PAPEL" and computer_opc == "PIEDRA":
    wins_user += 1
    print("Gana el usuario")
  elif usuario_opc == "PAPEL" and computer_opc == "TIJERA":
    wins_compu += 1
    print("Gana la computadora")

  print(f"Usuario va: {wins_user}")
  print(f"Computadora va: {wins_compu}")

  return wins_user, wins_compu


def elegir_ganador(user_wins, compute_wins):
  existsGanador = False
  print("Fin de la partida")
  if (compute_wins == 2):
    existsGanador = True
    print('Gano la Computadora')
  if (user_wins == 2):
    existsGanador = True
    print('Gano el usuario')

  return existsGanador

def run_game(rounds):
  compute_wins = 0
  user_wins = 0
  existsGanador = False
  rounds = rounds

  while True:

    print_header()

    usuario_opc, computer_opc = choose_options()

    if not usuario_opc in options:
      print("Esa opcion no es valida")
      continue
    else:
      print(f"Usuario eligio {usuario_opc}")
      print(f"Computadora eligio {computer_opc}")

      user_wins, compute_wins = ganador_ronda(usuario_opc, computer_opc,
                                            user_wins, compute_wins)

    if user_wins == 2 or compute_wins == 2:
      existsGanador = elegir_ganador(user_wins, compute_wins)
    if existsGanador == True:
      break

    rounds += 1
    

run_game(rounds)