from fastapi.testclient import TestClient
from tests.api.utils.papeis import create_papel_papel_valido, create_papel_invalido


def test_cria_papel(client: TestClient) -> None:
    body = create_papel_papel_valido()
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 200
    assert content["cnpj"] == body["cnpj"]


def test_cria_papel_com_sigla_invalida(client: TestClient) -> None:
    body = create_papel_invalido(['sigla'])
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 422
