import streamlit as st
from streamlit_sortables import sort_items

# Page Config
st.set_page_config(page_title="Kanban Board", layout="wide")

if 'count' not in st.session_state:
    st.session_state.count = 0

if 'my_lst' not in st.session_state:
    st.session_state['my_lst'] = []

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

# Function to update task lists
def update_tasks(column, updated_tasks):
    st.session_state.tasks[column] = updated_tasks

# Add new task
st.subheader("Add Task")
#with st.form(key="add_task_form"):
new_task = st.text_input("Task Name")
category = st.selectbox("Category", ["To Do", "In Progress", "Done"])
submit_button = st.button(label="Add Task")


st.write('Count = ', st.session_state.count) 

if submit_button and new_task.strip():
    st.session_state.tasks[category].append(new_task.strip())
    st.session_state.my_lst.append(new_task.strip())
    st.write( st.session_state['my_lst'] )
    st.write(st.session_state.tasks[category])
#    sort_items(st.session_state.tasks["To Do"], key="todo3")

sort_items(st.session_state.tasks["To Do"])



#with col1:
#        updated_todo2 = sort_items(st.session_state.tasks["To Do"], key="todo2")
#        update_tasks("To Do", updated_todo2)


# pressme2 = st.button(label="PRESSME2")
# if pressme2:
#     with col1:
#         updated_todo3 = sort_items(st.session_state.tasks["To Do"], key="todo3")
#         update_tasks("To Do", updated_todo3)
# st.rerun()
#        updated_todo2 = sort_items(st.session_state.tasks["To Do"], key="todo2")
#        update_tasks("To Do", updated_todo2)
# 2/9/25 button adds to session state but page doesn't refresh



