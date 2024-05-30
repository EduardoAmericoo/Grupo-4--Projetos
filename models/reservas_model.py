import json
from datetime import datetime
import time 
import os
os.system('cls')

def fazerReserva(area_escolhida, data, horario_inicio, horario_fim):

    reserva = {
        "area": area_escolhida,
        "data": data,
        "horario_inicio": horario_inicio,
        "horario_fim": horario_fim
    }
    
    if verificarConflito(reserva):
        print("Conflito de reserva! Já existe uma reserva para esta área no mesmo dia e horário.")
    
    reserva_salva = salvarReserva(reserva)
    
    if reserva_salva:
        print("Reserva salva com sucesso!")

        return reserva_salva

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
        print(f"Erro ao salvar reserva: {e}")
    
    return reserva_salva

def cancelarReserva(reserva_id, lista):
    reserva_cancelada = False

    lista.pop(int(reserva_id))
    try:
        with open('database/reservas.json', 'w') as file:
            json.dump(lista, file, indent=4)
        
        reserva_cancelada = True

    except Exception as e:
        print(f"Erro ao salvar cancelamento: {e}")

    return reserva_cancelada 

def listarReservas():
    try:
        with open('database/reservas.json', 'r') as file:
            reservas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Nenhuma reserva encontrada.")
    
    print("="*10)
    print(" RESERVAS ")
    print("="*10)
    
    for num_resX, reserva in enumerate(reservas):
        print(f"Número da reserva: {num_resX}")
        print(f"Área: {reserva['area']}")
        print(f"Data: {reserva['data']}")
        print(f"Horário: {reserva['horario_inicio']} - {reserva['horario_fim']}")
        print("-----------")

def buscarReservas():
    with open('database/reservas.json', 'r') as file:
        reservas = json.load(file) 
    
    return reservas