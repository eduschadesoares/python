# -*- coding: utf-8 -*-

import sys
from datetime import *
import time

sys.path.append('..')

# SERVICES
CABELO = 0
BARBA = 1
BIGODE = 2

JORNADA_TRABALHO = 20

barbearia = None

class Barbeiro:
    @staticmethod
    def cortar_cabelo():
        print('Cortando cabelo, aguarde...')
        for i in range(1,4):
            print(i)
            time.sleep(1)

    @staticmethod
    def cortar_barba():
        print('Cortando barba, aguarde...')
        for i in range(1,5):
            print(i)
            time.sleep(1)

    @staticmethod
    def cortar_bigode():
        print('Cortando bigode, aguarde...')
        for i in range(1,6):
            print(i)
            time.sleep(1)


class Cliente:

    def __init__(self, id, service):
        self.id = id
        self.service = sorted(service)
        self.count = datetime.now()
        self.is_proximo = True


    def __str__(self):
        return str(self.id)

class Barbearia:
    fila = []


    def __init__(self):
        self.barbeiro = Barbeiro()


    def acomodar_clientes(self, cliente):
        print("")
        print("Cliente {} entrou na barbearia".format(cliente))
        print("Horário de chegada: {}:{}:{}".format(cliente.count.hour, cliente.count.minute, cliente.count.second))
        print("Serviço:")
        
        for s in cliente.service:
            if s == 0:
                print("- Cabelo") 
            if s == 1:
                print("- Barba") 
            if s == 2:
                print("- Bigode") 
        
        self.fila.append(cliente)


    def tam_fila(self):
        print("")
        if len(self.fila) == 0:
            return str("Não há clientes na fila")
        if len(self.fila) == 1:
            return str("Um cliente está na fila")
        return str("{} clientes estão na fila".format(len(self.fila)))


    def get_ok_outros(self, cliente):
        print('')
        print("Avisando os outros clientes...")
        for index, client in enumerate(self.fila, start=1):
            if client is not cliente:
                print('Cliente {:2}: Ok!'.format(str(client)), end=' ')
            else:
                print('Cliente {:2}: --!'.format(str(client)), end=' ')
            if index % 4 == 0:
                print("")
        print('')
        print('')


    def concorrer(self):
        primeiro = datetime.now()
        if len(self.fila) > 0:
            print('')
            print('Concorrendo...')
            for cliente in self.fila:
                if cliente.count < primeiro and cliente.is_proximo:
                    primeiro = cliente.count 
                    cliente_escolhido = cliente

            print('Vez do cliente {}.'.format(cliente_escolhido))
            self.get_ok_outros(cliente_escolhido)
            return cliente_escolhido
        else:
            print('')
            print("A barbearia está vazia!")
            sys.exit(0)


    def ser_atendido(self, cliente):
        print('Atendendo cliente.')
        if cliente.service is not None:
            for servico in cliente.service:
                if servico == CABELO:
                    self.barbeiro.cortar_cabelo()
                    print('Cliente {} cortou o cabelo'.format(cliente))

                if servico == BARBA:
                    self.barbeiro.cortar_barba()
                    print('Cliente {} cortou a barba'.format(cliente))

                if servico == BIGODE:
                    self.barbeiro.cortar_bigode()
                    print('Cliente {} cortou o bigode'.format(cliente))

                cliente.is_proximo = False
                cliente.service.remove(servico)

                return cliente
        return cliente


    def verifica_clientes(self, cliente):
        if len(cliente.service) == 0:
            self.fila.remove(cliente)
            print('O cliente {} foi embora'.format(cliente))

        for client in self.fila:
            if len(self.fila) == 1 and client is cliente:
                client.is_proximo = True
            if client is not cliente:
                client.is_proximo = True
            # print('Cliente {} é {}'.format(client, client.is_proximo))


# Run
def abre_barbearia():
    # Abre a barbearia
    global barbearia
    barbearia = Barbearia()


def recebe_acomoda_clientes():
    # Recebe os clientes
    C1 = Cliente(1, [BARBA, CABELO, BIGODE])
    C2 = Cliente(2, [CABELO])
    C3 = Cliente(3, [BIGODE])
    C4 = Cliente(4, [BARBA, CABELO, BIGODE])
    C5 = Cliente(5, [BARBA, CABELO, BIGODE])
    C6 = Cliente(6, [BARBA, CABELO, BIGODE])
    C7 = Cliente(7, [BARBA, CABELO, BIGODE])
    C8 = Cliente(8, [BARBA, CABELO, BIGODE])
    C9 = Cliente(9, [BARBA, CABELO, BIGODE])
    C10 = Cliente(10, [BARBA, CABELO, BIGODE])
    C11 = Cliente(11, [BARBA, CABELO, BIGODE])
    C12 = Cliente(12, [BARBA, CABELO, BIGODE])
    C13 = Cliente(13, [BARBA, CABELO, BIGODE])
    C14 = Cliente(14, [BARBA, CABELO, BIGODE])
    C15 = Cliente(15, [BARBA, CABELO, BIGODE])
    C16 = Cliente(16, [BARBA, CABELO, BIGODE])
    C17 = Cliente(17, [BARBA, CABELO, BIGODE])
    C18 = Cliente(18, [BARBA, CABELO, BIGODE])
    C19 = Cliente(18, [BARBA, CABELO, BIGODE])
    C20 = Cliente(20, [BARBA, CABELO, BIGODE])

    # Acomoda os clientes
    barbearia.acomodar_clientes(C1)
    barbearia.acomodar_clientes(C2)
    barbearia.acomodar_clientes(C3)
    barbearia.acomodar_clientes(C4)
    barbearia.acomodar_clientes(C5)
    barbearia.acomodar_clientes(C6)
    barbearia.acomodar_clientes(C7)
    barbearia.acomodar_clientes(C8)
    barbearia.acomodar_clientes(C9)
    barbearia.acomodar_clientes(C10)
    barbearia.acomodar_clientes(C11)
    barbearia.acomodar_clientes(C12)
    barbearia.acomodar_clientes(C13)
    barbearia.acomodar_clientes(C14)
    barbearia.acomodar_clientes(C15)
    barbearia.acomodar_clientes(C16)
    barbearia.acomodar_clientes(C17)
    barbearia.acomodar_clientes(C18)
    barbearia.acomodar_clientes(C19)
    barbearia.acomodar_clientes(C20)


def verifica_tam_fila():
    # Verifica quantidade de clientes na barbearia
    print(barbearia.tam_fila())


def inicia_expediente():
    for index, qntd_servicos in enumerate(range(JORNADA_TRABALHO), start=1):
        print('')
        print('Jornada de trabalho {}/{}'.format(index, JORNADA_TRABALHO))
        barbearia.verifica_clientes(barbearia.ser_atendido(barbearia.concorrer()))

    print('')
    print('Jornada de trabalho encerrada')
    if len(barbearia.fila) == 1:
        print('Restou 1 cliente na fila para ser atendido')
    else:
        print('Restaram {} clientes na fila para serem atendidos'.format(len(barbearia.fila)))


if __name__ == '__main__':
    print('Barbearia do Lamport')
    abre_barbearia()
    recebe_acomoda_clientes()
    verifica_tam_fila()
    inicia_expediente()
else:
    print("You're not supposed to executed this file by module")
    print("Try again please")