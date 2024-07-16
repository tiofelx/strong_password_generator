import random
import string

def generate_strong_password(length=12):
    # Definindo os caracteres disponíveis para a senha
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Assegurando que a senha tenha pelo menos uma letra maiúscula, uma letra minúscula, um dígito e um caractere especial
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Preenchendo o restante da senha com caracteres aleatórios
    password += random.choices(all_characters, k=length-4)

    # Embaralhando os caracteres da senha para garantir aleatoriedade
    random.shuffle(password)

    # Convertendo a lista de caracteres em uma string
    return ''.join(password)

# Exemplo de uso do gerador de senhas
if __name__ == "__main__":
    password_length = 16  # Defina o comprimento desejado da senha
    strong_password = generate_strong_password(password_length)
    print(f"Senha forte gerada: {strong_password}")
