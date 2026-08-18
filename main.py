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


def displayMenu():
    print("=== Planejador de Eventos do Campus ===")
    print("1. Adicionar Evento")
    print("2. Ver Todos os Eventos")
    print("3. Filtrar por Categoria")
    print("4. Marcar Evento como Participado")
    print("5. Gerar Relatório")
    print("6. Sair")


def main():
    while True:
        displayMenu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            AdicionarEvento()
        elif opcao == "2":
            VerTodosEvento ()
        elif opcao == "3":
            FiltrarporEventos (listaEventos, categiria)
        elif opcao == "4":
            MarcarEventoAtendido(listaEventos, id)
        elif opcao == "5":
            GerarRelatorio(listaEventos)
        elif opcao == "6":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()