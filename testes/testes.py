def teste_validos():
    print("=== TESTES VÁLIDOS ===")

    inputs = ["jogar", "a", "e", "i", "o", "u", "sair"]

    for i in inputs:
        print(f"Input válido: {i}")

teste_validos()

def teste_invalidos():
    print("=== TESTES INVÁLIDOS ===")

    inputs = ["ab", "1", "@", "", "mesa"]

    for i in inputs:
        print(f"Input inválido: {i}")

teste_invalidos()

