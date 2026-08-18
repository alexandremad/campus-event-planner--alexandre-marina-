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

