import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip()

    if todo:
        todos.append(todo + "\n")
        functions.write_todos(todos)

    # ✅ Clear the text input after adding
    st.session_state["new_todo"] = ""



st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checked = st.checkbox(todo.strip(), key=f"todo_{index}")
    if checked:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()

st.text_input(label="Add a new todo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo', label_visibility="collapsed")

print("hello")


