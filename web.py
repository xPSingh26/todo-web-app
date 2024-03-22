import streamlit as st
import functions
import os

todos = functions.getTodos()


def add_todo():
    todo = st.session_state['todo']
    todos.append(todo + '\n')
    functions.writeTodos(todos)
    st.session_state['todo'] = ""


st.title("My To-Do App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writeTodos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input("", placeholder="Add a todo...", key='todo', on_change=add_todo)
