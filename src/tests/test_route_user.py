import requests

from core.config.config import app_logger

def test_register_user():
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
    print("Status Code:", response.status_code)
    
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



def test_login_user():
    url = "http://127.0.0.1:8000/api-auten_auth/login"

    # Defina os dados que você deseja enviar
    payload = {
        "username": "testuser@example.com",
        "password": "okokokokok"
    }

    # Envia a requisição POST com dados em application/x-www-form-urlencoded
    response = requests.post(url, data=payload)

    # Verifica a resposta
    print("Status Code:", response.status_code)
    
    assert response.status_code == 200  # código esperado para login bem-sucedido

    response_data = response.json()
    print(response_data)  # para debug

    # Verifique se o token está presente na resposta
    token = response_data.get("access_token") or response_data.get("token")
    assert token is not None, "Token não encontrado na resposta"

    print(f"Token recebido: {token}")


def test_get_current_user():

    url = "http://127.0.0.1:8000/api-auten_auth/login"


    # 1. Primeiro, faça login para obter o token de acesso
    login_data = {
        "username": "testuser@example.com",  # ou "email", conforme sua API
        "password": "okokokokok"
    }

    login_response = requests.post(url, data=login_data)

    # Verifica a resposta
    print("Status Code:", login_response.status_code)
    assert login_response.status_code == 200  # código esperado para login bem-sucedido

    token = login_response.json().get("access_token")
    assert token is not None

    # 2. Use o token no cabeçalho Authorization para acessar o endpoint protegido
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("http://127.0.0.1:8000/api-auten_auth/user/me/", headers=headers)

    assert response.status_code == 202
    user_data = response.json()
    assert user_data.get("email") == "testuser@example.com"  # ajuste conforme esperado


def test_update_user():
    
    login_url = "http://127.0.0.1:8000/api-auten_auth/login"
    user_me_url = "http://127.0.0.1:8000/api-auten_auth/user/me/"
    update_url = "http://127.0.0.1:8000/api-auten_auth/user/update-account-me/?email=testuser@example.com"

    # 1. Login para obter token
    login_data = {
        "username": "testuser@example.com",
        "password": "okokokokok"
    }

    login_response = requests.post(login_url, data=login_data)
    assert login_response.status_code == 200, f"Login falhou: {login_response.text}"

    token = login_response.json().get("access_token")
    assert token is not None, "Token não retornado no login"

    headers = {"Authorization": f"Bearer {token}"}

    # 2. Verifica usuário atual
    user_response = requests.get(user_me_url, headers=headers)
    assert user_response.status_code == 202, f"Falha ao obter usuário atual: {user_response.text}"
    user_data = user_response.json()
    assert user_data.get("email") == "testuser@example.com"

    # 3. Atualiza dados do usuário
    update_payload = {
        "username": "testuserok",
        "email": "testuser@example.com",
        "full_name": "Test User Updated",
    }
    update_response = requests.put(update_url, json=update_payload, headers=headers)
    assert update_response.status_code == 201, f"Falha ao atualizar usuário: {update_response.text}"

    updated_data = update_response.json()
    assert updated_data.get("email") == update_payload["email"]
    assert updated_data.get("full_name") == update_payload["full_name"]
    assert updated_data.get("username") == update_payload["username"]

    print(f"Teste de atualização de usuário: {updated_data.get("username")} passou com sucesso.")


def test_delete_user():

    login_url = "http://127.0.0.1:8000/api-auten_auth/login"
    delete_url = "http://127.0.0.1:8000/api-auten_auth/user/delete-account-me/"

    # 1. Login para obter token
    login_data = {
        "username": "testuser@example.com",
        "password": "okokokokok"
    }

    login_response = requests.post(login_url, data=login_data)
    assert login_response.status_code == 200, f"Login falhou: {login_response.text}"

    token = login_response.json().get("access_token")
    assert token is not None, "Token não retornado no login"

    headers = {"Authorization": f"Bearer {token}"}

    # 3. Envia a requisição DELETE autenticada
    delete_response = requests.delete(delete_url, headers=headers)
    
    # 4. Valida a resposta
    assert delete_response.status_code == 200 or delete_response.status_code == 204, \
        f"Falha ao deletar usuário: {delete_response.text}"

    print("Usuário deletado com sucesso.")