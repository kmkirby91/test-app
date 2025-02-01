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

def kanban_board_page():
    """Render the Kanban board with enforced wider columns."""
    st.title("Kanban Board")

    # CSS to force wider columns
    st.markdown(
        """
        <style>
        .css-1kyxreq {  /* Default Streamlit column container */
            display: flex;
            flex-wrap: nowrap;
        }
        .css-ocqkz7 {  /* Default Streamlit column */
            flex: 2 !important;  /* Make columns take twice the normal width */
        }
        .kanban-header {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            padding-bottom: 5px;
            white-space: nowrap;
        }
        .stTextArea textarea {
            min-height: 100px !important;
        }
        .parent-task {
            margin-bottom: 0px;
            line-height: 1.2;
        }
        .subtask {
            margin-left: 20px;
            margin-top: -5px;
            margin-bottom: -5px;
            line-height: 1.2;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Define Kanban board columns (default Streamlit way)
    columns = st.columns(5)  # This gets overridden by CSS for width control

    # Iterate through each column
    for col, section in zip(columns, ["Clinical", "Research", "Teaching", "Outreach", "Other"]):
        with col:
            # Properly aligned category titles
            st.markdown(f"<div class='kanban-header'>{section}</div>", unsafe_allow_html=True)

            # Task input area
            task_input_key = f"{section}_input"
            st.text_area(
                "",
                key=task_input_key,
                on_change=add_to_kanban_list,
                args=(section, task_input_key),
                height=100,  # Fixed height for alignment
            )

            # Display tasks in the column
            for task_data in st.session_state["kanban_board"][section]:
                parent_task = task_data["task"]
                subtasks = task_data.get("subtasks", [])

                # Display parent task
                st.markdown(
                    f"<p class='parent-task'><strong>- {parent_task}</strong></p>",
                    unsafe_allow_html=True,
                )

                # Display subtasks
                for subtask in subtasks:
                    st.markdown(
                        f"<p class='subtask'>- {subtask}</p>",
                        unsafe_allow_html=True,
                    )

# Main Function
def main():
    """Main function to display the Kanban Board."""
    st.sidebar.title("Navigation")
    kanban_board_page()

main()
