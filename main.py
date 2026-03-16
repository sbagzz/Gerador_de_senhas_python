import secrets
import string
import os 

def gerar_hexadecimal(tamanho: int) -> str:
    return secrets.token_hex(tamanho)


def gerar_bytes(tamanho: int) -> bytes:
    return secrets.token_bytes(tamanho)


def gerar_caracteres(tamanho: int) -> str:
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alfabeto) for _ in range(tamanho))

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        opcao = input(
            "Tipo de senha (hexadecimal, bytes, caracteres): "
        ).lower().strip()

        limpar_tela()

        if opcao not in ("hexadecimal", "bytes", "caracteres"):
            print("Opção inválida! digite novamente")
            continue
   
        limpar_tela()


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

        while True:
            resposta = input("Gerar outra senha? (s/n): ").strip().lower()    

            if resposta in ("sim", "s", "yes", "y"):
                limpar_tela()
                break

            elif resposta in ("não", "n", "no", "n"):
                print("Encerrando o programa.")
                exit()
                
            else:
                print("Resposta inválida! Digite 's' para sim ou 'n' para não.")

if __name__ == "__main__":
    main()
