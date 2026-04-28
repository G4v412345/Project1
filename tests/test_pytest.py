import pytest
from main_1 import TodoApp



@pytest.fixture
def app():
    """"""
    app = TodoApp()
    app.tasks = []  
    return app



@pytest.mark.parametrize("input_text, expected_result", [
    ("Task 1", 1),
    ("Task 2", 1),
    ("   ", 0),     
    ("", 0)
])
def test_add_task_param(app, input_text, expected_result):
    app.add_task_logic(input_text)
    assert len(app.tasks) == expected_result



def test_mark_done(app):
    app.tasks = [{"text": "Task", "done": False}]
    app.selected_index = 0

    app.mark_done()

    assert app.tasks[0]["done"] is True

def test_delete_without_selection_raises_error():
    app = TodoApp()
    app.tasks = []

    with pytest.raises(Exception):
        app.selected_index = None
        app.delete_task()

@pytest.mark.skip(reason="Skip")
def test_skip_example():
    app = TodoApp()
    app.tasks = []

    app.add_task_logic("Skipped task")

    assert len(app.tasks) == 1

@pytest.mark.xfail(reason="Очікувана помилка у функції видалення без вибору задачі")
def test_delete_without_selection_xfail():
    app = TodoApp()
    app.tasks = []

    app.selected_index = None
    app.delete_task()

    assert len(app.tasks) == 1