import unittest
from main_1 import TodoApp


class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.app = TodoApp()
        self.app.tasks = []  

    
    def test_add_task(self):
        self.app.add_task_logic("Task")
        self.assertEqual(len(self.app.tasks), 1)

    
    def test_mark_done(self):
        self.app.tasks = [{"text": "Task", "done": False}]
        self.app.selected_index = 0

        self.app.mark_done()

        self.assertTrue(self.app.tasks[0]["done"])


if __name__ == "__main__":
    unittest.main()