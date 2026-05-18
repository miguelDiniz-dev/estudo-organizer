from unittest.mock import patch
from src.main import adicionar_tarefa, tarefas, obter_dica


def test_adicionar_tarefa_sucesso():
    tarefas.clear()
    assert adicionar_tarefa("Python", 2) is True
    assert len(tarefas) == 1


def test_lista_comeca_vazia():
    tarefas.clear()
    assert len(tarefas) == 0


@patch('src.main.requests.get')
def test_obter_dica_integracao_api(mock_get):
    """
    Testa a integração com a API pública, simulando (mockando) a resposta
    para garantir que o sistema não quebra e exibe os dados corretamente.
    """
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"slip": {"advice": "Test API integration!"}}
    
    resultado = obter_dica()
    
    assert resultado == "Dica da API: Test API integration!"
    mock_get.assert_called_once_with("https://api.adviceslip.com/advice", timeout=5)
    