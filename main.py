import secrets
import string


def gerar_hexadecimal(tamanho: int) -> str:
    return secrets.token_hex(tamanho)


def gerar_bytes(tamanho: int) -> bytes:
    return secrets.token_bytes(tamanho)


def gerar_caracteres(tamanho: int) -> str:
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alfabeto) for _ in range(tamanho))


def main():
    while True:
        opcao = input(
            "Tipo de senha (hexadecimal, bytes, caracteres): "
        ).lower().strip()

        if opcao not in ("hexadecimal", "bytes", "caracteres"):
            print("Opção inválida! digite novamente")
            continue

        try:
            tamanho = int(input("Quantidade de caracteres: "))
            if tamanho <= 0:
                
                raise ValueError
        except ValueError:
            print("Digite um número válido maior que zero.")
            continue
            
        if opcao == "hexadecimal":
            print("Senha:", gerar_hexadecimal(tamanho))

        elif opcao == "bytes":
            print("Senha:", gerar_bytes(tamanho))

        elif opcao == "caracteres":
            print("Senha:", gerar_caracteres(tamanho))

        else:
            print("Opção inválida.")
            continue

        print("-" * 40)

        resposta = input("Gerar outra senha? (s/n): ").strip().lower()
        if resposta in ("sim", "s", "yes", "y"):
            continue

        else:

            break


if __name__ == "__main__":
    main()
