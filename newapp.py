import streamlit as st
from streamlit_sortables import sort_items

# Page Config
st.set_page_config(page_title="Kanban Board", layout="wide")

# Session State for Tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = {
        "To Do": ["Task 1", "Task 2", "Task 3"],
        "In Progress": ["Task 4", "Task 5"],
        "Done": ["Task 6"]
    }

st.title("📝 Kanban Board")

# Layout
col1, col2, col3 = st.columns(3)

# Function to update task lists
def update_tasks(column, updated_tasks):
    st.session_state.tasks[column] = updated_tasks

# Add new task using a form
st.subheader("Add Task")
with st.form(key="add_task_form"):
    new_task = st.text_input("Task Name")
    category = st.selectbox("Category", ["To Do", "In Progress", "Done"])
    submit_button = st.form_submit_button(label="Add Task")
    
    if submit_button and new_task.strip():
        st.session_state.tasks[category].append(new_task.strip())

# Kanban Columns
with col1:
    st.subheader("To Do")
    updated_todo = sort_items(st.session_state.tasks["To Do"], key="todo")
    update_tasks("To Do", updated_todo)
    pressme = st.button(label="PRESSME")
#    if pressme:
#        st.session_state.tasks["To Do"].append("hellooooo")
#        updated_todo = sort_items(st.session_state.tasks["To Do"], key="todo")
#        update_tasks("To Do", updated_todo)

with col2:
    st.subheader("In Progress")
    updated_in_progress = sort_items(st.session_state.tasks["In Progress"], key="in_progress")
    update_tasks("In Progress", updated_in_progress)

with col3:
    st.subheader("Done")
    updated_done = sort_items(st.session_state.tasks["Done"], key="done")
    update_tasks("Done", updated_done)

with col1:
        updated_todo2 = sort_items(st.session_state.tasks["To Do"], key="todo2")
        update_tasks("To Do", updated_todo2)


pressme2 = st.button(label="PRESSME2")
#        st.rerun()
#        updated_todo2 = sort_items(st.session_state.tasks["To Do"], key="todo2")
#        update_tasks("To Do", updated_todo2)
# 2/9/25 button adds to session state but page doesn't refresh