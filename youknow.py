import streamlit as st
from streamlit_sortables import sort_items

# Initialize session state with correct format
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"header": "To Do", "items": ["Task 1", "Task 2", "Task 3"]},
        {"header": "In Progress", "items": ["Task 4"]},
        {"header": "Done", "items": ["Task 5"]},
    ]

st.title("📝 Kanban Board with Instant Drag & Drop Updates")

# Function to add a new task
def add_task():
    new_task = st.session_state.new_task.strip()
    category = st.session_state.task_category

    if new_task:
        for column in st.session_state.tasks:
            if column["header"] == category:
                column["items"].append(new_task)
        st.session_state.new_task = ""  # Clear input field

# Task input form
st.text_input("New Task:", key="new_task")
st.selectbox("Select List:", ["To Do", "In Progress", "Done"], key="task_category")
st.button("➕ Add Task", on_click=add_task)

st.divider()

st.subheader("Kanban Board")

# Apply drag-and-drop across all columns in one go
updated_tasks = sort_items(
    st.session_state.tasks,
    multi_containers=True,  # Enable moving tasks between columns
    direction="vertical",   # Ensure vertical sorting within each column
)

# Force session state update to apply changes immediately
if updated_tasks != st.session_state.tasks:
    st.session_state.tasks = updated_tasks
    st.rerun()  # Forces an instant update so it doesn't require two drags

# Display updated task lists
st.write("### 🔄 Updated Task Lists:")
st.json(st.session_state.tasks)
