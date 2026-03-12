# Gerador de Senhas Seguras em Python 🔐

Um pequeno utilitário em Python para criar senhas fortes e aleatórias.  
Usa o módulo padrão `secrets` para garantir geração segura, com opções de hex, bytes ou conjunto de caracteres (letras, números e símbolos).

---

## 🚀 Funcionalidades

- Cria senhas em três formatos:
  - **Hexadecimal**
  - **Bytes**
  - **Caracteres** (letras maiúsculas, minúsculas, dígitos e símbolos)
- Interface simples via **linha de comando**
- Validação robusta das entradas fornecidas pelo usuário

---

## 🧰 Tecnologias usadas

- Python 3.x
- Biblioteca standard: `secrets`, `string`

---

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/sbagzz/Gerador_de_senhas_python.git
   cd gerador-de-senhas-python
   ```

2. (Opcional) crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

---

## ▶️ Como executar

Execute o script principal:

```bash
python main.py
```

Siga as instruções na tela para escolher o tipo e o comprimento da senha.

---

## 📘 Exemplos de uso

```bash
$ python main.py
Selecione o tipo de senha:
1) Hexadecimal
2) Bytes
3) Caracteres
> 3
Digite o comprimento desejado: 12
Senha gerada: 8fG!k2#pQwZ@
```

---

## 📄 Contribuição

Este repositório é fornecido "como está" e não está aberto a contribuições externas.

---

## 📝 Licença

Este projeto está licenciado sob a **MIT License**.  
Veja o arquivo [`LICENSE`](LICENSE) para mais detalhes.

---

Se precisar de alguma outra melhoria ou de ajuda com o código, é só chamar! 💬
