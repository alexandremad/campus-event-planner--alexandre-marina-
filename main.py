eventoBase = {
    "data": "10/09/2026",
    "local": "Mané Garrincha",
    "hora": "19:00",
    "cidade" : "Brasília/DF",
    "nome": "Encontro de Python",
    "valor": 200.00,
    "categoria": "Computação"
}

listaDeEventos = []

def adicionarEvento(listaEventos, nome, data, local, categoria, cidade):
    novoEvento = {
        "nome": nome, 
        "data" : data,
        "local" : local,
        "categoria" : categoria,
        "cidade": cidade
    }

    listaEventos.append(novoEvento)


def listar_eventos(listaDeEvento):
    """Lista os eventos cadatrados. """
    print("\n--- Lista de Eventos ---")
    for novoEvento in listaDeEvento:
        if novoEvento[2] > 0:                   
            print(f"Nome: {novoEvento[0]} | data: R$ {novoEvento[1]} | local: {novoEvento[3]} | categoria: {novoEvento[4]} | cidade: {novoEvento[5]}")
        

def displayMenu():
    print("=== Planejador de Eventos do Campus ===")
    print("1. Adicionar Evento")
    print("2. Ver Todos os Eventos")
    print("3. Filtrar por Categoria")
    print("4. Marcar Evento como Participado")
    print("5. Gerar Relatório")
    print("6. Sair")
