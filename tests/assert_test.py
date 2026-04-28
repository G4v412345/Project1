from main_1 import TodoApp

# add task
app = TodoApp()
app.tasks = []
app.add_task_logic("Task")
assert len(app.tasks) == 1

# empty task
app = TodoApp()
app.tasks = []
app.add_task_logic("   ")
assert len(app.tasks) == 0

# mark done
app = TodoApp()
app.tasks = [{"text": "Task", "done": False}]
app.selected_index = 0
app.mark_done()
assert app.tasks[0]["done"] is True

print("ALL TESTS PASSED")