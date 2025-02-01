import streamlit as st
from streamlit_sortables import sort_items

def main():
    st.set_page_config(layout="wide")
    st.title("📝 Kanban Board with Streamlit")
    
    # Define initial Kanban board columns
    if "todo" not in st.session_state:
        st.session_state.todo = ["Task 1", "Task 2", "Task 3"]
    if "in_progress" not in st.session_state:
        st.session_state.in_progress = ["Task 4"]
    if "done" not in st.session_state:
        st.session_state.done = ["Task 5", "Task 6"]
    
    # Input for adding new task groups (multi-line bulleted list)
    if "task_input" not in st.session_state:
        st.session_state.task_input = "- "
    
    new_task = st.text_area("Add new task groups (each line automatically starts with a bullet '-'):", value=st.session_state.task_input, key="task_input", height=150)
    
    # Ensure each new line starts with a bullet
    modified_task = "\n".join(["- " + line.lstrip("- ") if line.strip() else "- " for line in new_task.split("\n")])
    st.session_state.task_input = modified_task
    
    if st.button("Add Tasks") and new_task.strip():
        task_lines = new_task.strip().split("\n")
        formatted_tasks = [line if line.startswith("-") else "- " + line for line in task_lines]
        formatted_task = "\n".join(formatted_tasks)
        
        if formatted_task:
            st.session_state.todo.append(formatted_task)  # Preserve line breaks inside the card
        
        # Reset the text area after adding tasks
        st.session_state.task_input = "- "
    
    # Display Kanban columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("To Do")
        st.session_state.todo = sort_items(st.session_state.todo, "todo", direction="vertical")
        
    with col2:
        st.subheader("In Progress")
        st.session_state.in_progress = sort_items(st.session_state.in_progress, "in_progress", direction="vertical")
        
    with col3:
        st.subheader("Done")
        st.session_state.done = sort_items(st.session_state.done, "done", direction="vertical")
    
    # Button to reset board
    if st.button("Reset Board"):
        st.session_state.todo = ["Task 1", "Task 2", "Task 3"]
        st.session_state.in_progress = ["Task 4"]
        st.session_state.done = ["Task 5", "Task 6"]
        st.session_state.task_input = "- "
    
if __name__ == "__main__":
    main()
