import flet as ft 

class TodoModel:
    def __init__(self, todoMemo):
        self.todoMemo = todoMemo
        
class TodoService:
    def __init__(self):
        self.todoList = []
        
    def createTodo(self, todo):
        self.todoList.append(todo)
        
    def loadTodo(self):
        return self.todoList
    
def main(page: ft.Page):
    page.title = 'Flet Todo'
    todo_service= TodoService()
    
    def addClicked(e):
        newTodo = todo_input.value
        todoModelValue = TodoModel(newTodo)
        todo_service.createTodo(todoModelValue)
        fetchData()
        
    def fetchData():
        ListView.controls.clear()
        res = todo_service.loadTodo()
        for todo in res:
            aListTile = ft.Text(todo.todoMemo)
            ListView.controls.append(aListTile)
        page.update()
    
    ListView = ft.ListView(spacing=10, padding=20, auto_scroll=True, expand=1)
    
    todo_input = ft.TextField(label='Todo Input', width=200, multiline=2)
    add_button = ft.ElevatedButton('ADD', on_click=addClicked)
    
    page.add( todo_input, add_button, ListView)
    
ft.app(main)
    
    
