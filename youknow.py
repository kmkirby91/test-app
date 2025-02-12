import streamlit as st
from streamlit_sortables import sort_items

# Page Config
st.set_page_config(page_title="Kanban Board", layout="wide")

if 'count' not in st.session_state:
    st.session_state.count = 0

if 'my_lst' not in st.session_state:
    st.session_state['my_lst'] = []


# original_items = [
#     {'header': 'To do', 'items': ["Task 1", "Task 2", "Task 3"]},
#     {'header': "In Progress", 'items': ["Task 4", "Task 5"]}
# ]

itemss = [
    {'header': 'To do', 'items': ["Task 1", "Task 2", "Task 3"]},
    {'header': "In Progress", 'items': ["Task 4", "Task 5"]},
    {'header':"Done", 'items': ["Task 6"]} 
]

# Session State for Tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {'header': 'To do', 'items': ["Task 1", "Task 2", "Task 3"]},
        {'header': "In Progress", 'items': ["Task 4", "Task 5"]},
        {'header': "Done", 'items': ["Task 6"]}
    ]

# Am I even using this?
# def add_task():
#     new_task = st.session_state.get('new_task_input', '').strip()
#     category = st.session_state.get('new_task_category', 'To Do')
#     if new_task:
#         st.session_state.tasks[category].append(new_task)
#         del st.session_state['new_task_input']  # Clear input field
#         st.rerun()

st.title("📝 Kanban Board")

# Layout
col1, col2, col3 = st.columns(3)

# Function to update task lists
def update_tasks(column, updated_tasks):
    st.session_state.tasks[column] = updated_tasks
    # NEW LINE
    sort_items(st.session_state.tasks[column])

# Add new task
st.subheader("Add Task")
new_task = st.text_input("Task Name")
category = st.selectbox("Category", ["To Do", "In Progress", "Done"])
submit_button = st.button(label="Add Task")
if submit_button and new_task.strip() not in st.session_state.tasks[category]:
    st.session_state.tasks[category].append(new_task.strip())
#    st.session_state.my_lst.append(new_task.strip())
#    st.write( st.session_state['my_lst'] )
    st.write(st.session_state.tasks)
elif submit_button and new_task.strip() in st.session_state.tasks[category]:
    st.write("Duplicate :(")

# Kanban Columns
update_button=st.button(label="Update")
count2 = 1
if count2==1:
    with col1:
        st.subheader("To Do")
        # Sort the new list
        updated_todo4 = sort_items(st.session_state.tasks, multi_containers=True, direction='vertical')
        # Call update_tasks to write in the session state
        update_tasks("To Do", updated_todo4)
    with col2:
        st.subheader("In Progress")
        updated_in_progress = sort_items(st.session_state.tasks["In Progress"], key="in_progress")
        update_tasks("In Progress", updated_in_progress)
        st.session_state.count += 1
    with col3:  
        st.subheader("Done")
        updated_done = sort_items(st.session_state.tasks["Done"], key="done")
        update_tasks("Done", updated_done)

# with col1:
#     st.subheader("To Do")
#     # Sort the new list
#     updated_todo = sort_items(st.session_state.tasks["To Do"], key="todo")
#     # Call update_tasks to write in the session state
#     #update_tasks("To Do", updated_todo)
#     # pressme = st.button(label="PRESSME")
#     # if pressme and category == "To Do":
#     #     st.session_state.tasks["To Do"].append("hellooooo")
#     #     updated_todo2 = sort_items(st.session_state.tasks["To Do"], key="todo2")
#     #     update_tasks("To Do", updated_todo2)

# with col2:
#     st.subheader("In Progress")
#     updated_in_progress = sort_items(st.session_state.tasks["In Progress"], key="in_progress")
#     update_tasks("In Progress", updated_in_progress)
#     st.session_state.count += 1

# with col3:
#     st.subheader("Done")
#     updated_done = sort_items(st.session_state.tasks["Done"], key="done")
#     update_tasks("Done", updated_done)

# sort_items(st.session_state.tasks["Done"], key ="testtt")

# # update_button = st.button(label="Update list")
# # if update_button:
# #     with col1:
# #         st.subheader("To Do")
# # with col1:
# #     updated_todo3 = sort_items(st.session_state.tasks["To Do"], key="todo3")
# #     update_tasks("To Do", updated_todo3)
st.write('Count = ', st.session_state.count)





