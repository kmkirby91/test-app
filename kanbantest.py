import streamlit as st

# Initialize session state variables
if "kanban_board" not in st.session_state:
    st.session_state["kanban_board"] = {
        "Clinical": [],
        "Research": [],
        "Teaching": [],
        "Outreach": [],
        "Other": [],
    }

# Function to add a parent task with nested subtasks
def add_to_kanban_list(column, text_input_key):
    """Add a parent task and nested tasks to a Kanban column."""
    task_input = st.session_state.get(text_input_key, "").strip()
    if task_input:
        # Split the input into multiple lines
        lines = task_input.split("\n")
        if lines:
            # Parent task is the first line
            parent_task = {"task": lines[0], "subtasks": []}
            # Add subtasks if any
            for subtask in lines[1:]:
                parent_task["subtasks"].append(subtask.strip())
            st.session_state["kanban_board"][column].append(parent_task)
            st.session_state[text_input_key] = ""  # Clear input field

def delete_task(column, index):
    """Delete a task from a Kanban column."""
    st.session_state["kanban_board"][column].pop(index)

def kanban_board_page():
    """Render the Kanban-style board with multi-line tasks and nested subtasks."""
    st.title("Kanban Board")

    # CSS to ensure compact layout
    st.markdown(
        """
        <style>
        .parent-task {
            margin-bottom: 0px;
            line-height: 1.2; /* Adjust line height for parent task */
        }
        .subtask {
            margin-left: 20px;
            margin-top: -5px;
            margin-bottom: -5px;
            line-height: 1.2; /* Adjust line height for subtasks */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display and manage each column
    for column in ["Clinical", "Research", "Teaching", "Outreach", "Other"]:
        with st.expander(column):
            # Add task to the column
            task_input_key = f"{column}_input"
            st.text_area(
                f"Add task(s) to {column} (First line is the parent task, subsequent lines are subtasks)",
                key=task_input_key,
                on_change=add_to_kanban_list,
                args=(column, task_input_key),
                height=100,
            )

            # Display tasks in the column
            for index, task_data in enumerate(st.session_state["kanban_board"][column]):
                parent_task = task_data["task"]
                subtasks = task_data.get("subtasks", [])

                # Parent task row
                col1, col2 = st.columns([0.9, 0.1])
                with col1:
                    st.markdown(
                        f"<p class='parent-task'><strong>- {parent_task}</strong></p>",
                        unsafe_allow_html=True,
                    )
                with col2:
                    if st.button("🗑", key=f"{column}_{index}_delete"):
                        delete_task(column, index)

                # Subtasks
                if subtasks:
                    for subtask in subtasks:
                        st.markdown(
                            f"<p class='subtask'>- {subtask}</p>",
                            unsafe_allow_html=True,
                        )

# Main Function
def main():
    """Main function to display the Kanban Board."""
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Navigate", ["Kanban Board"])

    if page == "Kanban Board":
        kanban_board_page()

main()
