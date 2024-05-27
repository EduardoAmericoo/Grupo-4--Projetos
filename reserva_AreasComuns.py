import json
from datetime import datetime
import os
os.system('cls')

areas_comuns = ["Piscina", "Quadra", "Churrasqueira", "Salão de Festas"]

def main():
    while True:
        print("\nMenu Principal:")
        print("1. Fazer Reserva")
        print("2. Listar Reservas")
        print("3. Cancelar Reserva")
        print("4. Finalizar")
        
        escolha = input("Escolha a opção desejada: ")
        
        if escolha == '4':
            print("Finalizando o programa...")
            break
        elif escolha == '1':
            fazer_reserva()
        elif escolha == '2':
            listar_reservas()
        elif escolha == '3':
            cancelar_reserva()
        else:
            print("Escolha inválida. Tente novamente.")

def fazer_reserva():
    while True:
        print("\nÁreas Comuns Disponíveis para Reserva:")
        print("1. Piscina")
        print("2. Quadra")
        print("3. Churrasqueira")
        print("4. Salão de festas")
        print("V. Voltar para o Menu Principal")
        
        escolha = input("Escolha a área que deseja reservar (ou 'V' para voltar): ")
        
        if escolha.upper() == 'V':
            return
        
        if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(areas_comuns):
            print("Escolha inválida. Tente novamente.")
            continue
        
        area_escolhida = areas_comuns[int(escolha) - 1]
        print(f"Área escolhida: {area_escolhida}")
        
        while True:
            data = input("Insira a data da reserva (dd/mm/aaaa): ")
            if not validar_data(data):
                print("Data inválida ou data já passou. Tente novamente.")
                continue

            horario_inicio = input("Insira o horário de início da reserva (hh:mm): ")
            if not validar_horario(horario_inicio):
                print("Horário de início inválido. Tente novamente.")
                continue

            horario_fim = input("Insira o horário de término da reserva (hh:mm): ")
            if not validar_horario(horario_fim):
                print("Horário de término inválido. Tente novamente.")
                continue
            
            if horario_inicio >= horario_fim:
                print("O horário de término deve ser após o horário de início. Tente novamente.")
                continue

            reserva = {
                "area": area_escolhida,
                "data": data,
                "horario_inicio": horario_inicio,
                "horario_fim": horario_fim
            }
            
            if verificar_conflito(reserva):
                print("Conflito de reserva! Já existe uma reserva para esta área no mesmo dia e horário.")
                continue
            
            salvar_reserva(reserva)
            print("Reserva salva com sucesso!")
            break

def validar_data(data):
    try:
        data_reserva = datetime.strptime(data, "%d/%m/%Y")
        data_atual = datetime.now()
        if data_reserva.date() < data_atual.date():
            return False
        return True
    except ValueError:
        return False

def validar_horario(horario):
    try:
        datetime.strptime(horario, "%H:%M")
        return True
    except ValueError:
        return False

def verificar_conflito(nova_reserva):
    try:
        with open('reservas.json', 'r') as file:
            reservas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

    for reserva in reservas:
        if (reserva['area'] == nova_reserva['area'] and
            reserva['data'] == nova_reserva['data'] and
            not (nova_reserva['horario_fim'] <= reserva['horario_inicio'] or
                 nova_reserva['horario_inicio'] >= reserva['horario_fim'])):
            return True
    
    return False

def salvar_reserva(reserva):
    try:
        with open('reservas.json', 'r') as file:
            reservas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        reservas = []

    reservas.append(reserva)
    
    try:
        with open('reservas.json', 'w') as file:
            json.dump(reservas, file, indent=4)
        print("Reserva salva no arquivo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar reserva: {e}")

def cancelar_reserva():
    listar_reservas()
    try:
        with open('reservas.json', 'r') as file:
            reservas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Nenhuma reserva encontrada.")
        return
    
    if not reservas:
        print("Nenhuma reserva encontrada.")
        return

    reserva_id = input("Insira o ID da reserva que deseja cancelar: ")

    if reserva_id.isdigit() and 0 <= int(reserva_id) < len(reservas):
        reservas.pop(int(reserva_id))
        try:
            with open('reservas.json', 'w') as file:
                json.dump(reservas, file, indent=4)
            print("Reserva cancelada com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar cancelamento: {e}")
    else:
        print("Número da reserva inválido.")

def listar_reservas():
    try:
        with open('reservas.json', 'r') as file:
            reservas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Nenhuma reserva encontrada.")
        return
    
    if not reservas:
        print("Nenhuma reserva encontrada.")
        return

    print("\nReservas Atuais:")
    for num_resX, reserva in enumerate(reservas):
        print(f"Número da reserva: {num_resX}")
        print(f"Área: {reserva['area']}")
        print(f"Data: {reserva['data']}")
        print(f"Horário: {reserva['horario_inicio']} - {reserva['horario_fim']}")
        print("-----------")

if __name__ == "__main__":
    main()
