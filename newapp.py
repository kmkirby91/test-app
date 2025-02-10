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

def add_task():
    new_task = st.session_state.get('new_task_input', '').strip()
    category = st.session_state.get('new_task_category', 'To Do')
    if new_task:
        st.session_state.tasks[category].append(new_task)
        del st.session_state['new_task_input']  # Clear input field
        st.rerun()

st.title("📝 Kanban Board")

# Layout
col1, col2, col3 = st.columns(3)

# Function to update task lists
def update_tasks(column, updated_tasks):
    st.session_state.tasks[column] = updated_tasks

# Kanban Columns
with col1:
    st.subheader("To Do")
    updated_todo = sort_items(st.session_state.tasks["To Do"], key="todo")
    update_tasks("To Do", updated_todo)

with col2:
    st.subheader("In Progress")
    updated_in_progress = sort_items(st.session_state.tasks["In Progress"], key="in_progress")
    update_tasks("In Progress", updated_in_progress)

with col3:
    st.subheader("Done")
    updated_done = sort_items(st.session_state.tasks["Done"], key="done")
    update_tasks("Done", updated_done)

# Add new task in main page
st.subheader("Add Task")
st.text_input("Task Name", key="new_task_input", on_change=add_task)
st.selectbox("Category", ["To Do", "In Progress", "Done"], key="new_task_category")
if st.button("Add Task"):
    add_task()
