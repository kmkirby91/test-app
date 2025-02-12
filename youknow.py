import streamlit as st
from streamlit_sortables import sort_items

# Initialize session state with correct format
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"header": "To Do", "items": ["Task 1", "Task 2", "Task 3"]},
        {"header": "In Progress", "items": ["Task 4"]},
        {"header": "Done", "items": ["Task 5"]},
    ]

st.title("📝 Kanban Board with Multi-Container Drag & Drop")

# Function to add a new task
def add_task():
    new_task = st.session_state.new_task.strip()
    category = st.session_state.task_category

    if new_task:
        # Find the correct category and add the task
        for column in st.session_state.tasks:
            if column["header"] == category:
                column["items"].append(new_task)
        st.session_state.new_task = ""  # Clear input field

# Task input form
st.text_input("New Task:", key="new_task")
st.selectbox("Select List:", ["To Do", "In Progress", "Done"], key="task_category")
st.button("➕ Add Task", on_click=add_task)

st.divider()

# Kanban Board with Multi-Container Drag & Drop
st.subheader("Kanban Board")

st.session_state.tasks = sort_items(
    st.session_state.tasks,
    multi_containers=True,  # Enable moving between columns
)

# Display updated task lists
st.write("### 🔄 Updated Task Lists:")
st.json(st.session_state.tasks)
