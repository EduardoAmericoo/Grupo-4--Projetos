import json
from datetime import datetime
import time 
import os

def obter_proximo_id():
    file = 'database/reservas.json'
    
    with open(file, mode='r') as arquivo:
        read = arquivo.read()
        data = json.loads(read)
        
        ids = [int(row['id']) for row in data]
        return max(ids) + 1 if ids else 1

def fazerReserva(id, user, area_escolhida, data, horario_inicio, horario_fim):

    reserva = {
        "id": id,
        "usuario_reservou": user,
        "area": area_escolhida,
        "data": data,
        "horario_inicio": horario_inicio,
        "horario_fim": horario_fim
    }
    
    if verificarConflito(reserva):
        print("\033[1;31mConflito de reserva! Já existe uma reserva para esta área no mesmo dia e horário.\033[m")
    
    reserva_salva = salvarReserva(reserva)
    
    if reserva_salva:
        print("\033[1;32mReserva salva com sucesso!\033[m")

        return reserva_salva

def salvarReserva(reserva):
    reserva_salva = False
    
    try:
        with open('database/reservas.json', 'r') as file:
            reservas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        reservas = []

    reservas.append(reserva)
    
    try:
        with open('database/reservas.json', 'w') as file:
            json.dump(reservas, file, indent=4)

            reserva_salva = True

    except Exception as e:
        print(f"\033[1;31mErro ao salvar reserva: {e}\033[m")
    
    return reserva_salva

def atualizarReserva(id):
    file = 'database/reservas.json'
    reserva_updated = False 
    
    reservas = buscarReservas()
    for reserva in reservas:
        if id == reserva['id']:
            os.system('cls') 
            print("Digite as informações em respeito a nova reserva: ")

            reserva['data'] = str(input("Data: [00/00/0000] "))     
            if not validarData(reserva['data']):
                print("\033[1;31mData inválida ou data já passou. Tente novamente.\033[m")
                continue    

            reserva['horario_inicio'] = str(input("Horário de início: [00:00] "))      
            if not validarHorario(reserva['horario_inicio']):
                print("\033[1;31mHorário de início inválido. Tente novamente.\033[m")
                continue
            
            reserva['horario_fim'] = str(input("Horário de término: [00:00] "))      
            if not validarHorario(reserva['horario_fim']):
                print("\033[1;31mHorário de término inválido. Tente novamente.\033[m")
                continue

            if reserva['horario_inicio'] >= reserva['horario_fim']:
                print("\033[1;31mO horário de término deve ser após o horário de início. Tente novamente.\033[m")
                continue
            
            with open(file, 'w', encoding='utf8') as arquivo:
                arquivo.write(json.dumps(reservas, indent=4))
        
                reserva_updated = True
            break
    
    return reserva_updated

def cancelarReserva(reserva_id, lista):
    reserva_cancelada = False

    lista.pop(int(reserva_id))
    try:
        with open('database/reservas.json', 'w') as file:
            json.dump(lista, file, indent=4)
        
        reserva_cancelada = True

    except Exception as e:
        print(f"\033[1;31mErro ao salvar cancelamento: {e}\033[m")

    return reserva_cancelada 

def listarReservas():
    try:
        with open('database/reservas.json', 'r') as file:
            reservas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\033[1;31mNenhuma reserva encontrada.\033[m")
    
    print("="*10)
    print(" RESERVAS ")
    print("="*10)
    
    for num_resX, reserva in enumerate(reservas):
        print(f"Número da reserva: {num_resX}")
        print(f"Quem reservou: {reserva['usuario_reservou']}")
        print(f"Área: {reserva['area']}")
        print(f"Data: {reserva['data']}")
        print(f"Horário: {reserva['horario_inicio']} - {reserva['horario_fim']}")
        print("-----------")

def buscarReservas():
    with open('database/reservas.json', 'r') as file:
        reservas = json.load(file) 
    
    return reservas

def validarData(data):
    try:
        data_reserva = datetime.strptime(data, "%d/%m/%Y")
        data_atual = datetime.now()
        if data_reserva.date() < data_atual.date():
            return False
        return True
    except ValueError:
        return False

def validarHorario(horario):
    try:
        datetime.strptime(horario, "%H:%M")
        return True
    except ValueError:
        return False

def verificarConflito(nova_reserva):
    try:
        with open('database/reservas.json', 'r') as file:
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