# Gerador de Senhas Fortes

Este script em Python gera senhas fortes aleatórias com base nos requisitos mínimos de segurança. Ele assegura que cada senha contenha pelo menos uma letra maiúscula, uma letra minúscula, um dígito e um caractere especial.

## Funcionalidades

- Gera senhas aleatórias com requisitos mínimos de segurança.
- Permite especificar o comprimento desejado da senha.

## Requisitos

- Python 3.x

## Uso

1. Defina o comprimento desejado da senha modificando a variável `password_length` no código.
2. Execute o script utilizando Python:

   ```bash
   python strong_password_generator.py

## Exemplo de uso
if __name__ == "__main__":
    password_length = 16  # Defina o comprimento desejado da senha
    strong_password = generate_strong_password(password_length)
    print(f"Senha forte gerada: {strong_password}")
