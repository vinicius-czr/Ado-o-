import datetime

ARQUIVO = "animais.txt"

def salvar_animais(animais):
    """Reescreve o arquivo com todos os animais"""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for a in animais:
            f.write(f"NOME: {a['nome']}\n")
            f.write(f"ESPÉCIE: {a['especie']}\n")
            f.write(f"RAÇA: {a['raca']}\n")
            f.write(f"IDADE: {a['idade']}\n")
            f.write(f"SAÚDE: {a['saude']}\n")
            f.write(f"DATA_CHEGADA: {a['data_chegada']}\n")
            f.write(f"COMPORTAMENTO: {a['comportamento']}\n")
            f.write("TAREFAS: " + "; ".join(a["tarefas"]) + "\n")
            f.write("---\n")

def carregar_animais():
    """Lê os animais do arquivo e retorna como lista de dicionários"""
    animais = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            linhas = f.read().split("---\n")
            for bloco in linhas:
                if bloco.strip() == "":
                    continue
                dados = {}
                tarefas = []
                for linha in bloco.strip().split("\n"):
                    chave, valor = linha.split(":", 1)
                    chave = chave.strip().upper()
                    valor = valor.strip()
                    if chave == "NOME":
                        dados["nome"] = valor
                    elif chave == "ESPÉCIE":
                        dados["especie"] = valor
                    elif chave == "RAÇA":
                        dados["raca"] = valor
                    elif chave == "IDADE":
                        dados["idade"] = valor
                    elif chave == "SAÚDE":
                        dados["saude"] = valor
                    elif chave == "DATA_CHEGADA":
                        dados["data_chegada"] = valor
                    elif chave == "COMPORTAMENTO":
                        dados["comportamento"] = valor
                    elif chave == "TAREFAS":
                        tarefas = [t.strip() for t in valor.split(";") if t.strip()]
                dados["tarefas"] = tarefas
                animais.append(dados)
    except FileNotFoundError:
        pass
    return animais

def adicionar_animal():
    nome = input("Nome do animal: ")
    especie = input("Espécie: ")
    raca = input("Raça: ")
    idade = input("Idade (em anos): ")
    saude = input("Estado de saúde: ")
    data_chegada = input("Data de chegada (AAAA-MM-DD): ")
    comportamento = input("Comportamento: ")

    animal = {
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "saude": saude,
        "data_chegada": data_chegada,
        "comportamento": comportamento,
        "tarefas": []
    }

    animais = carregar_animais()
    animais.append(animal)
    salvar_animais(animais)
    print(f"\n Animal '{nome}' adicionado com sucesso!\n")

