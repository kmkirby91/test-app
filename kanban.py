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
    
    # Input for adding new tasks
    new_task = st.text_input("Add a new task:")
    if st.button("Add Task") and new_task:
        st.session_state.todo.append(new_task)
    
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
    
if __name__ == "__main__":
    main()