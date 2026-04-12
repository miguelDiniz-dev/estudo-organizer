from src.main import adicionar_tarefa, tarefas


def test_adicionar_tarefa_sucesso():
    tarefas.clear()
    assert adicionar_tarefa("Python", 2) is True
    assert len(tarefas) == 1


def test_adicionar_tarefa_invalida():
    assert adicionar_tarefa("", 0) is False


def test_lista_comeca_vazia():
    tarefas.clear()
    assert len(tarefas) == 0
    