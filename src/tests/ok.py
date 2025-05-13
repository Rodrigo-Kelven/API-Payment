import requests

url = "http://127.0.0.1:8000/api-auten_auth/user/register/"

# Defina os dados que você deseja enviar
payload = {
    "username": "testuser",
    "email": "testuser@example.com",
    "full_name": "Test User",
    "password": "okokokokok"
}

# Envia a requisição POST com dados em application/x-www-form-urlencoded
response = requests.post(url, data=payload)

# Verifica a resposta
print(response.status_code)

if response.status_code == 201:
    response_data = response.json()
    print(response_data)  # Exibe a resposta completa
    
    # Verifique se o ID está presente na resposta
    user_id = response_data.get("id")  # Ajuste conforme necessário
    if user_id is not None:
        print(f"User  ID: {user_id}")
    else:
        print("ID não encontrado na resposta.")
else:
    print("Erro ao registrar usuário:", response.json())