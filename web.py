import streamlit as st
from streamlit import session_state
import functions

todos = functions.get_todos()
list_delete = []

def add_todo():
    new_todo = session_state["new_todo"] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)

def delete_todo():
    if session_state["delete_todo"]:
        for todo_delete in list_delete:
            todos.remove(todo_delete)
            functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    key_todo = f"{todo}_{index}"
    st.checkbox(todo, key=key_todo)
    if session_state[key_todo]:
        list_delete.append(todo)
st.text_input(label="",
              placeholder="Add a todo...",
              key="new_todo",
              on_change=add_todo)

st.button("delete", on_click=delete_todo, key="delete_todo")


print(session_state)