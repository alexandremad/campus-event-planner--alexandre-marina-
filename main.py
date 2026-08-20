import re

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

import re

def validar_data(data):
    padrao = r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    return bool(re.match(padrao, data))


def adicionarEvento(listaEventos):
    print("\n--- Novo Evento ---")
    nome = input("Nome do evento: ")
    data = input("Data (DD/MM/AAAA): ")
    while (validar_data(data) == False):
        data = input("Data (DD/MM/AAAA): ")
    hora = input("Hora (HH:MM): ")
    local = input("Local: ")
    cidade = input("Cidade/UF: ")
    categoria = input("Categoria: ")

    novoEvento = {
        "nome": nome, 
        "data" : data,
        "local" : local,
        "categoria" : categoria,
        "cidade": cidade
    }

    listaEventos.append(novoEvento)
    print("\nEvento adicionado com sucesso!")


def listar_eventos(listaDeEvento):
    """Lista os eventos cadatrados. """
    print("\n--- Lista de Eventos ---")
    for novoEvento in listaDeEvento:
        if novoEvento[2] > 0:                   
            print(f"Nome: {novoEvento[0]} | data: R$ {novoEvento[1]} | local: {novoEvento[3]} | categoria: {novoEvento[4]} | cidade: {novoEvento[5]}")
        
def filtrar_eventos(listaDeEvento):
    
    nome_busca = input("Digite o nome (ou parte dele) para buscar: ")
    encontrou = False
    
    print("\n--- RESULTADO DA BUSCA ---")
    for novoEvento in listaDeEvento:
       
        if nome_busca.lower() in novoEvento[0].lower():
            print(f"Nome: {novoEvento[0]} | data: R$ {novoEvento[1]} | local: {novoEvento[2]} | categoria: {novoEvento[3]} | cidade: {novoEvento[4]}")
            encontrou = True
            
    if not encontrou:
        print("Nenhum produto encontrado com esse termo.")   

def marcar_participado(listaDeEventos):
    """Marca um evento da lista como participado."""
    listar_eventos(listaDeEventos)
    if not listaDeEventos:
        return

    try:
        num = int(input("Digite o número do evento que você participou: ")) - 1
        if 0 <= num < len(listaDeEventos):
            listaDeEventos[num]["participado"] = True
            print(f"\nEvento '{listaDeEventos[num]['nome']}' marcado como participado!")
        else:
            print("Número de evento inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def gerar_relatorio(listaDeEventos):
    """Gera um resumo estatístico dos eventos."""
    total = len(listaDeEventos)
    participados = sum(1 for e in listaDeEventos if e["participado"])
    
    print("\n--- RELATÓRIO DE EVENTOS ---")
    print(f"Total de eventos cadastrados: {total}")
    print(f"Eventos participados: {participados}")
    print(f"Eventos pendentes: {total - participados}")        



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
            adicionarEvento(listaDeEventos)
        elif opcao == "2":
            listar_eventos(listaDeEventos)
        elif opcao == "3":
            filtrar_eventos (listaDeEventos)
        elif opcao == "4":
            marcar_participado(listaDeEventos)
        elif opcao == "5":
            gerar_relatorio(listaDeEventos)
        elif opcao == "6":
            print("Até o proxímo evento!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__": 
    main()